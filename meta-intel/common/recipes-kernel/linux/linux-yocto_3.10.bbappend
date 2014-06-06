FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC and Valley Island
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc \
				 features/valleyisland-io/valleyisland-io.scc"

LINUX_VERSION_core2-32-intel-common = "3.10.41"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "b6d95bb5bf6b9e9b5c149e68ffed6db7a58b4187"
SRCREV_machine_core2-32-intel-common = "ca510b5192c3b3814f1d1a19403d8847ba5db12b"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.10.41"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "b6d95bb5bf6b9e9b5c149e68ffed6db7a58b4187"
SRCREV_machine_corei7-64-intel-common = "ca510b5192c3b3814f1d1a19403d8847ba5db12b"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
module_autoload_uio = "uio"

# For FRI2, NUC
module_autoload_iwlwifi = "iwlwifi"
