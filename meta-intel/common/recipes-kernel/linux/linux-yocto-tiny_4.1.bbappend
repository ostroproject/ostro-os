FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.2"
COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
SRCREV_meta_i586-nlp-32-intel-common = "429f9e2ff0649b8c9341345622545d874d5e303a"
SRCREV_machine_i586-nlp-32-intel-common = "59b8c4f5e8ddb9c33c62fff22204fe2b0d8c703e"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
