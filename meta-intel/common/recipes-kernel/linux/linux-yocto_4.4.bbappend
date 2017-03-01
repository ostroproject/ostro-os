FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_INTEL_COMMON = "4.4.41"
SRCREV_META_INTEL_COMMON = "f4a781388fae67caec79a5a571c8aadef0185044"
SRCREV_MACHINE_INTEL_COMMON = "eb391bc8320167a9d5875c6c84348a4bcce260ff"

KBRANCH_INTEL_COMMON = "standard/intel/base"

LINUX_VERSION_core2-32-intel-common = "${LINUX_VERSION_INTEL_COMMON}"
COMPATIBLE_MACHINE_core2-32-intel-common = "${MACHINE}"
KMACHINE_core2-32-intel-common = "intel-core2-32"
KBRANCH_core2-32-intel-common = "${KBRANCH_INTEL_COMMON}"
SRCREV_meta_core2-32-intel-common ?= "${SRCREV_META_INTEL_COMMON}"
SRCREV_machine_core2-32-intel-common ?= "${SRCREV_MACHINE_INTEL_COMMON}"
KERNEL_FEATURES_append_core2-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

LINUX_VERSION_corei7-64-intel-common = "${LINUX_VERSION_INTEL_COMMON}"
COMPATIBLE_MACHINE_corei7-64-intel-common = "${MACHINE}"
KMACHINE_corei7-64-intel-common = "intel-corei7-64"
SRCREV_meta_corei7-64-intel-common ?= "${SRCREV_META_INTEL_COMMON}"
SRCREV_machine_corei7-64-intel-common ?= "${@bb.utils.contains('INTEL_MACHINE_SUBTYPE', 'broxton-m', 'a249f6388ace2a4035220c2333649b42c300faa9', '${SRCREV_MACHINE_INTEL_COMMON}', d)}"
KBRANCH_corei7-64-intel-common = "${@bb.utils.contains('INTEL_MACHINE_SUBTYPE', 'broxton-m', 'standard/intel/bxt-rebase;rebaseable=1', '${KBRANCH_INTEL_COMMON}', d)}"
KERNEL_FEATURES_append_corei7-64-intel-common = "${KERNEL_FEATURES_INTEL_COMMON}"

# Quark / X1000 BSP Info
LINUX_VERSION_i586-nlp-32-intel-common = "${LINUX_VERSION_INTEL_COMMON}"
COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KBRANCH_i586-nlp-32-intel-common = "${KBRANCH_INTEL_COMMON}"
SRCREV_meta_i586-nlp-32-intel-common ?= "${SRCREV_META_INTEL_COMMON}"
SRCREV_machine_i586-nlp-32-intel-common ?= "${SRCREV_MACHINE_INTEL_COMMON}"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = ""


# For Crystalforest and Romley
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " uio"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " uio"

# For FRI2, NUC
KERNEL_MODULE_AUTOLOAD_append_core2-32-intel-common = " iwlwifi"
KERNEL_MODULE_AUTOLOAD_append_corei7-64-intel-common = " iwlwifi"
