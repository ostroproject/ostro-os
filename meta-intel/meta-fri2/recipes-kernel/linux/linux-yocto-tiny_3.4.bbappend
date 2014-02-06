FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/tiny/base"
#SRCREV_machine_pn-linux-yocto-tiny_fri2 ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto-tiny_fri2 ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"


COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/tiny/base"
#SRCREV_machine_pn-linux-yocto-tiny_fri2-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto-tiny_fri2-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"
