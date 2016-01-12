include dpdk.inc

SRC_URI += "\
            file://dpdk-2.2.0-add-config-variable-to-enable-disable-dpdk_qat.patch \
            file://dpdk-2.2.0-dpdk-enable-ip_fragmentation-in-common_linuxapp.patch \
            "

SRC_URI[dpdk.md5sum] = "22e2fd68cd5504f43fe9a5a6fd6dd938"
SRC_URI[dpdk.sha256sum] = "77206ad93618ec93ef6e59566e240aa80b6f660d12693febf0fa96ee23bd610d"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_configure_prepend () {
	sed -e "s#CONFIG_RTE_LIBRTE_POWER=y#CONFIG_RTE_LIBRTE_POWER=${CONFIG_EXAMPLE_VM_POWER_MANAGER}#" -i ${S}/config/common_linuxapp
}
