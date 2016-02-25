# Class for swupd integration -- generates input artefacts for consumption by
# swupd-server and calls swupd-server to process the inputs into update
# artefacts for consumption by swupd-client.
#
# Limitations:
# * Machine specific: generated swupd update artefacts are for a single MACHINE
#   only as reflected in the DEPLOY_DIR directories.
#
# Usage:
# * inherit this class in your core OS image. swupd-based OS's use bundles, the
#   primary one of which, os-core, is defined as the contents of this image.
# * Assign a list of names for bundles you wish to generate to the
#   SWUPD_BUNDLES variable i.e. SWUPD_BUNDLES = "feature_one feature_two"
# * Assign a list of packages for which their content should be included in
#   a bundle to a varflag of BUNDLE_CONTENTS which matches the bundle name
#   i.e. BUNDLE_CONTENTS[feature_one] = "package_one package_three package_six"
# * Ensure the OS_VERSION variable is assigned an integer value and increased
#   before each image build which should generate swupd update artefacts.
#
# An image that inherits this class will automatically have bundle 'chroots'
# created which contain the filesystem contents of the specified bundles.
# The mechanism to achieve this is that several virtual image recipes are
# created, one for each defined bundle plus a 'mega' image recipe.
# The 'mega' image contains the base image plus all of the bundles, whilst
# bundle images contain only the base image plus the contents of a single
# bundle.
#
# We build the mega image first, then the base image (the one which inherits
# this class) and finally all of the bundle images  . Each non-mega image
# has a manifest generated that lists all of the file contents of the image.
#
# Once the images and their manifests have been created each bundle image
# manifest is compared to the base image manifest in order to generate a delta
# list of files in the bundle image which don't exist in the base image.
# Files in this list are then preserved in the bundle directory for processing
# by swupd-server in order to generate update artefacts.
#
# Note: the reason for generating the mega image is to ensure that all files
# which are staged from the shared sysroot, i.e. passwd and groups, are
# fully populated.
# This is not an ideal compromise and requires further thought.
#
# TODO: we're copying a lot of potentially duplicate files into
# DEPLOY_DIR_SWUPD consider using hardlink to de-duplicate the files and save
# some disk space.

DEPLOY_DIR_SWUPDBASE = "${DEPLOY_DIR}/swupd/${MACHINE}"
SWUPD_ROOTFS_MANIFEST = "${IMAGE_BASENAME}-files-in-image.txt"

# User configurable variables to disable all swupd processing or deltapack
# generation.
SWUPD_GENERATE ??= "1"
SWUPD_DELTAPACKS ??= "1"
# Create delta packs for N versions back — default 2
SWUPD_N_DELTAPACK ??= "2"
# Amount the OS_VERSION should be increased by for each release, used by the
# delta pack looping to generate delta packs going back up toSWUPD_N_DELTAPACK
# releases
SWUPD_VERSION_STEP ??= "10"
# Set this to 0 to prevent virtual images being automatically deleted
SWUPD_RM_BUNDLE_IMAGES ??= "1"

# This version number *must* map to VERSION_ID in /etc/os-release and *must* be
# a non-negative integer that fits in an int.
OS_VERSION ??= "${DISTRO_VERSION}"

IMAGE_INSTALL_append = " swupd-client os-release"
# We need full-fat versions of these for swupd (at least as of 2.87)
IMAGE_INSTALL_append = " gzip bzip2 tar xz"

inherit distro_features_check
REQUIRED_DISTRO_FEATURES = "systemd"

