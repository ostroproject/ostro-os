include dpdk.inc

SRC_URI = "http://dpdk.org/browse/dpdk/snapshot/dpdk-${PV}.tar.gz;name=dpdk \
	   file://dpdk-1.8.0-dpdk-enable-build-config-VHOST-in-common_linuxapp-config.patch \
	   file://dpdk-1.8.0-and-2.0.0-examples-add-config-variable-to-enable-disable-dpdk.patch \
	   file://dpdk-1.8.0-and-2.0.0-add-RTE_KERNELDIR_OUT-to-split-kernel-bu.patch \
	   file://dpdk-1.8.0-and-2.0.0-add-sysroot-option-within-app-makefile.patch \
	   file://dpdk-1.8.0-and-2.0.0-dpdk-defconfig-select-RTE_MACHINE-type.patch \
	   "

SRC_URI[dpdk.md5sum] = "11ad8785aaa869cc87265bcb8d828f22"
SRC_URI[dpdk.sha256sum] = "9f5386830bd999355182e20408f3fc2cfa0802a4497fdded8d43202feede1939"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

# dpdk example apps dpdk_qat and vhost have dependancy on fuse and qat.
# fuse is in meta-filesystems and qat is not yet upstreamed.
# So adding mechanism to explicitly disable the use of fuse and qat.
# To enable, uncomment the below line or include in .bbappend.
# PACKAGECONFIG ?= " dpdk_qat vhost libvirt"

PACKAGECONFIG[dpdk_qat] = ",,qat"
PACKAGECONFIG[vhost] = ",,fuse"
PACKAGECONFIG[libvirt] = ",,libvirt"

export CONFIG_EXAMPLE_DPDK_QAT = "${@base_contains('PACKAGECONFIG', 'dpdk_qat', 'y', 'n', d)}"
export CONFIG_EXAMPLE_VM_POWER_MANAGER = "${@base_contains('PACKAGECONFIG', 'libvirt', 'y', 'n', d)}"
export CONFIG_VHOST_ENABLED = "${@base_contains('PACKAGECONFIG', 'vhost', 'y', 'n', d)}"

do_install_append () {

	install -m 0755 -d ${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp
	install -m 0755 ${S}/${RTE_TARGET}/hostapp/*	${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp/
}
