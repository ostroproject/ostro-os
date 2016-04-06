FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.3"
SRCREV_meta-i586-nlp-32-intel-common = "770996a263e22562c81f48fde0f0dc647156abce"
SRCREV_machine-i586-nlp-32-intel-common = "c43425f73287757a166d74464fddf1f5389c9f59"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
