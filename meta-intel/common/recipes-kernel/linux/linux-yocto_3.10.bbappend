FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC and Valley Island
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc \
				 features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.38"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "617c6158c3d5b931f0d6131e0b0a7b374c792599"
SRCREV_machine_core2-32-intel-common = "02f7e63e56c061617957388c23bd5cf9b05c5388"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.38"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "617c6158c3d5b931f0d6131e0b0a7b374c792599"
SRCREV_machine_corei7-64-intel-common = "02f7e63e56c061617957388c23bd5cf9b05c5388"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
module_autoload_uio = "uio"

# For FRI2, NUC
module_autoload_iwlwifi = "iwlwifi"
