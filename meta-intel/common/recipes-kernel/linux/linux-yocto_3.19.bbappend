FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# For NUC
KERNEL_FEATURES_INTEL_COMMON += "features/amt/mei/mei.scc"

LINUX_VERSION_core2-32-intel-common = "3.19.2"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
SRCREV_meta_core2-32-intel-common = "e308b2c52519c4ec60fe51f020e711cc12b799ae"
SRCREV_machine_core2-32-intel-common = "31b35da6a5c8a2b162f6c33202e9b64dd13757d5"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "standard/base"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "3.19.2"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
SRCREV_meta_corei7-64-intel-common = "e308b2c52519c4ec60fe51f020e711cc12b799ae"
SRCREV_machine_corei7-64-intel-common = "31b35da6a5c8a2b162f6c33202e9b64dd13757d5"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
KBRANCH_corei7-64-intel-common = "standard/base"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# For Crystalforest and Romley
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " uio"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " uio"

# For FRI2, NUC
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " iwlwifi"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " iwlwifi"
