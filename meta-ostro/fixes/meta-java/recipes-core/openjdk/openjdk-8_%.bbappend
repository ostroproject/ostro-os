# 'int readdir_r(DIR*, dirent*, dirent**)' is deprecated
#
# Reported to meta-java maintainers via the openembedded-devel
# mailing list as "[meta-java] openjdk/jre-8: readdir_r deprecated".
CFLAGS_append = "-Wno-error=deprecated-declarations"
