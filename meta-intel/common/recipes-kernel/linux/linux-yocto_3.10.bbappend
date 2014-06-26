FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC and Valley Island
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc \
				 features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.38"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_core2-32-intel-common = "02f7e63e56c061617957388c23bd5cf9b05c5388"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.38"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_corei7-64-intel-common = "02f7e63e56c061617957388c23bd5cf9b05c5388"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
KERNEL_MODULE_AUTOLOAD_core2-32-intel-common += "uio"
KERNEL_MODULE_AUTOLOAD_corei7-64-intel-common += "uio"

# For FRI2, NUC
KERNEL_MODULE_AUTOLOAD_core2-32-intel-common += "iwlwifi"
KERNEL_MODULE_AUTOLOAD_corei7-64-intel-common += "iwlwifi"
