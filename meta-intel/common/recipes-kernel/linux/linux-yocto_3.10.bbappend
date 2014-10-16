FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC and Valley Island
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc \
				 features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.55"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "f79a00265eefbe2fffc2cdb03f67235497a9a87e"
SRCREV_machine_core2-32-intel-common = "3677ea7f9476458aa6dec440243de3a6fb1343a9"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.55"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "f79a00265eefbe2fffc2cdb03f67235497a9a87e"
SRCREV_machine_corei7-64-intel-common = "3677ea7f9476458aa6dec440243de3a6fb1343a9"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " uio"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " uio"

# For FRI2, NUC
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " iwlwifi"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " iwlwifi"
