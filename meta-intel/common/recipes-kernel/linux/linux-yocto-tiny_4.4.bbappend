FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION_i586-nlp-32-intel-common = "4.4.41"
SRCREV_meta_i586-nlp-32-intel-common = "78a26182e20c0a49c1adda63faa15ccd3f4ecb27"
SRCREV_machine_i586-nlp-32-intel-common = "6b94736dbcacbecd1d0c05fb5d8aacbed1a4b8fc"

COMPATIBLE_MACHINE_i586-nlp-32-intel-common = "${MACHINE}"
KBRANCH_i586-nlp-32-intel-common = "standard/tiny/intel/base"
KMACHINE_i586-nlp-32-intel-common = "intel-quark"
KERNEL_FEATURES_append_i586-nlp-32-intel-common = "${KERNEL_FEATURES_INTEL_COMMON} cfg/fs/ext4.scc"
