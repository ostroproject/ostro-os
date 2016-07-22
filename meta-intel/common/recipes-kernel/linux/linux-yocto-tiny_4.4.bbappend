FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.15"
SRCREV_meta_i586-nlp-32-intel-common = "8c6158ec5e43a4cae59058af49f70e0406d18091"
SRCREV_machine_i586-nlp-32-intel-common = "d6c9054e231ed9cbeee22162e0e5c532e31de534"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
