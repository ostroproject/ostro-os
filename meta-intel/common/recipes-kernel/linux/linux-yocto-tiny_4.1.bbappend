FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.28"
SRCREV_meta_i586-nlp-32-intel-common = "afbc6bd00e6fa854ae10eb67ab8c3be5112f6f41"
SRCREV_machine_i586-nlp-32-intel-common = "44af900716206d4cae283aa74e92f4118720724a"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
