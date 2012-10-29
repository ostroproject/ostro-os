FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "f5a22aa0b14bb998d88ad4732f85b66c347631f8"
SRCREV_meta_pn-linux-yocto_crownbay ?= "486f7aec824b4127e91ef53228823e996b3696f0"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "f5a22aa0b14bb998d88ad4732f85b66c347631f8"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
