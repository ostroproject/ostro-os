include dpdk.inc

SRC_URI += "\
            file://dpdk-2.1.0-add-config-variable-to-enable-disable-dpdk_qat.patch \
            file://dpdk-2.0.0-dpdk-enable-ip_fragmentation-in-common_linuxapp.patch \
            "

SRC_URI[dpdk.md5sum] = "205a0d12bfd6eb717d57506272f43519"
SRC_URI[dpdk.sha256sum] = "f7b322867a45f99afd9c8fbacdc56e1621676f9ca0f046656ec85eb6a99a3440"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_configure_prepend () {
	sed -e "s#CONFIG_RTE_LIBRTE_POWER=y#CONFIG_RTE_LIBRTE_POWER=${CONFIG_EXAMPLE_VM_POWER_MANAGER}#" -i ${S}/config/common_linuxapp
}
