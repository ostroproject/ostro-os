FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.3"
SRCREV_meta-i586-nlp-32-intel-common = "e1515ef98cec975df218363e28c2abe3a71c6a59"
SRCREV_machine-i586-nlp-32-intel-common = "7a073202d4d47b5ffecf1e8f57b036f83b1fe2e0"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
