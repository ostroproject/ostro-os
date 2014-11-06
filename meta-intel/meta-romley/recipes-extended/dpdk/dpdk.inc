DESCRIPTION = "Intel(r) Data Plane Development Kit"
HOMEPAGE = "http://dpdk.org"
LICENSE = "BSD & LGPLv2 & GPLv2"
LIC_FILES_CHKSUM = "file://LICENSE.GPL;md5=751419260aa954499f7abaabaa882bbe"

COMPATIBLE_MACHINE = "romley|romley-ivb"

RDEPENDS_${PN} += "python-subprocess"

inherit module

export MODULE_DIR="/lib/modules/${KERNEL_VERSION}/kernel/drivers/net"
export RTE_SDK = "${S}"
export RTE_TARGET="${TARGET_ARCH}-ivshmem-${TARGET_OS}app-gcc"
export ICP_ROOT = "${PKG_CONFIG_SYSROOT_DIR}/usr/include"
export ICP_LIB_ROOT= "${PKG_CONFIG_SYSROOT_DIR}/usr/lib"
export RTE_KERNELDIR = "${STAGING_KERNEL_DIR}"
export INSTALL_PATH = "${prefix}/dpdk"


do_configure () {
	#############################################################
	### default value for prefix is "usr", unsetting it, so it
	### will not be concatenated in ${RTE_TARGET}/Makefile
	### which will cause compilation failure
	#############################################################
	unset prefix

	make O=$RTE_TARGET T=$RTE_TARGET config

}


do_compile () {
	unset LDFLAGS TARGET_LDFLAGS BUILD_LDFLAGS

	cd ${S}/${RTE_TARGET}
	oe_runmake EXTRA_LDFLAGS=" --sysroot=${STAGING_DIR_HOST}" \
		   EXTRA_CFLAGS=" --sysroot=${STAGING_DIR_HOST}" \
		   CROSS="${TARGET_PREFIX}" \
		   prefix=""  LDFLAGS=""  WERROR_FLAGS="-w" V=1

}


do_install () {

	install -m 0755 -d	${D}/${INSTALL_PATH} \
				${D}/${INSTALL_PATH}/doc \
				${D}/${INSTALL_PATH}/tools \
				${D}/${INSTALL_PATH}/${RTE_TARGET} \
				${D}/${INSTALL_PATH}/${RTE_TARGET}/app \
				${D}${includedir} \
				${D}${includedir}/arch \
				${D}${includedir}/exec-env \
				${D}${libdir} \
				${D}${MODULE_DIR}

	install -m 0755 ${S}/${RTE_TARGET}/kmod/igb_uio.ko	${D}${MODULE_DIR}/
	install -m 0755 ${S}/${RTE_TARGET}/kmod/rte_kni.ko	${D}${MODULE_DIR}/

	install -m 640 ${S}/${RTE_TARGET}/lib/*.a		${D}${libdir}

	install -m 640 ${S}/${RTE_TARGET}/.config			${D}/${INSTALL_PATH}/${RTE_TARGET}/
	install -m 640 ${S}/${RTE_TARGET}/include/*.h			${D}${includedir}/
	install -m 640 ${S}/${RTE_TARGET}/include/arch/*		${D}${includedir}/arch/
	install -m 640 ${S}/${RTE_TARGET}/include/exec-env/*		${D}${includedir}/exec-env/
	install -m 0755 ${S}/tools/*.py					${D}/${INSTALL_PATH}/tools/


	#Install test applications
	install -m 0755 ${S}/${RTE_TARGET}/app/test	${D}/${INSTALL_PATH}/${RTE_TARGET}/app
	install -m 0755 ${S}/${RTE_TARGET}/app/testpmd	${D}/${INSTALL_PATH}/${RTE_TARGET}/app
	install -m 0755 ${S}/${RTE_TARGET}/app/dump_cfg	${D}/${INSTALL_PATH}/${RTE_TARGET}/app
	install -m 0755 ${S}/${RTE_TARGET}/app/cmdline_test	${D}/${INSTALL_PATH}/${RTE_TARGET}/app


	# Install example applications
	# It is expected that user of this include file should define EXAMPLES_BUILD_DIR
	for app in ${S}/examples/*
	do
		case `basename ${app}` in
		"dpdk_qat" | "vhost" | "vhost_xen" | "Makefile" ) continue
		;;
		"l2fwd-ivshmem")
		install -m 0755 ${app}/guest/${EXAMPLES_BUILD_DIR}/app/guest		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		install -m 0755 ${app}/host/${EXAMPLES_BUILD_DIR}/app/host		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		"multi_process")
		install -m 0755 ${app}/client_server_mp/mp_client/${EXAMPLES_BUILD_DIR}/app/mp_client	${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		install -m 0755 ${app}/client_server_mp/mp_server/${EXAMPLES_BUILD_DIR}/app/mp_server	${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		install -m 0755 ${app}/simple_mp/${EXAMPLES_BUILD_DIR}/app/simple_mp			${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		install -m 0755 ${app}/symmetric_mp/${EXAMPLES_BUILD_DIR}/app/symmetric_mp		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		"netmap_compat")
		install -m 0755 ${app}/bridge/${EXAMPLES_BUILD_DIR}/app/bridge			${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		"quota_watermark")
		install -m 0755 ${app}/qw/${EXAMPLES_BUILD_DIR}/app/qw			${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		install -m 0755 ${app}/qwctl/${EXAMPLES_BUILD_DIR}/app/qwctl		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		"vmdq")
		install -m 0755 ${app}/${EXAMPLES_BUILD_DIR}/app/`basename ${app}`_app		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		"vmdq_dcb")
		install -m 0755 ${app}/${EXAMPLES_BUILD_DIR}/app/`basename ${app}`_app		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
		continue
		;;
		esac

		install -m 0755 ${app}/${EXAMPLES_BUILD_DIR}/app/`basename ${app}`		${D}/${INSTALL_PATH}/${RTE_TARGET}/app
	done
}

PACKAGES += "${PN}-examples"

FILES_${PN}-dbg += " \
	${INSTALL_PATH}/.debug \
	${INSTALL_PATH}/${RTE_TARGET}/app/.debug \
	"

FILES_${PN}-doc += "\
	${INSTALL_PATH}/doc \
	"

FILES_${PN}-dev += " \
	${INSTALL_PATH}/${RTE_TARGET}/.config \
	${includedir} \
	${includedir}/arch \
	${includedir}/exec-env \
	"

FILES_${PN} +=  " ${INSTALL_PATH}/tools/ "

FILES_${PN}-examples += " ${INSTALL_PATH}/${RTE_TARGET}/app/ "
