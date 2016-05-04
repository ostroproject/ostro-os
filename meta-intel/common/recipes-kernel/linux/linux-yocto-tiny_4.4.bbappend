FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.3"
SRCREV_meta-i586-nlp-32-intel-common = "082c2ea9f6bffa9b2bfa8f1e10b88046b8f064fd"
SRCREV_machine-i586-nlp-32-intel-common = "7a073202d4d47b5ffecf1e8f57b036f83b1fe2e0"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
