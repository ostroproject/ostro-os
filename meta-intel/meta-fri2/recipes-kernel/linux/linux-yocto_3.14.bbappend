FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.14.2"
SRCREV_machine_fri2-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_fri2-noemgd = "4df1e2ed992adeac4da60ad5118d0237e8cb88df"

module_autoload_iwlwifi = "iwlwifi"
