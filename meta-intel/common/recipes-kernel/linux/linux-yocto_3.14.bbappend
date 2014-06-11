FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc"

LINUX_VERSION_core2-32-intel-common = "3.14.4"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "62f236c734996f240d91daee2cb6a05669c7326c"
SRCREV_machine_core2-32-intel-common = "cb22733185cd9db3e8945dadb899d9eb3831b9ad"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.14.4"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "62f236c734996f240d91daee2cb6a05669c7326c"
SRCREV_machine_corei7-64-intel-common = "cb22733185cd9db3e8945dadb899d9eb3831b9ad"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
module_autoload_uio = "uio"

# For FRI2, NUC
module_autoload_iwlwifi = "iwlwifi"
