FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

SRCREV_meta_crownbay = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_crownbay = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_emgd_crownbay = "caea08c988e0f41103bbe18eafca20348f95da02"

SRCREV_meta_crownbay-noemgd = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_crownbay-noemgd = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
