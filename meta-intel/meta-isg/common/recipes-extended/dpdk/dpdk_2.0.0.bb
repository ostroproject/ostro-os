include dpdk.inc

SRC_URI += "file://dpdk-2.0.0-dpdk-enable-ip_fragmentation-in-common_linuxapp.patch \
            file://dpdk-1.8.0-and-2.0.0-examples-add-config-variable-to-enable-disable-dpdk.patch \
            file://dpdk-1.8.0-and-2.0.0-ixgbe-fix-a-build-warning-being-treated-as-error.patch \
            file://dpdk-2.0.0-kni-fix-build-with-kernel-4.0.patch \
            file://dpdk-2.0.0-kni-fix-igb-build-with-kernel-4.1.patch \
            file://dpdk-2.0.0-kni-net-fix-build-with-kernel-4.1.patch \
            file://dpdk-2.0.0-kni-fix-vhost-build-with-kernels-3.19-and-4.0.patch \
            file://dpdk-2.0.0-kni-fix-vhost-build-with-kernel-4.1.patch \
            "

SRC_URI[dpdk.md5sum] = "e9e7935c9eec920841ad373949514934"
SRC_URI[dpdk.sha256sum] = "643789a3be5ba44dd84d6b248cdf5471b260f8736dada177dadf076aebfbff3f"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"
