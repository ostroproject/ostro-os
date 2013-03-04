FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"
KBRANCH_sys940x = "standard/sys940x"
KERNEL_FEATURES_sys940x = " features/drm-emgd/drm-emgd-1.16"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KBRANCH_sys940x-noemgd = "standard/sys940x"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"

SRCREV_meta_sys940x = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_sys940x = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_emgd_sys940x = "caea08c988e0f41103bbe18eafca20348f95da02"

SRCREV_meta_sys940x-noemgd = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_sys940x-noemgd = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"

SRC_URI_sys940x = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
