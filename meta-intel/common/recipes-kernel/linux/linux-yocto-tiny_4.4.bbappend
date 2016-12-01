FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.4.32"
SRCREV_meta_i586-nlp-32-intel-common = "24ea5324fc90c7cb15ce1a08cdd294f22c6e6382"
SRCREV_machine_i586-nlp-32-intel-common = "56d90955fb338cb2badbcbbfbce21c9c774abdfc"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
