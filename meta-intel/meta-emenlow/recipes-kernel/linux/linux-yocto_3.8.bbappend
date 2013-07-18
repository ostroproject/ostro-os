FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

LINUX_VERSION = "3.8.13"

SRCREV_meta_emenlow = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_emenlow = "f20047520a57322f05d95a18a5fbd082fb15cb87"
SRCREV_emgd_emenlow = "a18cbb7a2886206815dbf6c85caed3cb020801e0"

SRCREV_meta_emenlow-noemgd = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_emenlow-noemgd = "f20047520a57322f05d95a18a5fbd082fb15cb87"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
