FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.10.11"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_fri2-noemgd = "702040ac7c7ec66a29b4d147665ccdd0ff015577"

module_autoload_iwlwifi = "iwlwifi"

