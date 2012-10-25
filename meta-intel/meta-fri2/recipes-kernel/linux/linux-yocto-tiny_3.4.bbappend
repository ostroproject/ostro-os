FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/tiny/base"
#SRCREV_machine_pn-linux-yocto-tiny_fri2 ?= "449f7f520350700858f21a5554b81cc8ad23267d"
SRCREV_meta_pn-linux-yocto-tiny_fri2 ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"


COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/tiny/base"
#SRCREV_machine_pn-linux-yocto-tiny_fri2-noemgd ?= "449f7f520350700858f21a5554b81cc8ad23267d"
SRCREV_meta_pn-linux-yocto-tiny_fri2-noemgd ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"
