FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.10.55"
SRCREV_meta_crownbay-noemgd = "f79a00265eefbe2fffc2cdb03f67235497a9a87e"
SRCREV_machine_crownbay-noemgd = "3677ea7f9476458aa6dec440243de3a6fb1343a9"
