FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For Valley Island
KERNEL_FEATURES_INTEL_COMMON = "features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.41"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "b6d95bb5bf6b9e9b5c149e68ffed6db7a58b4187"
SRCREV_machine_core2-32-intel-common = "f49f81e77f7bf3191a11c2557b2b47a8d0927a3a"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.41"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "b6d95bb5bf6b9e9b5c149e68ffed6db7a58b4187"
SRCREV_machine_corei7-64-intel-common = "f49f81e77f7bf3191a11c2557b2b47a8d0927a3a"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
