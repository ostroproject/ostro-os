DESCRIPTION = "Intel Local Manageability Service allows applications \
to access the Intel Active Management Technology (AMT) firmware via \
the Intel Management Engine Interface (MEI)."
HOMEPAGE = "http://software.intel.com/en-us/articles/download-the-latest-intel-amt-open-source-drivers"

LICENSE = "BSD_LMS"

PR = "r0"
BPN="lms"
PV_SUB = "25"
SRC_URI = "http://software.intel.com/file/37962;downloadfilename=${BPN}+${PV}.${PV_SUB}.zip \
           file://atnetworktool-printf-fix.patch \
           file://readlink-declaration.patch"

COMPATIBLE_HOST = '(i.86|x86_64).*-linux'

LIC_FILES_CHKSUM = "file://COPYING;md5=7264184cf88d9f27b719a9656255b47b"

SRC_URI[md5sum] = "687b76e78bfdbcf567c0e842c1fe240a"
SRC_URI[sha256sum] = "cc0457f0044e924794bb1aeae9a72c28666a525cd8a963d0d92970222946e75b"

inherit autotools update-rc.d

INITSCRIPT_NAME = "lms7"
INITSCRIPT_PARAMS = "defaults"

do_unpack2() {
	cd ${WORKDIR}
	tar -xvzf ${WORKDIR}/outputdir/lms-${PV}-${PV_SUB}.tar.gz
}

addtask unpack2 after do_unpack before do_patch

do_install_append () {
	mv ${D}/${sbindir}/lms ${D}/${sbindir}/lms7
	install -d ${D}${sysconfdir}/init.d
	mv ${D}${sysconfdir}/rc.d/init.d/lms ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
	sed -i 's/^NAME=lms/NAME=lms7/' ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
	rmdir ${D}${datadir} || :
}
