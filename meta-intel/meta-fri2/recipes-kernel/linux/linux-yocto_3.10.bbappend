FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.10.38"
SRCREV_meta_fri2-noemgd = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_fri2-noemgd = "02f7e63e56c061617957388c23bd5cf9b05c5388"

KERNEL_MODULE_AUTOLOAD_append_fri2-noemgd = " iwlwifi"
