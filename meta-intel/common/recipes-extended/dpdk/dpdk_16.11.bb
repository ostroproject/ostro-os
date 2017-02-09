include dpdk.inc

SRC_URI += "\
            file://dpdk-16.04-add-config-variable-to-enable-disable-dpdk_qat.patch \
            file://dpdk-16.04-dpdk-enable-ip_fragmentation-in-common_base-config.patch \
            "

SRC_URI[dpdk.md5sum] = "f51ffc862a4f57b0030ca5d7ff07fef0"
SRC_URI[dpdk.sha256sum] = "8098b3542b4c78d28bde5f4eba57d4ee929fffaaa941b7afd2b881eae0b45c00"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_configure_prepend () {
	sed -e "s#CONFIG_RTE_LIBRTE_POWER=y#CONFIG_RTE_LIBRTE_POWER=${CONFIG_EXAMPLE_VM_POWER_MANAGER}#" -i ${S}/config/common_linuxapp
}

COMPATIBLE_HOST_libc-musl_class-target = "null"
