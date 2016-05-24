FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.11"
SRCREV_meta-i586-nlp-32-intel-common = "6ec93aaa70f838b551f58b91d0c6ffeff6f6094b"
SRCREV_machine-i586-nlp-32-intel-common = "628bf627561c6285d99fb978e11d4c15fc29324b"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
