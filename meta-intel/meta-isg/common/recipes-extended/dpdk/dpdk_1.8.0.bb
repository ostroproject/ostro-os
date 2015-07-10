include dpdk.inc

SRC_URI = "http://dpdk.org/browse/dpdk/snapshot/dpdk-${PV}.tar.gz;name=dpdk \
	   file://dpdk-1.8.0-examples-add-config-variable-to-enable-disable-dpdk_.patch \
	   file://dpdk-1.8.0-dpdk-enable-build-config-VHOST-in-common_linuxapp-config.patch \
	   file://dpdk-1.8.0-add-RTE_KERNELDIR_OUT-to-split-kernel-bu.patch \
	   file://dpdk-1.8.0-add-sysroot-option-within-app-makefile.patch \
	   file://dpdk-1.8.0-dpdk-defconfig-select-RTE_MACHINE-type.patch \
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

# The list of intel Comms platforms and their target machine
# process mapping. The supported target machine is listed under
# dpdk/mk/machine
def get_dpdk_target_mach(bb, d):
    target_arch = d.getVar('MACHINE_ARCH', True)
    multiarch_options = {
        "mohonpeak64":    "atm",
        "mohonpeak32":    "atm",
        "crystalforest":  "ivb",
        "romley":         "snd",
        "romley-ivb":     "ivb",
    }

    if target_arch in multiarch_options :
            return multiarch_options[target_arch]
    return ""

export CONFIG_EXAMPLE_DPDK_QAT = "${@base_contains('PACKAGECONFIG', 'dpdk_qat', 'y', 'n', d)}"
export CONFIG_EXAMPLE_VM_POWER_MANAGER = "${@base_contains('PACKAGECONFIG', 'libvirt', 'y', 'n', d)}"
export CONFIG_VHOST_ENABLED = "${@base_contains('PACKAGECONFIG', 'vhost', 'y', 'n', d)}"
export SYSROOTPATH = "--sysroot=${STAGING_DIR_HOST}"
export DPDK_TARGET_MACH = "${@get_dpdk_target_mach(bb,d)}"

do_compile_append () {

	cd ${S}/examples/

	###############################################################
	# In order to make use of dpdk.inc for example app installation
	# without failure, override the default build directory
	###############################################################
	oe_runmake EXTRA_LDFLAGS="-L${STAGING_LIBDIR}" \
		   EXTRA_CFLAGS="--sysroot=${STAGING_DIR_HOST} -I${STAGING_INCDIR}" \
		   CROSS="${TARGET_PREFIX}" O="${S}/examples/$@/"
}
