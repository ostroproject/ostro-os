FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.14.0"
SRCREV_machine_fri2-noemgd = "144595ef6215a0febfb8ee7d0c9e4eb2eaf93d61"
SRCREV_meta_fri2-noemgd = "ad5f23c47b299418a88f13b1e6f119602115804a"

module_autoload_iwlwifi = "iwlwifi"
