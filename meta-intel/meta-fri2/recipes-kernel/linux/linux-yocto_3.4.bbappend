FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/fri2"
SRCREV_machine_pn-linux-yocto_fri2 ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_fri2 ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

LINUX_VERSION = "3.4.11"

module_autoload_iwlwifi = "iwlwifi"
