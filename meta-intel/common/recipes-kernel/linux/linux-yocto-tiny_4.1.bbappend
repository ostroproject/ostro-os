FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.1.37"
SRCREV_meta_i586-nlp-32-intel-common = "46b3153a39950b3542a99486bd964ab2ed65aeb4"
SRCREV_machine_i586-nlp-32-intel-common = "86a10ee9f4562882a0f74c1aacd195f46e9f2f53"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
