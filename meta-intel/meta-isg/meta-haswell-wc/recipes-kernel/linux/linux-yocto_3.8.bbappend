FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_haswell-wc = "haswell-wc"
KMACHINE_haswell-wc = "haswell-wc"
KBRANCH_haswell-wc = "standard/common-pc-64/base"

KERNEL_FEATURES_haswell-wc += "features/amt/mei"

LINUX_VERSION = "3.8.13"

SRCREV_machine_haswell-wc = "f20047520a57322f05d95a18a5fbd082fb15cb87"
SRCREV_meta_haswell-wc = "dfeaae26b811cb006f3013a1be7bb2de54d9c015"

SRC_URI_haswell-wc = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"
