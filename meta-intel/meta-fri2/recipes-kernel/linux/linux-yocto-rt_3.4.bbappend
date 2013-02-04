FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "2ee9df8d3205983a94321cad82befae4050f77b5"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "2ee9df8d3205983a94321cad82befae4050f77b5"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

module_autoload_iwlwifi = "iwlwifi"

LINUX_VERSION = "3.4.28"
