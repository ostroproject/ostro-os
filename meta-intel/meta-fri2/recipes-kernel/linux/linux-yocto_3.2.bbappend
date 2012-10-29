FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2 ?= "e0b29aa980673a1a5abde5ffdf356ca21b00f3ec"
SRCREV_meta_pn-linux-yocto_fri2 ?= "486f7aec824b4127e91ef53228823e996b3696f0"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "e0b29aa980673a1a5abde5ffdf356ca21b00f3ec"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"

module_autoload_iwlwifi = "iwlwifi"
