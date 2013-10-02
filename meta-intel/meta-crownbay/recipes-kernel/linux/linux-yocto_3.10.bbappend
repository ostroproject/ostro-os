FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.11"

SRCREV_meta_crownbay-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_crownbay-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"