python () {
    if d.getVar('VIRTUAL-RUNTIME_init_manager', True) != 'systemd':
        bb.error('swupd integration requires the systemd init manager')

    ver = d.getVar('OS_VERSION', True) or 'invalid'
    try:
        int(ver)
    except ValueError:
        bb.fatal("Invalid value for OS_VERSION (%s), must be a non-negative integer value." % ver)

    pn_base = d.getVar('PN_BASE', True)
    if pn_base is not None:
        # We want all virtual images from this recipe to deploy to the same
        # directory
        deploy_dir = d.getVar('DEPLOY_DIR_SWUPDBASE')
        deploy_dir = os.path.join(deploy_dir, pn_base)
        d.setVar('DEPLOY_DIR_SWUPD', deploy_dir)

        # We need all virtual images from this recipe to share the same pseudo
        # database so that permissions are correctly set in the copied bundle
        # directories when swupd post-processing happens
        pseudo_state = d.expand('${TMPDIR}/work-shared/${PN_BASE}/pseudo')
        d.setVar('PSEUDO_LOCALSTATEDIR', pseudo_state)

        # Non-base (bundle) images which aren't the mega image must depend on
        # the base image having been built and its contents staged in
        # DEPLOY_DIR_SWUPD so that those contents can be compared against in
        # the do_prune_bundle task
        if (d.getVar('BUNDLE_NAME') or "") == 'mega':
            return
        base_copy = (' %s:do_copy_bundle_contents' % pn_base)
        d.appendVarFlag('do_prune_bundle', 'depends', base_copy)
        return

    # We use a shared Pseudo database in order to ensure that all tasks have
    # full awareness of the files created for the base image recipe and each
    # of its virtual recipes.
    # However, we must be careful with the pseudo database and managing
    # database lifecycles in order to avoid confusion should inode numbers be
    # reused when files are deleted outside of pseudo's awareness.
    #
    # TODO: Figure out database lifecycles. When can we be sure that deleting
    # the database is appropriate? We need it to live for the generation of
    # an image and all of its virtual images.
    pseudo_state = d.expand('${TMPDIR}/work-shared/${IMAGE_BASENAME}/pseudo')
    d.setVar('PSEUDO_LOCALSTATEDIR', pseudo_state)

    deploy_dir = d.expand('${DEPLOY_DIR_SWUPDBASE}/${IMAGE_BASENAME}')
    d.setVar('DEPLOY_DIR_SWUPD', deploy_dir)
    varflags = '%s/image %s/empty %s/www %s' % (deploy_dir, deploy_dir, deploy_dir, deploy_dir)
    d.setVarFlag('do_swupd_update', 'dirs', varflags)

    # For the base image only, set the BUNDLE_NAME to os-core and generate the
    # virtual images for each bundle and the mega image
    d.setVar('BUNDLE_NAME', 'os-core')

    bundles = (d.getVar('SWUPD_BUNDLES', True) or "").split()
    extended = (d.getVar('BBCLASSEXTEND', True) or "").split()

    # Generate virtual images for each of the bundles, the base image + the
    # bundle contents. Add each virtual image's do_prune_bundle task as a
    # dependency of the base image as we can't generate the update until all
    # dependent images are done with their build, 'chroot' populate and pruning
    pn = d.getVar('PN', True)
    for bndl in bundles:
        extended.append('swupdbundle:%s' % bndl)
        dep = ' %s-%s:do_prune_bundle' % (pn, bndl)
        d.appendVarFlag ('do_swupd_update', 'depends', dep)
    extended.append('swupdbundle:mega')
    d.setVar('BBCLASSEXTEND', ' '.join(extended))

    # The base image should depend on the mega-image having been populated
    # to ensure that we're staging the same shared files from the sysroot as
    # the bundle images.
    mega_name = (' %s-mega:do_image_complete' % d.getVar('PN', True))
    d.appendVarFlag('do_rootfs', 'depends', mega_name)
}

fakeroot do_rootfs_append () {
    bndl = d.getVar('BUNDLE_NAME', True)
    if (bndl == 'mega'):
        return

    # swupd-client expects a bundle subscription to exist for each
    # installed bundle. This is simply an empty file named for the
    # bundle in /usr/share/clear/bundles
    bundledir = d.expand('${IMAGE_ROOTFS}/usr/share/clear/bundles')
    bb.utils.mkdirhier(bundledir)
    open(os.path.join(bundledir, bndl), 'w+b').close()
}

