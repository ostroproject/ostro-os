FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.10"
SRCREV_meta-i586-nlp-32-intel-common = "d6ee402d461048cf1afd10375fee5769c06d21d6"
SRCREV_machine-i586-nlp-32-intel-common = "578ff2a88676d20439dbf3877768370d06a22d8f"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
