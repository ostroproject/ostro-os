FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "47c5a633aa48ee20152ea009079f141a3009ec1b"
SRCREV_meta_pn-linux-yocto_crownbay ?= "e7f2fdc48f8808887175f0328274a2668084738c"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "47c5a633aa48ee20152ea009079f141a3009ec1b"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
