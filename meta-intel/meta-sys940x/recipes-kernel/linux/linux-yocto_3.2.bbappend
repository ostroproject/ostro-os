FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
#KBRANCH_sys940x = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x ?= "06882fc16a4e965872e7faacb91da1497efd9ac3"
SRCREV_meta_pn-linux-yocto_sys940x ?= "486f7aec824b4127e91ef53228823e996b3696f0"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
#KBRANCH_sys940x-noemgd = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "06882fc16a4e965872e7faacb91da1497efd9ac3"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
