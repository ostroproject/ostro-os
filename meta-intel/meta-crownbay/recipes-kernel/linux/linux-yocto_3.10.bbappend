FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.10.38"
SRCREV_meta_crownbay-noemgd = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_crownbay-noemgd = "02f7e63e56c061617957388c23bd5cf9b05c5388"
