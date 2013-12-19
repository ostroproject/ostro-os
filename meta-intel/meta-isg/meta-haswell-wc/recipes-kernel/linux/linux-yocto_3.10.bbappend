FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_haswell-wc = "haswell-wc"
KMACHINE_haswell-wc = "haswell-wc"
KBRANCH_haswell-wc = "standard/common-pc-64/base"

KERNEL_FEATURES_haswell-wc += "features/amt/mei"

LINUX_VERSION = "3.10.19"

SRCREV_machine_haswell-wc = "a9ec82e355130160f9094e670bd5be0022a84194"
SRCREV_meta_haswell-wc = "d9cd83c0292bd4e2a6754a96761027252e726a42"

SRC_URI_haswell-wc = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"
