PROVIDES_append = " ${JDKPN}-jdk"

OPENJDK_OECONF = " \
     --openjdk-target=${TARGET_SYS} \
     --prefix=/usr                  \
     --exec_prefix=/usr             \
     --bindir=/usr/bin              \
     --sbindir=/usr/sbin            \
     --libexecdir=/usr/libexec      \
     --datadir=/usr/share           \
     --sysconfdir=/etc              \
     --sharedstatedir=/com          \
     --localstatedir=/var           \
     --libdir=/usr/lib              \
     --includedir=/usr/include      \
     --oldincludedir=/usr/include   \
     --infodir=/usr/share/info      \
     --mandir=/usr/share/man        \
     --disable-headful              \
     --with-sys-root=${STAGING_DIR_TARGET} \
     --with-boot-jdk=${STAGING_LIBDIR_JVM_NATIVE}/icedtea7-native \
     CFLAGS="--sysroot=${STAGING_DIR_TARGET} " \
     CXXFLAGS="--sysroot=${STAGING_DIR_TARGET} " \
     LDFLAGS="--sysroot=${STAGING_DIR_TARGET} " \
     --with-extra-cflags="--sysroot=${STAGING_DIR_TARGET} ${SELECTED_OPTIMIZATION}" \
     --with-extra-cxxflags="--sysroot=${STAGING_DIR_TARGET} " \
     --with-extra-ldflags="--sysroot=${STAGING_DIR_TARGET} " \
     "

