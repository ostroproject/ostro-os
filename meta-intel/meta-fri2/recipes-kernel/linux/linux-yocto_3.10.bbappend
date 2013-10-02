FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.10.11"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_fri2-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"

module_autoload_iwlwifi = "iwlwifi"

