FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.18"
SRCREV_meta_i586-nlp-32-intel-common = "59290c5f6192da2eccf478d37a8f9f88134822b3"
SRCREV_machine_i586-nlp-32-intel-common = "2cbbf10c66383c0c052708686ab005a9f9dc442c"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
