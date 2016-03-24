# Class for swupd integration -- generates input artefacts for consumption by
# swupd-server and calls swupd-server to process the inputs into update
# artefacts for consumption by swupd-client.
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
# See HOWTO.md for more information.

DEPLOY_DIR_SWUPDBASE = "${DEPLOY_DIR}/swupd/${MACHINE}"
SWUPD_ROOTFS_MANIFEST_SUFFIX = "-files-in-image.txt"
SWUPD_ROOTFS_MANIFEST = "${PN}${SWUPD_ROOTFS_MANIFEST_SUFFIX}"

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

# This version number *must* map to VERSION_ID in /etc/os-release and *must* be
# a non-negative integer that fits in an int.
OS_VERSION ??= "${DISTRO_VERSION}"

IMAGE_INSTALL_append = " swupd-client os-release"
# We need full-fat versions of these for swupd (at least as of 2.87)
IMAGE_INSTALL_append = " gzip bzip2 tar xz"

# We need to preserve xattrs which is only supported by GNU tar >= 1.27
# to be sure this functionality works as expected use the tar-replacement-native
DEPENDS += "tar-replacement-native"
EXTRANATIVEPATH += "tar-native"

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

    havebundles = (d.getVar('SWUPD_BUNDLES', True) or '') != ''

    pn_base = d.getVar('PN_BASE', True)
    pn = d.getVar('PN', True)

    # We set the path to the rootfs folder of the mega image here so that
    # it's simple to refer to later
    megarootfs = d.getVar('IMAGE_ROOTFS', True)
    if havebundles:
        megarootfs = megarootfs.replace('/' + pn +'/', '/bundle-%s-mega/' % (pn_base or pn))
        d.setVar('MEGA_IMAGE_ROOTFS', megarootfs)

    if pn_base is not None:
        # We want all virtual images from this recipe to deploy to the same
        # directory
        deploy_dir = d.getVar('DEPLOY_DIR_SWUPDBASE', True)
        deploy_dir = os.path.join(deploy_dir, pn_base)
        d.setVar('DEPLOY_DIR_SWUPD', deploy_dir)

        # We need all virtual images from this recipe to share the same pseudo
        # database so that permissions are correctly set in the copied bundle
        # directories when swupd post-processing happens.
        #
        # Because real image building via SWUPD_IMAGES can happen also after
        # the initial "bitbake <core image>" invocation, we have to keep that
        # pseudo database around and cannot delete it.
        pseudo_state = d.expand('${TMPDIR}/work-shared/${PN_BASE}/pseudo')
        d.setVar('PSEUDO_LOCALSTATEDIR', pseudo_state)

        # Non-base (bundle) images which aren't the mega image must depend on
        # the base image having been built and its contents staged in
        # DEPLOY_DIR_SWUPD so that those contents can be compared against in
        # the do_prune_bundle task
        bundle_name = d.getVar('BUNDLE_NAME', True) or ""
        if bundle_name == 'mega':
            return
        base_copy = (' %s:do_copy_bundle_contents' % pn_base)
        d.appendVarFlag('do_prune_bundle', 'depends', base_copy)
        # The bundle contents will be copied from the mega image rootfs, thus
        # we need to ensure that the mega image is finished building before
        # we try and perform any bundle contents copying for other images
        mega_image = (' bundle-%s-mega:do_image_complete' % pn_base)
        d.appendVarFlag('do_copy_bundle_contents', 'depends', mega_image)

        return

    # We use a shared Pseudo database in order to ensure that all tasks have
    # full awareness of the files created for the base image recipe and each
    # of its virtual recipes.
    # However, we must be careful with the pseudo database and managing
    # database lifecycles in order to avoid confusion should inode numbers be
    # reused when files are deleted outside of pseudo's awareness.
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

    if 'mega' in bundles:
        bb.error('SWUPD_BUNDLES contains an item named "mega", this is a reserved name. Please rename that bundle.')

    # Generate virtual images for each of the bundles, the base image + the
    # bundle contents. Add each virtual image's do_prune_bundle task as a
    # dependency of the base image as we can't generate the update until all
    # dependent images are done with their build, 'chroot' populate and pruning
    for bndl in bundles:
        extended.append('swupdbundle:%s' % bndl)
        dep = ' bundle-%s-%s:do_prune_bundle' % (pn, bndl)
        d.appendVarFlag ('do_swupd_update', 'depends', dep)

    if havebundles:
        extended.append('swupdbundle:mega')

    # Generate real image files from the os-core bundle plus
    # certain additional bundles. All of these images can share
    # the same swupd update stream, the only difference is the
    # number of pre-installed bundles.
    for imageext in (d.getVar('SWUPD_IMAGES', True) or '').split():
        extended.append('swupdimage:%s' % imageext)

    d.setVar('BBCLASSEXTEND', ' '.join(extended))

    # The base image should depend on the mega-image having been populated
    # to ensure that we're staging the same shared files from the sysroot as
    # the bundle images.
    if havebundles:
        mega_name = (' bundle-%s-mega:do_image_complete' % pn)
        d.appendVarFlag('do_rootfs', 'depends', mega_name)
}

