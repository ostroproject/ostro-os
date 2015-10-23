FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.2"
COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
SRCREV_meta-nlp-32-intel-common = "aed902160251d69cc28d1e69a4f692e8ea8fa13b"
SRCREV_machine-nlp-32-intel-common = "dbe692d91c8e55d1430f2c45fd578c8e4e71e482"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
