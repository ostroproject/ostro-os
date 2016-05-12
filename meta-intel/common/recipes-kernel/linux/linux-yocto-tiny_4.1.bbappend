FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.1.18"
SRCREV_meta-i586-nlp-32-intel-common = "2bdebd11f1a0bc00071ec1467289a7feb5418dde"
SRCREV_machine-i586-nlp-32-intel-common = "d03753ddb28a1141e550a67c99ac95789a424fc5"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
