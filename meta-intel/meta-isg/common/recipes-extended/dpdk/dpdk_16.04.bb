include dpdk.inc

SRC_URI += "\
            file://dpdk-16.04-add-config-variable-to-enable-disable-dpdk_qat.patch \
            file://dpdk-16.04-dpdk-enable-ip_fragmentation-in-common_base-config.patch \
            "

SRC_URI[dpdk.md5sum] = "0728d506d7f56eb64233e824fa3c098a"
SRC_URI[dpdk.sha256sum] = "d631495bc6e8d4c4aec72999ac03c3ce213bb996cb88f3bf14bb980dad1d3f7b"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_configure_prepend () {
	sed -e "s#CONFIG_RTE_LIBRTE_POWER=y#CONFIG_RTE_LIBRTE_POWER=${CONFIG_EXAMPLE_VM_POWER_MANAGER}#" -i ${S}/config/common_linuxapp
}
