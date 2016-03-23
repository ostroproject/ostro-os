FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.3"
SRCREV_meta-i586-nlp-32-intel-common = "e0cf18471a271cd057538e9d33fa01a7669ff76f"
SRCREV_machine-i586-nlp-32-intel-common = "3d2455f9da30f923c6bd69014fad4cc4ea738be6"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