def copyxattrtree(src, dst):
    import subprocess

    bb.utils.mkdirhier(dst)
    # tar does not properly copy xattrs when used like this.
    # See the comment on tar in meta/classes/image_types.bbclass
    cmd = "tar --xattrs --xattrs-include='*' -cf - -C %s -p . | tar -p --xattrs --xattrs-include='*' -xf - -C %s" % (src, dst)
    oe.path.check_output(cmd, shell=True, stderr=subprocess.STDOUT)

# swupd-client expects a bundle subscription to exist for each
# installed bundle. This is simply an empty file named for the
# bundle in /usr/share/clear/bundles
def create_bundle_manifest(d, bundlename):
    bundledir = d.expand('${IMAGE_ROOTFS}/usr/share/clear/bundles')
    bb.utils.mkdirhier(bundledir)
    open(os.path.join(bundledir, bundlename), 'w+b').close()

fakeroot do_rootfs_append () {
    bundle = d.getVar('BUNDLE_NAME', True)
    bundles = ['os-core']
    if bundle == 'mega':
        bundles.extend((d.getVar('SWUPD_BUNDLES', True) or '').split())
    else:
        bundles.append(bundle)
    # swupd-client expects a bundle subscription to exist for each
    # installed bundle. This is simply an empty file named for the
    # bundle in /usr/share/clear/bundles
    for bundle in bundles:
        create_bundle_manifest(d, bundle)
}

def swupd_create_rootfs(d):
    imagefstypes = d.getVar('IMAGE_FSTYPES', d)
    if not imagefstypes:
        # Not producing real images, so there's no need to copy
        # files from the mega image.
        return
    pn = d.getVar('PN', True)
    pn_base = d.getVar('PN_BASE', True)
    imageext = d.getVar('IMAGE_BUNDLE_NAME', True) or ''

    # Sanity checking was already done in swupdimage.bbclass.
    # Here we can simply use the settings.
    imagebundles = d.getVarFlag('SWUPD_IMAGES', imageext, True).split() if imageext else []
    rootfs = d.getVar('IMAGE_ROOTFS', True)
    rootfs_contents = []
    if not pn_base:
        import subprocess

        # For the base image only we need to remove all of the files that were
        # installed during the base do_rootfs and replace them with the
        # equivalent files from the mega image.
        #
        # The virtual image recipes will already have an empty rootfs.
        outfile = d.expand('${WORKDIR}/orig-rootfs-manifest.txt')
        rootfs = d.getVar('IMAGE_ROOTFS', True)
        # Generate a manifest of the current file contents
        manifest_cmd = 'cd %s && find . ! -path . > %s' % (rootfs, outfile)
        subprocess.call(manifest_cmd, shell=True, stderr=subprocess.STDOUT)
        # Remove the current rootfs contents
        oe.path.remove('%s/*' % rootfs)
        for entry in manifest_to_file_list(outfile):
            rootfs_contents.append(entry[1:])
        # clean up
        os.unlink(outfile)
    else:
        manifest = d.expand("${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${PN_BASE}${SWUPD_ROOTFS_MANIFEST_SUFFIX}")
        for entry in manifest_to_file_list(manifest):
            rootfs_contents.append(entry[1:])

    # Copy all files from the mega bundle...
    copyxattrtree(d.getVar('MEGA_IMAGE_ROOTFS', True), rootfs)

    # ... and then remove files again which shouldn't have been copied.
    for bundle in imagebundles:
        manifest = d.expand("${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/bundle-${PN_BASE}-%s${SWUPD_ROOTFS_MANIFEST_SUFFIX}") % bundle
        for entry in manifest_to_file_list(manifest):
            rootfs_contents.append(entry[1:])

    # Prune the items not in the manifest
    remove_unlisted_files_from_directory(rootfs_contents, rootfs)

