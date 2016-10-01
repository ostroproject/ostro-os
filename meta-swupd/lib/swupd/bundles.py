import subprocess
from oe.package_manager import RpmPM
from oe.package_manager import OpkgPM
from oe.package_manager import DpkgPM
from oe.utils import format_pkg_list
from oe.rootfs import image_list_installed_packages
import oe.path
import swupd.path
import swupd.utils


def create_bundle_manifest(d, bundlename, dest=None):
    """
    create a bundle subscription receipt

    swupd-client expects a bundle subscription to exist for each
    installed bundle. This is simply an empty file named for the
    bundle in /usr/share/clear/bundles

    d -- the bitbake datastore
    bundlename -- the name of the bundle [and the receipt file name]
    dest -- the effective root location in which to create the receipt
        (default IMAGE_ROOTFS)
    """
    tgtpath = '/usr/share/clear/bundles'
    if dest:
        bundledir = dest + tgtpath
    else:
        bundledir = d.expand('${IMAGE_ROOTFS}%s' % tgtpath)
    bb.utils.mkdirhier(bundledir)
    open(os.path.join(bundledir, bundlename), 'w+b').close()


def get_bundle_packages(d, bundle):
    """
    Return a list of packages included in a bundle

    d -- the bitbake datastore
    bundle -- the name of the bundle for which we return a package list
    """
    pkgs = (d.getVarFlag('BUNDLE_CONTENTS', bundle, True) or '').split()
    return pkgs


def create_content_manifest(dir, outfile, blacklist):
    """
    Iterate over the content of the directory, remove entries listed in the blacklist
    (for example, /etc/machine-id), and write the full paths of the remaining
    entries (without leading ./ or /) to the file named in outfile. All directories
    are explicitly listed.
    """
    bb.debug(3, 'Creating %s from directory %s, excluding %s' % (outfile, dir, blacklist))
    cwd = os.getcwd()
    try:
        os.chdir(dir)
        with open(outfile, 'w') as f:
            for root, dirs, files in os.walk('.'):
                for entry in dirs + files:
                    # strip the leading ./
                    fullpath = os.path.join(root, entry)[2:]
                    if not ('/' + fullpath) in blacklist:
                        f.write(fullpath + '\n')
    finally:
        os.chdir(cwd)


def copy_core_contents(d):
    """
    Determine the os-core contents and copy the mega image to swupd's image directory.

    d -- the bitbake datastore
    """
    imagedir = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}')
    corefile = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}/os-core${SWUPD_ROOTFS_MANIFEST_SUFFIX}')
    fullfile = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}/full${SWUPD_ROOTFS_MANIFEST_SUFFIX}')
    bundle = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}/full.tar')
    rootfs = d.getVar('IMAGE_ROOTFS', True)

    # Generate a manifest of the bundle content.
    bb.utils.mkdirhier(imagedir)
    unwanted_files = (d.getVar('SWUPD_FILE_BLACKLIST', True) or '').split()
    create_content_manifest(rootfs, corefile, unwanted_files)

    havebundles = (d.getVar('SWUPD_BUNDLES', True) or '') != ''
    imgrootfs = d.getVar('MEGA_IMAGE_ROOTFS', True)
    if not havebundles:
        imgrootfs = rootfs
        manifest_files = swupd.utils.manifest_to_file_list(corefile)
        with open(fullfile, 'w') as f:
            f.write('\n'.join(manifest_files))
    else:
        create_content_manifest(imgrootfs, fullfile, unwanted_files)
        manifest_files = swupd.utils.manifest_to_file_list(fullfile)

    bb.debug(1, "Copying from image (%s) to full bundle (%s)" % (imgrootfs, bundle))
    # Create full.tar.gz instead of directory - speeds up
    # do_stage_swupd_input from ~11min in the Ostro CI to 6min.
    swupd.path.copyxattrfiles(d, manifest_files, imgrootfs, bundle, True)


def stage_image_bundle_contents(d, bundle):
    """
    Determine bundle contents which aren't part of os-core from the mega-image rootfs

    For an image-based bundle, generate a list of files which exist in the
    bundle but not os-core and stage those files from the mega image rootfs to
    the swupd inputs directory

    d -- the bitbake datastore
    bundle -- the name of the bundle to be staged
    """

    # Construct paths to manifest files and directories
    pn = d.getVar('PN', True)
    manifest_path = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}/')
    base_manifest_name = d.expand('os-core${SWUPD_ROOTFS_MANIFEST_SUFFIX}')
    image_manifest_name = base_manifest_name.replace('os-core', bundle, 1)
    base_manifest = manifest_path + base_manifest_name
    image_manifest = manifest_path + image_manifest_name
    megarootfs = d.getVar('MEGA_IMAGE_ROOTFS', True)
    imagesrc = megarootfs.replace('mega', bundle)

    # Generate the manifest of the bundle image's file contents,
    # excluding blacklisted files and the content of the os-core.
    bb.debug(3, 'Writing bundle image file manifest %s' % image_manifest)
    unwanted_files = set((d.getVar('SWUPD_FILE_BLACKLIST', True) or '').split())
    unwanted_files.update(['/' + x for x in swupd.utils.manifest_to_file_list(base_manifest)])
    create_content_manifest(imagesrc, image_manifest, unwanted_files)

def stage_empty_bundle(d, bundle):
    """
    stage an empty bundle

    d -- the bitbake datastore
    bundle -- the name of the bundle to be staged
    """
    bundledir = d.expand('${SWUPDIMAGEDIR}/${OS_VERSION}/%s' % bundle)
    bb.utils.mkdirhier(bundledir)
    create_bundle_manifest(d, bundle, bundledir)


def copy_bundle_contents(d):
    """
    Stage bundle contents

    Copy the contents of all bundles from the mega image rootfs to the swupd
    inputs directory to ensure that any image postprocessing which modifies
    files is reflected in os-core bundle

    d -- the bitbake datastore
    """
    bb.debug(1, 'Copying contents of bundles for %s from mega image rootfs' % d.getVar('PN', True))
    bundles = (d.getVar('SWUPD_BUNDLES', True) or '').split()
    for bndl in bundles:
        stage_image_bundle_contents(d, bndl)
    bundles = (d.getVar('SWUPD_EMPTY_BUNDLES', True) or '').split()
    for bndl in bundles:
        stage_empty_bundle(d, bndl)
