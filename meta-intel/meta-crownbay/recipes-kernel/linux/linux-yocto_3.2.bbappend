FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_crownbay ?= "${AUTOREV}"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "${AUTOREV}"
