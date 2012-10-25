FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "f867af8e39af7a47b79e05b6b4ccc6cde09579ee"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "f867af8e39af7a47b79e05b6b4ccc6cde09579ee"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

module_autoload_iwlwifi = "iwlwifi"
