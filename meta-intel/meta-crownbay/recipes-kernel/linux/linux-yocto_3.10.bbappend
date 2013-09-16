FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.11"

SRCREV_meta_crownbay-noemgd = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_crownbay-noemgd = "702040ac7c7ec66a29b4d147665ccdd0ff015577"

