SUMMARY = "libcrypto* (OpenSSL*) QAT_MEM Memory Management Module \
for Intel Quick Assist Technology"
DESCRIPTION = "This software adds an engine that accelerates some of \
the libcrypto algorithms via the Intel QuickAssist Technology \
implemented on Intel Communications Chipset 89xx Series based platforms."

HOMEPAGE = "http://www.openssl.org/"
SECTION = "libs/network"

LICENSE = "openssl & GPLv2 & BSD"
LIC_FILES_CHKSUM = "file://${WORKDIR}/openssl-${PV}/LICENSE;md5=f9a8f968107345e0b75aa8c2ecaa7ec8 \
			file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6 \
			file://${COMMON_LICENSE_DIR}/BSD;md5=3775480a712fc46a69647678acb234cb"

PV = "1.0.1"
PR = "r0"

OPENSSL_QAT_VERSION = "0.4.0-012"

SRC_URI = "http://www.openssl.org/source/openssl-${PV}.tar.gz;name=openssl \
	http://downloadmirror.intel.com/19368/eng/libcrypto-openssl-${PV}-qat.L.${OPENSSL_QAT_VERSION}.tar.gz;name=libcrypto \
	file://openssl_qat_module.patch"

SRC_URI[openssl.md5sum]="134f168bc2a8333f19f81d684841710b"
SRC_URI[openssl.sha256sum]="4d9f0a594a9a89b28e1a04a9504c04104f6508ee27ad1e0efdd17a7a6dbbeeee"

SRC_URI[libcrypto.md5sum] = "e4e131fa56d3aa1a52b5bdb9f8fe5a69"
SRC_URI[libcrypto.sha256sum] = "19a80ae6e78548934295d312148e4254c18dabd25e2fd72de5796d8ac15b1cfb"

COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"

S = "${WORKDIR}/openssl-${PV}/engines/qat_engine/qat_mem"

export KERNEL_SOURCE_ROOT = "${STAGING_KERNEL_DIR}"
inherit module

do_patch()     {
	cd ${WORKDIR}/openssl-${PV}
	patch -p2 < ${WORKDIR}/libcrypto-openssl-${PV}-qat.L.${OPENSSL_QAT_VERSION}.patch

	cd ${WORKDIR}
	patch -p1 <${WORKDIR}/openssl_qat_module.patch
}

do_compile() 	{
	cd ${S}
	oe_runmake  KERNEL_CC="${KERNEL_CC}"
}

do_install_append() 	{
	install -m 0755 -d ${D}${bindir} \
			   ${D}${includedir}/engines/qat_engine/qat_mem

	install -m 0755 ${S}/qat_mem_test  ${D}${bindir}
	install -m 0750 ${S}/*.h	   ${D}${includedir}/engines/qat_engine/qat_mem/
}

FILES_${PN} += "${bindir}/qat_mem_test"
