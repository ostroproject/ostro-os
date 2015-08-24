# Both Smack and IMA/EVM rely on xattrs. Inheriting this class ensures
# that these xattrs get preserved in tar and jffs2 images.

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
