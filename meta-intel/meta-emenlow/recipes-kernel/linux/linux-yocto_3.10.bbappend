FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION = "3.10.11"

SRCREV_meta_emenlow = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_emenlow = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"
SRCREV_emgd_emenlow = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_emenlow-noemgd = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_emenlow-noemgd = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
