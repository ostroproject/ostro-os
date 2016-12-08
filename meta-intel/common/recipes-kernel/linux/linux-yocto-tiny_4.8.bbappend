FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.8.10"
SRCREV_meta_i586-nlp-32-intel-common = "f768e31c67f7c67b27ff2c1ba857eef2367de974"
SRCREV_machine_i586-nlp-32-intel-common = "96ea072413fb386598a62c77ed202a6de08085f6"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"

KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
