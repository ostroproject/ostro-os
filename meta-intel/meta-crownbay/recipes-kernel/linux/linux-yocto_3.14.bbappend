FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION_crownbay-noemgd = "3.14.0"
SRCREV_machine_crownbay-noemgd = "0143c6ebb4a2d63b241df5f608b19f483f7eb9e0"
SRCREV_meta_crownbay-noemgd = "fc8c30398dbc3cdea787a1042242d4aab689d0ae"
