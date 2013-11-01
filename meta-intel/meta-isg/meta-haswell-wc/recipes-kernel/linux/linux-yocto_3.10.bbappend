FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_haswell-wc = "haswell-wc"
KMACHINE_haswell-wc = "haswell-wc"
KBRANCH_haswell-wc = "standard/common-pc-64/base"

KERNEL_FEATURES_haswell-wc += "features/amt/mei"

LINUX_VERSION = "3.10.11"

SRCREV_machine_haswell-wc = "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_haswell-wc = "aa4a6574195b220cacd9c1e8dcbba7b0b1085eb6"

SRC_URI_haswell-wc = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"
