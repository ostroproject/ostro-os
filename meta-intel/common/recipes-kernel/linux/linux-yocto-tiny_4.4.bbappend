FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.12"
SRCREV_meta_i586-nlp-32-intel-common = "8900370d334ab4f7224fa71d7d46d62f0b11199d"
SRCREV_machine_i586-nlp-32-intel-common = "1f3e98df094cb7afb7d3d540dd0e47b3b8c89711"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
