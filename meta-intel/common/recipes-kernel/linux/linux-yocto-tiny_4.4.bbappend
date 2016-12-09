FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.4.36"
SRCREV_meta_i586-nlp-32-intel-common = "b846fc6436aa5d4c747d620e83dfda969854d10c"
SRCREV_machine_i586-nlp-32-intel-common = "52b43bce6be062690e7f8e3bb49243e3e1d4873d"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
