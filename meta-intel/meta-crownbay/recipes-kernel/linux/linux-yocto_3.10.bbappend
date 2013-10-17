FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_append_crownbay = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.11"

SRCREV_meta_crownbay = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_crownbay = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"
SRCREV_emgd_crownbay = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_crownbay-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_crownbay-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
