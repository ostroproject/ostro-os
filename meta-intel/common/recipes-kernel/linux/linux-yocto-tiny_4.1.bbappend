FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.1.36"
SRCREV_meta_i586-nlp-32-intel-common = "44719fa8f73fd7c444044ad3c04f5fc66f57b993"
SRCREV_machine_i586-nlp-32-intel-common = "5dc85f2035c2a9d0c78ccabf6960682d496b3b37"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
