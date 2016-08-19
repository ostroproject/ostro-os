FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.15"
SRCREV_meta_i586-nlp-32-intel-common = "5df9a9f82e0ba355e030496ce21fd601b410172c"
SRCREV_machine_i586-nlp-32-intel-common = "015fb0cc854bd13523def72fe2bc47a3ee780e0d"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
