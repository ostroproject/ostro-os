FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/base"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.14.2"
SRCREV_machine_crownbay-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_crownbay-noemgd = "71d5b64a173f51107bf947ceef80a5a7c8d72a7d"
