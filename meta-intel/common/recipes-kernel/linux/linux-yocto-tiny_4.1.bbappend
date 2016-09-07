FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.30"
SRCREV_meta_i586-nlp-32-intel-common = "f7984d610b3e0dcffc52db019400ebce53ae28d7"
SRCREV_machine_i586-nlp-32-intel-common = "470c84a2e1ccde34c3d955ab6971771d17e73479"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
