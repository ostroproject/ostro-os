FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_haswell-wc = "haswell-wc"
KMACHINE_haswell-wc = "haswell-wc"
KBRANCH_haswell-wc = "standard/common-pc-64/base"

KERNEL_FEATURES_haswell-wc += "features/amt/mei"

LINUX_VERSION = "3.10.17"

SRCREV_machine_haswell-wc = "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_meta_haswell-wc = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

SRC_URI_haswell-wc = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"
