FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For Valley Island
KERNEL_FEATURES_INTEL_COMMON = "features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.38"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "d07bc7ba4ff00ddcd77db1026a63c327b81a35d8"
SRCREV_machine_core2-32-intel-common = "8aa9023c5e2e2ca4180e971da9a2c139d5b3c79e"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.38"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "d07bc7ba4ff00ddcd77db1026a63c327b81a35d8"
SRCREV_machine_corei7-64-intel-common = "8aa9023c5e2e2ca4180e971da9a2c139d5b3c79e"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/preempt-rt/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"
