FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.28"
SRCREV_meta_i586-nlp-32-intel-common = "0d6de63d4603b9cc3a4a68391bcb5156b9b0cf96"
SRCREV_machine_i586-nlp-32-intel-common = "0530fc3c02d9f8bc7adc41db2b9318791dc3ca3a"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
