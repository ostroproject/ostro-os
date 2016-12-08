FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.1.35"
SRCREV_meta_i586-nlp-32-intel-common = "b28f454e264f24abce6acda7c1c4f05d9a6f7ba5"
SRCREV_machine_i586-nlp-32-intel-common = "274f08fb196afa099d003166399e6bd1952fd80c"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
