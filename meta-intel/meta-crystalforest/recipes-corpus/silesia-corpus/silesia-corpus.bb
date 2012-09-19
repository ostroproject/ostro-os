SUMMARY = "The Data Compression Resource on the Internet"
DESCRIPTION = "The intention of the Silesia corpus is to provide a data set of files \
		that covers the typical data types used nowadays. \
		The sizes of the files are between 6 MB and 51 MB."

HOMEPAGE = "http://www.data-compression.info/index.htm"
SECTION = "misc"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"

PR="r0"

S = "${WORKDIR}/silesia-corpus"

SRC_URI = "http://sun.aei.polsl.pl/~sdeor/corpus/silesia.zip"

SRC_URI[md5sum] = "c240c17d6805fb8a0bde763f1b94cd99"
SRC_URI[sha256sum] = "0626e25f45c0ffb5dc801f13b7c82a3b75743ba07e3a71835a41e3d9f63c77af"

do_unpack () {
	mkdir -p ${S}
	cp ${DL_DIR}/silesia.zip ${S}
	cd ${S} && unzip silesia.zip
}

do_install () {

	install -d 			${D}${base_libdir}/firmware
	install -m 664 ${S}/* 		${D}${base_libdir}/firmware
}

FILES_${PN} = "/lib/firmware/*"
