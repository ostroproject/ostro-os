FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

SRCREV_meta_emenlow = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_emenlow = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_emgd_emenlow = "caea08c988e0f41103bbe18eafca20348f95da02"

SRCREV_meta_emenlow-noemgd = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_emenlow-noemgd = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
