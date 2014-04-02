FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.14.0"
SRCREV_machine_fri2-noemgd = "0143c6ebb4a2d63b241df5f608b19f483f7eb9e0"
SRCREV_meta_fri2-noemgd = "fc8c30398dbc3cdea787a1042242d4aab689d0ae"

module_autoload_iwlwifi = "iwlwifi"
