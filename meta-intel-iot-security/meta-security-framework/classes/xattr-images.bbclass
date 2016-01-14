# Both Smack and IMA/EVM rely on xattrs. Inheriting this class ensures
# that these xattrs get preserved in tar and jffs2 images.
#
# It also fixes the rootfs so that the content of directories with
# SMACK::TRANSMUTE is correctly labelled. This is because pseudo does
# not know the special semantic of SMACK::TRANSMUTE and omits the
# updating of the Smack label when creating entries inside such a directory,
# for example /etc (see base-files_%.bbappend). Without the fixup,
# files already installed during the image creation would have different (and
# wrong) Smack labels.

# xattr support is expected to be compiled into mtd-utils. We just need to
# use it.
EXTRA_IMAGECMD_jffs2_append = " --with-xattr"

# By default, OE-core uses tar from the host, which may or may not have the
# --xattrs parameter which was introduced in 1.27. For image building we
# use a recent enough tar instead.
#
# The GNU documentation does not specify whether --xattrs-include is necessary.
# In practice, it turned out to be not needed when creating archives and
# required when extracting, but it seems prudent to use it in both cases.
IMAGE_DEPENDS_tar_append = " tar-replacement-native"
EXTRANATIVEPATH += "tar-native"
IMAGE_CMD_TAR = "tar --xattrs --xattrs-include=*"

xattr_images_fix_transmute () {
    set -e
    cd ${IMAGE_ROOTFS}

    # The recursive updating of the Smack label ensures that each entry
    # has the label set for its parent directories if one of those was
    # marked as transmuting.
    #
    # In addition, "-" is set explicitly on everything that would not
    # have a label otherwise. This is a workaround for tools like swupd
    # which transfers files from a rootfs onto a target device where Smack
    # is active: on the target, each file gets assigned a label, typically
    # the one from the process which creates it. swupd (or rather, the tools
    # it is currently built on) knows how to set security.SMACK64="_" when
    # it is set on the original files, but it does not know that it needs
    # to remove that xattr when not set.
    python <<EOF
import xattr
import os
import errno

def lgetxattr(f, attr, default=None):
    try:
        value = xattr.getxattr(f, attr, symlink=True)
    except IOError, ex:
        if ex.errno == errno.ENODATA and default is not None:
            value = default
        else:
            raise
    return value

def lsetxattr(f, attr, value):
    xattr.setxattr(f, attr, value, symlink=True)

def visit(path, deflabel, deftransmute):
    isrealdir = os.path.isdir(path) and not os.path.islink(path)
    curlabel = lgetxattr(path, 'security.SMACK64', '')
    transmute = lgetxattr(path, 'security.SMACK64TRANSMUTE', '') == 'TRUE'

    # We don't want to set the floor label explicitly. It is the default label
    # and thus adding it would create additional overhead, and mkfs.ext4 has
    # problems when files have multiple xattrs (https://bugzilla.yoctoproject.org/show_bug.cgi?id=8992).
    # That may also occur without the explicit '_' label, but setting it
    # triggers that problem reliably.
    if not curlabel:
        if deflabel != '_':
            lsetxattr(path, 'security.SMACK64', deflabel)
        if not transmute and deftransmute and isrealdir:
            lsetxattr(path, 'security.SMACK64TRANSMUTE', 'TRUE')

    # Identify transmuting directories and change the default Smack
    # label inside them. In addition, directories themselves must become
    # transmuting.
    if isrealdir:
        if transmute:
            deflabel = lgetxattr(path, 'security.SMACK64')
            deftransmute = True
            if deflabel is None:
                raise RuntimeError('%s: transmuting directory without Smack label' % path)
        elif curlabel:
            # Directory with explicit label set and not transmuting => do not
            # change the content unless we run into another transmuting directory.
           deflabel = '_'
           deftransmute = False

        for entry in os.listdir(path):
            visit(os.path.join(path, entry), deflabel, deftransmute)

visit('.', '_', False)
EOF
}
# Same logic as in ima-evm-rootfs.bbclass: try to run as late as possible.
IMAGE_PREPROCESS_COMMAND_append_smack = " xattr_images_fix_transmute ; "