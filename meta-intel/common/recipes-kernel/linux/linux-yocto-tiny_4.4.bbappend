FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.13"
SRCREV_meta_i586-nlp-32-intel-common = "01ac19ede037b753d2b3f0adb20ab1becb7e1511"
SRCREV_machine_i586-nlp-32-intel-common = "0e30a74f2cbbab0c7014561fe4eab1c9d8bfe560"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
