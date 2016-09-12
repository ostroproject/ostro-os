FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.30"
SRCREV_meta_i586-nlp-32-intel-common = "cf6d9876629270e8ed99541db252840291d03f5a"
SRCREV_machine_i586-nlp-32-intel-common = "488286187ea5bda2e35730e5593f040c9f0f34d1"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
