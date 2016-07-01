FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.26"
SRCREV_meta_i586-nlp-32-intel-common = "e978d15367ec69788c4a10d1e2a65bfa626c5d8c"
SRCREV_machine_i586-nlp-32-intel-common = "9f166e918f63dd7214ad0388d64709d33f2a14a3"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
