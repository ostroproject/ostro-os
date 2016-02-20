DESCRIPTION = "DB Utility"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=3504d672db73bec8465bdb67542a50b5;beginline=3"

DEPENDS = " \
dlog \
glib-2.0 \
icu \
sqlite3 \
"

inherit cmake

EXTRA_OECMAKE += " \
-DCMAKE_VERBOSE_MAKEFILE=ON \
-DINCLUDE_INSTALL_DIR:PATH=${includedir} \
-DLIB_INSTALL_DIR:PATH=${libdir} \
-DSYSCONF_INSTALL_DIR:PATH=${sysconfdir} \
"
