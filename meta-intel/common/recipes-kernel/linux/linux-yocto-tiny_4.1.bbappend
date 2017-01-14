FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.1.37"
SRCREV_meta_i586-nlp-32-intel-common = "4de9b8f96c8dca0c55a496792a2ad4d2776e6657"
SRCREV_machine_i586-nlp-32-intel-common = "ea1c55e4260e8303839791de0ccadff26349d657"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
