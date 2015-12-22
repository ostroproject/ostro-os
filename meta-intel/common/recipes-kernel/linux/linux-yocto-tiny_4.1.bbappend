FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.5"
SRCREV_meta-i586-nlp-32-intel-common = "46bb64d605fd336d99fa05bab566b9553b40b4b4"
SRCREV_machine-i586-nlp-32-intel-common = "788dfc9859321c09f1c58696bf8998f90ccb4f51"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
