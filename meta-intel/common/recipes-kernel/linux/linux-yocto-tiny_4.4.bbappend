FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.9"
SRCREV_meta-i586-nlp-32-intel-common = "344bfd3a9df9247b2aaf47b123916a94b23ab097"
SRCREV_machine-i586-nlp-32-intel-common = "242f3e2d6ec292c84813b0e8a577cc24a55335e7"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/common-pc"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
