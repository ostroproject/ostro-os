FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/base"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.14.2"
SRCREV_machine_crownbay-noemgd = "d0047ab24e8e92fc2a116b0bccfa10d6b84985be"
SRCREV_meta_crownbay-noemgd = "11e091dc40c53af6ea08ce491ae50fbb1b0b6377"
