SUMMARY = "Zlib QAT_MEM Memory Management Module for Intel Quick Assist \
Technology"

DESCRIPTION = "This software acelerates the data compression algorithm \
in the zlib software library via the Intel QuickAssist Technology \
implemented on Intel Communications Chipset 89xx and 895x Series based platforms."

HOMEPAGE = "http://zlib.net/"
SECTION = "libs"
LICENSE = "Zlib & GPLv2 & BSD"
LIC_FILES_CHKSUM = "file://${WORKDIR}/zlib-${ZLIB_VERSION}/zlib.h;beginline=4;endline=23;md5=fde612df1e5933c428b73844a0c494fd \
		    file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6 \
		    file://${COMMON_LICENSE_DIR}/BSD;md5=3775480a712fc46a69647678acb234cb"

# For target side versions of openssl enable support for OCF Linux driver
# if they are available.
DEPENDS += "cryptodev-linux pkgconfig qat16"

SRC_URI = "http://www.zlib.net/zlib-${ZLIB_VERSION}.tar.gz;name=zlib \
           https://01.org/sites/default/files/page/zlib_shim_0.4.7-002_withdocumentation.zip;name=zlibqat \
           file://zlib-qat-0.4.7-002-qat_mem-build-qat_mem-ko-against-yocto-kernel-src.patch \
           "

SRC_URI[zlib.md5sum] = "44d667c142d7cda120332623eab69f40"
SRC_URI[zlib.sha256sum] = "36658cb768a54c1d4dec43c3116c27ed893e88b02ecfcb44f2166f9c0b7f2a0d"

SRC_URI[zlibqat.md5sum] = "dfde8618198aa8d35ecc00d10dcc7000"
SRC_URI[zlibqat.sha256sum] = "8e5786400bbc2a879ae705c864ec63b53ae019b4f2d1c94524a97223847b6e46"

ZLIB_VERSION = "1.2.8"
ZLIB_QAT_VERSION = "0.4.7-002"

S = "${WORKDIR}/zlib-${ZLIB_VERSION}"

export ICP_ROOT = "${PKG_CONFIG_SYSROOT_DIR}"
export ZLIB_ROOT = "${S}"
export ICP_ZLIBQAT = "${S}"
export ICP_BUILD_OUTPUT = "${ICP_ROOT}/lib"
export KERNEL_SOURCE_ROOT = "${STAGING_KERNEL_DIR}"
export KERNEL_BUILDDIR = "${STAGING_KERNEL_BUILDDIR}"

CFLAGS += "\
		-I${ICP_ROOT}/usr/include \
		-I${ICP_ROOT}/usr/include/dc \
		-I${ZLIB_ROOT}/ \
		-D_LARGEFILE64_SOURCE=1 -DHAVE_HIDDEN -DUSE_QAT_MEM -I${ZLIB_ROOT}/contrib/qat/qat_mem -D_GNU_SOURCE \
		-L${ZLIB_ROOT} -lz \
		-L${ICP_ROOT}/usr/lib/ -lpthread -lcrypto -ldl -lrt \
		-L${ICP_ROOT}/usr/lib/ -licp_qa_al -losal -ladf_proxy"

inherit module
MODULE_DIR = "${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers"
MEM_PATH = "${S}/contrib/qat"

do_unpack2(){
	cd ${WORKDIR}/
	unzip zlib_quickassist_patch_l.0.4.7_002_stable.zip
	cd zlib_quickassist_patch_l.0.4.7_002_devbranch
	tar -xvzf zlib-1.2.8-qat.L.0.4.7-002.tar.gz
	cp zlib-1.2.8-qat.patch ${WORKDIR}
}

addtask unpack2 after do_unpack before do_patch

do_patch() {
	cd ${S}
	patch -p1  < ${WORKDIR}/zlib-1.2.8-qat.patch
	patch -p1  < ${WORKDIR}/zlib-qat-0.4.7-002-qat_mem-build-qat_mem-ko-against-yocto-kernel-src.patch
}

do_configure() {
	cd ${S}
	./configure
}

do_compile() {
	EXTRA_OEMAKE="'CFLAGS=${CFLAGS} -fPIC'"
	cd ${MEM_PATH}/qat_mem/
	oe_runmake
	cd ${S}/
	oe_runmake
	cd ${MEM_PATH}/qat_zlib_test/
	oe_runmake
}

do_install() {
	chrpath -d ${MEM_PATH}/qat_zlib_test/comptestapp
	install -m 0755 -d		${MODULE_DIR}/
	install -m 0755 -d		${D}${bindir}/
	install -m 0755 -d		${D}${sysconfdir}/zlib_conf/
	install -m 640  ${MEM_PATH}/qat_mem/qat_mem.ko		${MODULE_DIR}/
	install -m 0755 ${WORKDIR}/zlib-${ZLIB_VERSION}/zpipe		${D}${bindir}/
	install -m 0755 ${WORKDIR}/zlib-${ZLIB_VERSION}/minigzip	${D}${bindir}/
	install -m 0755 ${MEM_PATH}/qat_zlib_test/comptestapp		${D}${bindir}/
	install -m 660  ${MEM_PATH}/config/dh895xcc/multi_thread_optimized/*	${D}${sysconfdir}/zlib_conf/
	install -m 660  ${MEM_PATH}/config/dh89xxcc/multi_thread_optimized/*	${D}${sysconfdir}/zlib_conf/
}

PACKAGES += "${PN}-app"

FILES_${PN} += " \
		${sysconfdir}/zlib_conf/ \
		"

FILES_${PN}-app += " \
		${bindir}/* \
	"

FILES_${PN}-dbg += " \
		${bindir}/.debug \
		"
