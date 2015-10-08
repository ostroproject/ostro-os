include dpdk.inc

SRC_URI += "file://dpdk-1.8.0-and-2.0.0-examples-add-config-variable-to-enable-disable-dpdk.patch \
            file://dpdk-1.8.0-and-2.0.0-ixgbe-fix-a-build-warning-being-treated-as-error.patch \
            file://dpdk-1.8.0-kni-fix-build-with-kernel-3.19.patch \
            file://dpdk-2.0.0-kni-fix-build-with-kernel-4.0.patch \
            file://dpdk-2.0.0-kni-fix-igb-build-with-kernel-4.1.patch \
            file://dpdk-2.0.0-kni-net-fix-build-with-kernel-4.1.patch \
            file://dpdk-1.8.0-mk-rework-gcc-version-detection-to-permit-versions-n.patch \
            "

SRC_URI[dpdk.md5sum] = "11ad8785aaa869cc87265bcb8d828f22"
SRC_URI[dpdk.sha256sum] = "9f5386830bd999355182e20408f3fc2cfa0802a4497fdded8d43202feede1939"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_install_append () {

	install -m 0755 -d ${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp
	install -m 0755 ${S}/${RTE_TARGET}/hostapp/*	${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp/
}
