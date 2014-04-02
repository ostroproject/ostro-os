FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow = "3.10.25"
SRCREV_meta_emenlow = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_emenlow = "79af968f2f26378798aec7a6d729ff5a371aae5f"
SRCREV_emgd_emenlow = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"

LINUX_VERSION_emenlow-noemgd = "3.10.25"
SRCREV_meta_emenlow-noemgd = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_emenlow-noemgd = "79af968f2f26378798aec7a6d729ff5a371aae5f"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
