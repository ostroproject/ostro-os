FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION = "3.10.19"

SRCREV_meta_emenlow = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_emenlow = "a9ec82e355130160f9094e670bd5be0022a84194"
SRCREV_emgd_emenlow = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_emenlow-noemgd = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_emenlow-noemgd = "a9ec82e355130160f9094e670bd5be0022a84194"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
