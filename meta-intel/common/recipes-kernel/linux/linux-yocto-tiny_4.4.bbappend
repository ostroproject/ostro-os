FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.18"
SRCREV_meta_i586-nlp-32-intel-common = "698835841165b68089604398f68fd8bc3f79cb65"
SRCREV_machine_i586-nlp-32-intel-common = "21ec8e8e70703aa0e721000a1f0ca31bbbd4dfe3"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
