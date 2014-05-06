FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.14.2"
SRCREV_machine_crownbay-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_crownbay-noemgd = "4df1e2ed992adeac4da60ad5118d0237e8cb88df"
