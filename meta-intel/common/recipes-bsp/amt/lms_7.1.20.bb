DESCRIPTION = "Intel Local Manageability Service allows applications \
to access the Intel Active Management Technology (AMT) firmware via \
the Intel Management Engine Interface (MEI)."
HOMEPAGE = "http://software.intel.com/en-us/articles/download-the-latest-intel-amt-open-source-drivers"

LICENSE = "Modified BSD"

PR = "r0"
SRC_URI = "http://software.intel.com/file/37962 \
           file://atnetworktool-printf-fix.patch \
           file://readlink-declaration.patch"

COMPATIBLE_HOST = '(i.86|x86_64).*-linux'

LIC_FILES_CHKSUM = "file://COPYING;md5=7264184cf88d9f27b719a9656255b47b"

SRC_URI[md5sum] = "687b76e78bfdbcf567c0e842c1fe240a"
SRC_URI[sha256sum] = "cc0457f0044e924794bb1aeae9a72c28666a525cd8a963d0d92970222946e75b"

inherit autotools update-rc.d

INITSCRIPT_NAME = "lms"
INITSCRIPT_PARAMS = "defaults"

PV_SUB = "25"

do_unpack2() {
	# The downloaded 37962 filename is actually lms+7.1.20.25.zip.
	# It contains lms-7.1.20-25.tar.gz.
	# It contains lms-7.1.20-25.tar.gz untars to lms-7.1.20
	if [ -e "${WORKDIR}/37962" ]; then
		mv ${WORKDIR}/37962 ${WORKDIR}/${PN}+${PV}.${PV_SUB}.zip
		unzip -o ${WORKDIR}/${PN}+${PV}.${PV_SUB}.zip
		mv ${WORKDIR}/${PN}-${PV}/outputdir/${PN}-${PV}-${PV_SUB}.tar.gz ${WORKDIR}/
		cd ${WORKDIR}
		tar -xvzf ${PN}-${PV}-${PV_SUB}.tar.gz
	fi
}

addtask unpack2 after do_unpack before do_patch

do_install_append () {
	install -d ${D}${sysconfdir}/init.d
	install -m 0755 ${WORKDIR}/${PN}-${PV}/scripts/lms ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
}
