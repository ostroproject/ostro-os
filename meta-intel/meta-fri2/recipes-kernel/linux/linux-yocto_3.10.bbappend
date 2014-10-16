FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.10.55"
SRCREV_meta_fri2-noemgd = "f79a00265eefbe2fffc2cdb03f67235497a9a87e"
SRCREV_machine_fri2-noemgd = "3677ea7f9476458aa6dec440243de3a6fb1343a9"

KERNEL_MODULE_AUTOLOAD_append_fri2-noemgd = " iwlwifi"
