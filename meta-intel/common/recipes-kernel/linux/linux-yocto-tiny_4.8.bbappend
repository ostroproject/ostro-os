FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.8.0-rc4"
SRCREV_meta_i586-nlp-32-intel-common = "8cb7317502c2577f8c83eaf1c061603023824313"
SRCREV_machine_i586-nlp-32-intel-common = "3eab887a55424fc2c27553b7bfe32330df83f7b8"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"

KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
