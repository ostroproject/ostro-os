FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_fri2_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_meta_fri2 = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_fri2 = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_emgd_fri2 = "caea08c988e0f41103bbe18eafca20348f95da02"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_fri2_append = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_fri2-noemgd = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"

module_autoload_iwlwifi = "iwlwifi"

SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
