FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KERNEL_FEATURES_INTEL_COMMON = ""

#LINUX_VERSION_core2-32-intel-common = "3.10"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
#SRCREV_meta_core2-32-intel-common = "${AUTOREV}"
#SRCREV_machine_core2-32-intel-common = "${AUTOREV}"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

#LINUX_VERSION_corei7-64-intel-common = "3.10"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
#SRCREV_meta_corei7-64-intel-common = "${AUTOREV}"
#SRCREV_machine_corei7-64-intel-common = "${AUTOREV}"
KMACHINE_intel-corei7-64-intel-common = "intel-corei7-64"
KBRANCH_intel-corei7-64-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
