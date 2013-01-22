FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_fri2_append = " features/drm-emgd cfg/vesafb"
SRCREV_machine_pn-linux-yocto_fri2 ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_fri2 ?= "${AUTOREV}"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_fri2_append = " cfg/vesafb"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "${AUTOREV}"

module_autoload_iwlwifi = "iwlwifi"
