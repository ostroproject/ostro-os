FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.4.32"
SRCREV_meta_i586-nlp-32-intel-common = "2d1114e7b6f39e8e4c442ad18e2eda1a918c7e48"
SRCREV_machine_i586-nlp-32-intel-common = "56d90955fb338cb2badbcbbfbce21c9c774abdfc"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
