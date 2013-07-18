FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"
LINUX_VERSION = "3.8.13"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"
KBRANCH_sys940x = "standard/sys940x"
KERNEL_FEATURES_sys940x = " features/drm-emgd/drm-emgd-1.18"
SRCREV_meta_sys940x = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_sys940x = "f20047520a57322f05d95a18a5fbd082fb15cb87"
SRCREV_emgd_sys940x = "a18cbb7a2886206815dbf6c85caed3cb020801e0"
SRC_URI_sys940x = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KBRANCH_sys940x-noemgd = "standard/sys940x"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"
SRCREV_meta_sys940x-noemgd = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_sys940x-noemgd = "f20047520a57322f05d95a18a5fbd082fb15cb87"

