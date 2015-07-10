include dpdk.inc

SRC_URI = "http://dpdk.org/browse/dpdk/snapshot/dpdk-${PV}.tar.gz;name=dpdk \
	   file://dpdk-2.0.0-dpdk-enable-VHOST-and-ip_fragmentation-in-common_linuxapp.patch \
	   file://dpdk-1.8.0-and-2.0.0-examples-add-config-variable-to-enable-disable-dpdk.patch \
	   file://dpdk-1.8.0-and-2.0.0-add-RTE_KERNELDIR_OUT-to-split-kernel-bu.patch \
	   file://dpdk-1.8.0-and-2.0.0-add-sysroot-option-within-app-makefile.patch \
	   file://dpdk-1.8.0-and-2.0.0-dpdk-defconfig-select-RTE_MACHINE-type.patch \
	   "

SRC_URI[dpdk.md5sum] = "e9e7935c9eec920841ad373949514934"
SRC_URI[dpdk.sha256sum] = "643789a3be5ba44dd84d6b248cdf5471b260f8736dada177dadf076aebfbff3f"

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