# Stage the contents of the generated image rootfs, and a manifest listing all
# of the files in the image, for further processing.
fakeroot do_copy_bundle_contents () {
    bbdebug 2 "Considering copying bundle contents for ${PN}"
    if [ "${BUNDLE_NAME}" != "mega" ] ; then
        bbdebug 2 "Copying ${BUNDLE_NAME} contents"
        outfile="${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${SWUPD_ROOTFS_MANIFEST}"
        bundledir="${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${BUNDLE_NAME}/"
        rootfs="${IMAGE_ROOTFS}"
        mkdir -p $bundledir
        # Generate a manifest of the bundle contents for pruning
        cd $rootfs && find . ! -path . > $outfile
        # Copy the rootfs tree preserving the files and all of their attributes
        cp -a $rootfs/* $bundledir
    fi
}
# Needs to run after do_image_complete so that IMAGE_POSTPROCESS commands have run
addtask copy_bundle_contents after do_image_complete before do_prune_bundle

# Generate a list of files which exist in the bundle image, but not the base
# image.
def delta_contents(difflist):
    # '- ' - line unique to lhs
    # '+ ' - line unique to rhs
    # '  ' - line common
    # '? ' - line not present in either
    #
    # difflist should be a list containing the output of difflib.Differ.compare
    #       where the lhs (left-hand-side) was the base image and the rhs
    #       (right-hand-side) was base image + extras (the bundle image).
    #
    # returns a list containing the items which are unique in the rhs
    cont = []
    for ln in difflist:
        if ln[0] == '+':
            cont.append(ln[3:])
    return cont

# Compare the bundle image manifest to the base image manifest and return
# a list of files unique to the bundle image.
def unique_contents(base_manifest_fn, image_manifest_fn):
    import difflib
    differ = difflib.Differ()

    base_manifest_list = []
    with open(base_manifest_fn) as base:
        base_manifest_list = base.read().splitlines()

    image_manifest_list = []
    with open(image_manifest_fn) as image:
        image_manifest_list = image.read().splitlines()

    delta = list(differ.compare(base_manifest_list, image_manifest_list))

    return delta_contents(delta)

fakeroot python do_prune_bundle () {
    bundle = d.getVar('BUNDLE_NAME', True) or ''
    if not bundle:
        bb.warn('Trying to prune bundle of a non-bundle image: ' % d.getVar('PN', True))
        return

    if bundle == 'mega' or bundle == 'os-core':
        bb.debug(2, 'Skipping bundle pruning for %s image' % bundle)
        return

    # Get a list of files in the bundle which aren't in the base image
    pn_base = d.getVar("PN_BASE", True)
    image_manifest = d.expand("${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${SWUPD_ROOTFS_MANIFEST}")
    base_manifest = image_manifest.replace('-%s' % bundle, '')
    bb.debug(1, "Comparing manifest %s to %s" % (base_manifest, image_manifest))
    bundle_file_contents = unique_contents(base_manifest, image_manifest)
    bb.debug(1, '%s has %s unique contents' % (d.getVar('PN', True), len(bundle_file_contents)))

    # now we have a list of bundle files we can go ahead and delete files in
    # the bundle directory which aren't in this list.
    bundledir = d.expand('${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${BUNDLE_NAME}/')
    bb.debug(1, "Creating and pruning %s bundle dir (%s)" % (bundle, bundledir))
    for root, dirs, files in os.walk(bundledir):
        relroot = root.replace(bundledir, '/')
        for f in files:
            fpath = os.path.join(relroot, f)
            if fpath not in bundle_file_contents:
                bb.debug(3, 'Pruning %s from the bundle\n\t%s' % (fpath, os.path.join(root, f)))
                os.remove(os.path.join(root, f))

    # Now need to clean up empty directories
    for dir, _, _ in os.walk(bundledir, topdown=False):
        try:
            os.rmdir(dir)
        except OSError as err:
            bb.debug(2, 'Not removing %s, reason: %s' % (dir, err.strerror))
    bb.debug(1, "Done pruning %s bundle dir (%s)" % (bundle, bundledir))
}
addtask prune_bundle after do_copy_bundle_contents before do_swupd_update

# Automated removal of the bundle images, in order to reduce disk space impact
python rm_bundle_images () {
    if d.getVar('SWUPD_RM_BUNDLE_IMAGES', True) != '1':
        bb.debug(1, 'Not deleting images, SWUPD_RM_BUNDLE_IMAGES = "1"')
        return

    if d.getVar('PN_BASE', True) is None:
        return

    bb.debug(2, 'Removing image files for %s' % d.getVar('IMAGE_NAME', True))

    import fnmatch

    image_dir = d.getVar('DEPLOY_DIR_IMAGE', True)

    pattern = '%s.*' % d.getVar('IMAGE_LINK_NAME', True)
    bb.debug(3, 'removing files matching pattern: %s' % pattern)
    for img in os.listdir(image_dir):
        if fnmatch.fnmatch(img, pattern):
            os.unlink('%s/%s' % (image_dir, img))

    pattern = '%s.*' % d.getVar('IMAGE_NAME', True)
    bb.debug(3, 'removing files matching pattern: %s' % pattern)
    for img in os.listdir(image_dir):
        if fnmatch.fnmatch(img, pattern):
            os.unlink('%s/%s' % (image_dir, img))
}
do_image_complete[postfuncs] += "rm_bundle_images"

fakeroot do_swupd_update () {
    if [ ! -z "${PN_BASE}" ]; then
        bbwarn 'We only generate swupd updates for the base image, skipping ${PN}'
        exit
    fi

    if [ ! "${SWUPD_GENERATE}" -eq 1 ]; then
        bbnote 'Update generation disabled, skipping.'
        exit
    fi

    export SWUPD_CERTS_DIR="${STAGING_ETCDIR_NATIVE}/swupd-certs"
    export LEAF_KEY="leaf.key.pem"
    export LEAF_CERT="leaf.cert.pem"
    export CA_CHAIN_CERT="ca-chain.cert.pem"
    export PASSPHRASE="${SWUPD_CERTS_DIR}/passphrase"

    export XZ_DEFAULTS="--threads 0"

    bbdebug 1 "New OS_VERSION is ${OS_VERSION}"
    # If the swupd directory already exists don't trample over it, but let
    # the user know we're not doing any update generation.
    if [ -e ${DEPLOY_DIR_SWUPD}/www/${OS_VERSION} ]; then
        bbwarn 'swupd image directory exists for OS_VERSION=${OS_VERSION}, not generating updates.'
        bbwarn 'Ensure OS_VERSION is incremented if you want to generate updates.'
        exit
    fi

    mkdir -p ${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/os-core
    cp -ar ${IMAGE_ROOTFS}/* ${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/os-core/

    # Generate swupd-server configuration
    bbdebug 1 "Writing ${DEPLOY_DIR_SWUPD}/server.ini"
    if [ -e "${DEPLOY_DIR_SWUPD}/server.ini" ]; then
       rm ${DEPLOY_DIR_SWUPD}/server.ini
    fi
    cat << END > ${DEPLOY_DIR_SWUPD}/server.ini
[Server]
imagebase=${DEPLOY_DIR_SWUPD}/image/
outputdir=${DEPLOY_DIR_SWUPD}/www/
emptydir=${DEPLOY_DIR_SWUPD}/empty/
END

    if [ -e ${DEPLOY_DIR_SWUPD}/image/latest.version ]; then
        PREVREL=`cat ${DEPLOY_DIR_SWUPD}/image/latest.version`
    else
        bbdebug 1 "Stubbing out empty latest.version file"
        touch ${DEPLOY_DIR_SWUPD}/image/latest.version
        PREVREL="0"
    fi

    GROUPS_INI="${DEPLOY_DIR_SWUPD}/groups.ini"
    bbdebug 1 "Writing ${GROUPS_INI}"
    if [ -e "${DEPLOY_DIR_SWUPD}/groups.ini" ]; then
       rm ${DEPLOY_DIR_SWUPD}/groups.ini
    fi
    for bndl in ${SWUPD_BUNDLES}; do
        echo "[$bndl]" >> ${GROUPS_INI}
        echo "group=$bndl" >> ${GROUPS_INI}
        echo "" >> ${GROUPS_INI}
    done

    bbdebug 1 "Generating update from PREVREL to ${OS_VERSION}"
    ${STAGING_BINDIR_NATIVE}/swupd_create_update -S ${DEPLOY_DIR_SWUPD} --osversion ${OS_VERSION}

    bbdebug 1 "Generating fullfiles for ${OS_VERSION}"
    ${STAGING_BINDIR_NATIVE}/swupd_make_fullfiles -S ${DEPLOY_DIR_SWUPD} ${OS_VERSION}

    bbdebug 1 "Generating zero packs, this can take some time."
    ${STAGING_BINDIR_NATIVE}/swupd_make_pack -S ${DEPLOY_DIR_SWUPD} 0 ${OS_VERSION} os-core
    for bndl in ${SWUPD_BUNDLES}; do
        bbdebug 2 "Generating zero pack for $bndl"
        ${STAGING_BINDIR_NATIVE}/swupd_make_pack -S ${DEPLOY_DIR_SWUPD} 0 ${OS_VERSION} $bndl
    done

    # Generate delta-packs going back SWUPD_N_DELTAPACK versions
    if [ ${SWUPD_DELTAPACKS} -eq 1 -a ${SWUPD_N_DELTAPACK} -gt 0 -a $PREVREL -gt 0 ]; then
        bbdebug 1 "Generating delta pack with previous release $PREVREL"
        bundles="os-core ${SWUPD_BUNDLES}"
        for bndl in $bundles; do
            bndlcnt=0
            prevver=$PREVREL
            while [ $bndlcnt -lt ${SWUPD_N_DELTAPACK} -a $prevver -gt 0 ]; do
                if [ -e ${DEPLOY_DIR_SWUPD}/image/$prevver/$bndl ]; then
                    bbdebug 2 "Generating delta pack from $prevver to ${OS_VERSION} for $bndl"
                    ${STAGING_BINDIR_NATIVE}/swupd_make_pack -S ${DEPLOY_DIR_SWUPD} $prevver ${OS_VERSION} $bndl
                    bndlcnt=`expr $bndlcnt + 1`
                fi
                # Both let and expr return 1 if the expression evaluates to 0,
                # bitbake catches the non-zero exit code from a shell command
                # end exits with an error - special case to work around this.
                if [ $prevver -eq ${SWUPD_VERSION_STEP} ]; then
                    prevver=0
                else
                    prevver=`expr $prevver - ${SWUPD_VERSION_STEP}`
                fi
            done
        done
    fi

    # Write version to www/version/format3/latest and image/latest.version
    bbdebug 2 "Writing latest file"
    mkdir -p ${DEPLOY_DIR_SWUPD}/www/version/format3
    echo ${OS_VERSION} > ${DEPLOY_DIR_SWUPD}/www/version/format3/latest
    echo ${OS_VERSION} > ${DEPLOY_DIR_SWUPD}/image/latest.version
}

python rm_shared_pseudodb () {
    pseudo_state = d.expand('${TMPDIR}/work-shared/${IMAGE_BASENAME}/pseudo')
    bb.utils.prunedir(pseudo_state)
}
do_swupd_update[postfuncs] += "rm_shared_pseudodb"

SWUPDDEPENDS = "\
    virtual/fakeroot-native:do_populate_sysroot \
    rsync-native:do_populate_sysroot \
    swupd-server-native:do_populate_sysroot \
"
addtask swupd_update after do_image_complete after do_copy_bundle_contents after do_prune_bundle before do_build
do_swupd_update[depends] = "${SWUPDDEPENDS}"
