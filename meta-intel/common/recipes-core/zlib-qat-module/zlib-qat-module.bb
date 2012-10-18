SUMMARY="Zlib QAT_MEM Memory Management Module for Intel Quick Assist \
Technology"
DESCRIPTION="This software acelerates the data compression algorithm \
in the zlib software library via the Intel QuickAssist Technology \
implemented on Intel Communications Chipset 89xx Series based platforms."

HOMEPAGE = "http://zlib.net/"
SECTION = "libs"
LICENSE = "Zlib & GPLv2 & BSD"

LIC_FILES_CHKSUM = "file://${WORKDIR}/zlib-${PV}/zlib.h;beginline=4;endline=23;md5=94d1b5a40dadd127f3351471727e66a9 \
			file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6 \
			file://${COMMON_LICENSE_DIR}/BSD;md5=3775480a712fc46a69647678acb234cb"
PV = "1.2.7"
ZLIB_QAT_VERSION = "0.4.0-011"

PR="r0"

SRC_URI = "http://www.zlib.net/zlib-${PV}.tar.gz;name=zlib \
	http://downloadmirror.intel.com/20294/eng/zlib-${PV}-qat.L.${ZLIB_QAT_VERSION}.tar.gz;name=zlib_qat \
	file://zlib_qat_module.patch"

SRC_URI[zlib.md5sum]="60df6a37c56e7c1366cca812414f7b85"
SRC_URI[zlib.sha256sum]="fa9c9c8638efb8cb8ef5e4dd5453e455751e1c530b1595eed466e1be9b7e26c5"

SRC_URI[zlib_qat.md5sum]="88e4140f98d2f9e170bf473f20e1a8d4"
SRC_URI[zlib_qat.sha256sum]="3c360878127f3930e64640ef5a5822719a5059143326bb4c396645ae37b704a6"

S = "${WORKDIR}/zlib-${PV}/contrib/qat/qat_mem"

inherit module
export KERNEL_SOURCE_ROOT = "${STAGING_KERNEL_DIR}"

do_patch() 	{
	cd ${WORKDIR}/zlib-${PV}
	patch -p0  < ${WORKDIR}/zlib-${PV}-qat.L.${ZLIB_QAT_VERSION}.patch

	cd ${WORKDIR}
	patch -p1   < ${WORKDIR}/zlib_qat_module.patch
}

do_compile()    {
	cd ${S}
	oe_runmake KERNEL_CC="${KERNEL_CC}"
}

do_install_append()     {
	install -m 0755 -d      		${D}${bindir}
	install -m 0755 ${S}/qat_mem_test       ${D}${bindir}
}

FILES_${PN} += "${bindir}/qat_mem_test"
