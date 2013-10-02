FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"
LINUX_VERSION = "3.10.11"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KBRANCH_sys940x-noemgd = "standard/sys940x"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"
SRCREV_meta_sys940x-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_sys940x-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"
