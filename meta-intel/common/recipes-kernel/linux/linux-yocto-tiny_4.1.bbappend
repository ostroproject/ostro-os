FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.28"
SRCREV_meta_i586-nlp-32-intel-common = "6a2047c00450aeafb7006805d266a44fd7676126"
SRCREV_machine_i586-nlp-32-intel-common = "846e0a90dd228d07272bf5b246aab405ec6941f8"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
