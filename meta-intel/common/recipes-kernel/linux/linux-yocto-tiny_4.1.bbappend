FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.18"
SRCREV_meta-i586-nlp-32-intel-common = "b9023d4c8fbbb854c26f158a079a5f54dd61964d"
SRCREV_machine-i586-nlp-32-intel-common = "91f62d4a0a31919d9b2ccdaf881130f99b61fc5e"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
