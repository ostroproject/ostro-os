FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION_i586-nlp-32-intel-common = "4.4.13"
SRCREV_meta_i586-nlp-32-intel-common = "44a610517357619a9ba827a597eef6d7f6e079f3"
SRCREV_machine_i586-nlp-32-intel-common = "13852755ecbf491848afbe40e66fc152bc70915b"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
