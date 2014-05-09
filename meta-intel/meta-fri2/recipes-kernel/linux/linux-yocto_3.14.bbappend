FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.14.2"
SRCREV_machine_fri2-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_fri2-noemgd = "71d5b64a173f51107bf947ceef80a5a7c8d72a7d"

module_autoload_iwlwifi = "iwlwifi"