do_image_append () {
    swupd_create_rootfs(d)
}

# Stage the contents of the generated image rootfs, and a manifest listing all
# of the files in the image, for further processing.
fakeroot python do_copy_bundle_contents () {
    import subprocess

    bndl = d.getVar('BUNDLE_NAME', True)
    if not bndl or bndl == 'mega':
        return

    bb.debug(2, "Copying %s contents" % bndl)
    outfile = d.expand('${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${SWUPD_ROOTFS_MANIFEST}')
    bundledir = d.expand('${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${BUNDLE_NAME}/')
    rootfs = d.getVar('IMAGE_ROOTFS', True)

    # Generate a manifest of the bundle contents for pruning
    bb.utils.mkdirhier(bundledir)
    manifest_cmd = 'cd %s && find . ! -path . > %s' % (rootfs, outfile)
    subprocess.call(manifest_cmd, shell=True, stderr=subprocess.STDOUT)

    # Copy the entire mega image's contents, we'll prune this down to only
    # the files in the manifest in do_prune_bundle
    copyxattrtree(d.getVar('MEGA_IMAGE_ROOTFS', True), bundledir)

    create_bundle_manifest(d, bndl)
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

# Open a manifest file and read it into a list
def manifest_to_file_list(manifest_fn):
    image_manifest_list = []
    with open(manifest_fn) as image:
        image_manifest_list = image.read().splitlines()

    return image_manifest_list

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

# Takes a list of files and a base directory, removes items from the base
# directory which don't exist in the list
def remove_unlisted_files_from_directory (file_list, directory, fullprune=False):
    for root, dirs, files in os.walk(directory):
        replace = '/'
        if not directory.endswith('/'):
            replace = ''
        relroot = root.replace(directory, replace)
        #bb.debug(1, 'Substituting "%s" for %s in root of %s to give %s' % (replace, directory, root, relroot))
        for f in files:
            fpath = os.path.join(relroot, f)
            if fpath not in file_list:
                bb.debug(3, 'Pruning %s from the bundle (%s)' % (fpath, os.path.join(root, f)))
                os.remove(os.path.join(root, f))

    # Now need to clean up empty directories, unless they were listed in the
    # the bundle's manifest
    for dir, _, _ in os.walk(directory, topdown=False):
        replace = '/'
        if not directory.endswith('/'):
            replace = ''
        d = dir.replace(directory, replace)
        bb.debug(3, 'Checking whether to delete %s (%s)' % (d, dir))
        if fullprune or (d not in file_list):
            try:
                bb.debug(3, 'Attempting to remove unwanted directory %s (%s)' % (d, dir))
                os.rmdir(dir)
            except OSError as err:
                bb.debug(2, 'Not removing %s, reason: %s' % (dir, err.strerror))
        else:
            bb.debug(3, 'Not removing wanted empty directory %s' % d)

fakeroot python do_prune_bundle () {
    bundle = d.getVar('BUNDLE_NAME', True)
    if not bundle:
        return

    if bundle == 'mega':
        bb.debug(2, 'Skipping bundle pruning for %s image' % bundle)
        return

    # Get a list of files in the bundle which aren't in the base image
    pn_base = d.getVar("PN_BASE", True)
    bundle_file_contents = []
    image_manifest = d.expand("${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${SWUPD_ROOTFS_MANIFEST}")
    fullprune = True
    if not pn_base:
        fullprune = False
        manifest_files = manifest_to_file_list(image_manifest)
        bundle_file_contents = []
        # The manifest files have a leading . before the /
        for f in manifest_files:
            bundle_file_contents.append(f[1:])
        bb.debug(1, 'os-core has %s unique contents' % len(bundle_file_contents))
    else:
        base_manifest = image_manifest.replace('-%s' % bundle, '').replace('/bundle-', '/')
        bb.debug(3, "Comparing manifest %s to %s" % (base_manifest, image_manifest))
        bundle_file_contents = unique_contents(base_manifest, image_manifest)
        bb.debug(3, '%s has %s unique contents' % (d.getVar('PN', True), len(bundle_file_contents)))

    # now we have a list of bundle files we can go ahead and delete files in
    # the bundle directory which aren't in this list.
    bundledir = d.expand('${DEPLOY_DIR_SWUPD}/image/${OS_VERSION}/${BUNDLE_NAME}/')
    bb.debug(1, "Creating and pruning %s bundle dir (%s)" % (bundle, bundledir))
    remove_unlisted_files_from_directory (bundle_file_contents, bundledir, fullprune)
    bb.debug(1, "Done pruning %s bundle dir (%s)" % (bundle, bundledir))
}
addtask prune_bundle after do_copy_bundle_contents before do_swupd_update

fakeroot do_swupd_update () {
    if [ -z "${BUNDLE_NAME}" ] || [ ! -z "${PN_BASE}" ] ; then
        bbwarn 'We only generate swupd updates for the base image, skipping ${PN}:do_swupd_update'
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
    touch ${GROUPS_INI}
    for bndl in ${SWUPD_BUNDLES}; do
        echo "[$bndl]" >> ${GROUPS_INI}
        echo "group=$bndl" >> ${GROUPS_INI}
        echo "" >> ${GROUPS_INI}
    done

    bbdebug 1 "Generating update from $PREVREL to ${OS_VERSION}"
    ${STAGING_BINDIR_NATIVE}/swupd_create_update -S ${DEPLOY_DIR_SWUPD} --osversion ${OS_VERSION}

    bbdebug 1 "Generating fullfiles for ${OS_VERSION}"
    ${STAGING_BINDIR_NATIVE}/swupd_make_fullfiles -S ${DEPLOY_DIR_SWUPD} ${OS_VERSION}

    bbdebug 1 "Generating zero packs, this can take some time."
    bundles="os-core ${SWUPD_BUNDLES}"
    for bndl in $bundles; do
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

SWUPDDEPENDS = "\
    virtual/fakeroot-native:do_populate_sysroot \
    rsync-native:do_populate_sysroot \
    swupd-server-native:do_populate_sysroot \
"
addtask swupd_update after do_image_complete after do_copy_bundle_contents after do_prune_bundle before do_build
do_swupd_update[depends] = "${SWUPDDEPENDS}"

# pseudo does not handle xattrs correctly for hardlinks:
# https://bugzilla.yoctoproject.org/show_bug.cgi?id=9317
#
# This started to become a problem when copying rootfs
# content around for swupd bundle creation. As a workaround,
# we avoid having hardlinks in the rootfs and replace them
# with symlinks.
python swupd_replace_hardlinks () {
    import os
    import stat

    # Collect all inodes and which entries share them.
    inodes = {}
    for root, dirs, files in os.walk(d.getVar('IMAGE_ROOTFS', True)):
        for file in files:
            path = os.path.join(root, file)
            s = os.lstat(path)
            if stat.S_ISREG(s.st_mode):
                inodes.setdefault(s.st_ino, []).append(path)

    for inode, paths in inodes.iteritems():
        if len(paths) > 1:
            paths.sort()
            bb.debug(3, 'Removing hardlinks: %s' % ' = '.join(paths))
            # Arbitrarily pick the first entry as symlink target.
            target = paths.pop(0)
            for path in paths:
                reltarget = os.path.relpath(target, os.path.dirname(path))
                os.unlink(path)
                os.symlink(reltarget, path)
}
ROOTFS_POSTPROCESS_COMMAND += "swupd_replace_hardlinks; "

python rm_bundle_image_manifests () {
    if not d.getVar('PN_BASE', True):
        return

    manifest_link = d.expand('${DEPLOY_DIR_IMAGE}/${IMAGE_LINK_NAME}.manifest')
    if os.path.exists(manifest_link):
        os.unlink(manifest_link)
    manifest = d.getVar('IMAGE_MANIFEST', True)
    if os.path.exists(manifest):
        os.unlink(manifest)
}
do_image_complete[postfuncs] += "rm_bundle_image_manifests"
