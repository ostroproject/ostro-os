FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION = "3.10.17"

SRCREV_meta_emenlow = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_emenlow = "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_emgd_emenlow = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_emenlow-noemgd = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_emenlow-noemgd = "c03195ed6e3066494e3fb4be69154a57066e845b"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
