FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_machine_pn-linux-yocto_fri2 ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_fri2 ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " cfg/vesafb"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

module_autoload_iwlwifi = "iwlwifi"

LINUX_VERSION = "3.4.28"
