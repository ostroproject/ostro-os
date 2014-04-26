FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.14.0"
SRCREV_machine_crownbay-noemgd = "144595ef6215a0febfb8ee7d0c9e4eb2eaf93d61"
SRCREV_meta_crownbay-noemgd = "ad5f23c47b299418a88f13b1e6f119602115804a"
