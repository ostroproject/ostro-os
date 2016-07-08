FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.26"
SRCREV_meta_i586-nlp-32-intel-common = "48837d8ef0a7fcf781e735e58a7f58976443f8c0"
SRCREV_machine_i586-nlp-32-intel-common = "75d56a13f86fc48002e4a3f9ed60546db30432b7"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
