FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd  = "emenlow"
KBRANCH_emenlow-noemgd  = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

SRCREV_machine_pn-linux-yocto_emenlow ?= "38909cd5415a3a6c237ab2e880c57e853b3b472f"
SRCREV_meta_pn-linux-yocto_emenlow ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"
SRCREV_emgd_pn-linux-yocto_emenlow ?= "08f65e2611877f7339a0626ab1c7255a35787adb"

SRCREV_machine_pn-linux-yocto_emenlow-noemgd ?= "38909cd5415a3a6c237ab2e880c57e853b3b472f"
SRCREV_meta_pn-linux-yocto_emenlow-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"

LINUX_VERSION = "3.4.28"
