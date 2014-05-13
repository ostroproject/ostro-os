FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/base"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.14.2"
SRCREV_machine_fri2-noemgd = "d0047ab24e8e92fc2a116b0bccfa10d6b84985be"
SRCREV_meta_fri2-noemgd = "11e091dc40c53af6ea08ce491ae50fbb1b0b6377"

module_autoload_iwlwifi = "iwlwifi"
