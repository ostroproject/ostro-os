DESCRIPTION = "Intel(r) Data Plane Development Kit"
HOMEPAGE = "http://dpdk.org"
LICENSE = "BSD & LGPLv2 & GPLv2"
LIC_FILES_CHKSUM = "file://LICENSE.GPL;md5=751419260aa954499f7abaabaa882bbe"

RDEPENDS_${PN} += "python-subprocess"

inherit module

export MODULE_DIR="/lib/modules/${KERNEL_VERSION}/kernel/drivers/net"
export RTE_SDK = "${S}"
export RTE_TARGET="${@bb.utils.contains("TUNE_FEATURES", "corei7", "x86_64-ivshmem-linuxapp-gcc", "i686-native-linuxapp-gcc", d)}"

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
				${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp \
				${D}${includedir} \
				${D}${includedir}/arch \
				${D}${includedir}/exec-env \
				${D}${libdir} \
				${D}${MODULE_DIR}

	install -m 0755 ${S}/${RTE_TARGET}/kmod/*.ko	${D}${MODULE_DIR}/

	install -m 640 ${S}/${RTE_TARGET}/lib/*.a		${D}${libdir}

	install -m 640 ${S}/${RTE_TARGET}/.config			${D}/${INSTALL_PATH}/${RTE_TARGET}/
	install -m 640 ${S}/${RTE_TARGET}/include/*.h			${D}${includedir}/
	install -m 640 ${S}/${RTE_TARGET}/include/arch/*.h		${D}${includedir}/arch/
	install -m 640 ${S}/${RTE_TARGET}/include/exec-env/*.h		${D}${includedir}/exec-env/
	install -m 0755 ${S}/tools/*.py					${D}/${INSTALL_PATH}/tools/

	# Install applications
	install -m 0755 ${S}/${RTE_TARGET}/app/*	${D}/${INSTALL_PATH}/${RTE_TARGET}/app/
	install -m 0755 ${S}/${RTE_TARGET}/hostapp/*	${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp/

	# Install examples
	for dirname in ${S}/examples/*
	do
		install -m 0755 -d ${D}/${INSTALL_PATH}/examples/`basename ${dirname}`

		for appname in `find ${dirname} -regex ".*${EXAMPLES_BUILD_DIR}\/app\/[-0-9a-zA-Z0-9/_]*$"`
		do
			install -m 755 ${appname}	${D}/${INSTALL_PATH}/examples/`basename ${dirname}`/
		done
	done
}

PACKAGES += "${PN}-examples"

FILES_${PN}-dbg += " \
	${INSTALL_PATH}/.debug \
	${INSTALL_PATH}/${RTE_TARGET}/app/.debug \
	${INSTALL_PATH}/${RTE_TARGET}/hostapp/.debug \
	${INSTALL_PATH}/${RTE_TARGET}/app/*.map \
	${INSTALL_PATH}/examples/*/.debug \
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

FILES_${PN} += " ${INSTALL_PATH}/tools/ "

FILES_${PN}-examples += " \
	${INSTALL_PATH}/${RTE_TARGET}/app/* \
	${INSTALL_PATH}/${RTE_TARGET}/hostapp/* \
	${INSTALL_PATH}/examples/* \
	"
