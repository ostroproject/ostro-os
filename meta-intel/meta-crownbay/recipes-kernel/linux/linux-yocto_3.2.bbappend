FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "48101e609711fcfe8d5e737a37a5a69f4bd57d9a"
SRCREV_meta_pn-linux-yocto_crownbay ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "48101e609711fcfe8d5e737a37a5a69f4bd57d9a"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"
