FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "standard/default/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "3303a0ec2cde4766fd0ee9dd059e9b4dd7bd7e79"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
