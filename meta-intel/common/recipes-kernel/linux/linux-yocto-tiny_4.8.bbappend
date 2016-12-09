FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.8.12"
SRCREV_meta_i586-nlp-32-intel-common = "b22e47739683444916dc64548df1dbf6856500a5"
SRCREV_machine_i586-nlp-32-intel-common = "e274a507b23c23bf0dd6502d0c38fae731c11511"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"

KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
