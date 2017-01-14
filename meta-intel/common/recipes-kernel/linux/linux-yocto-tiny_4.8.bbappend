FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.8.17"
SRCREV_meta_i586-nlp-32-intel-common = "7b320e0a54be4b2d9bbaf4eb6165532e3954ad3e"
SRCREV_machine_i586-nlp-32-intel-common = "b62f29ac5c15d6333a13811db030d704b35ace8f"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"

KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
