FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.10.11"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"
SRCREV_meta_fri2 = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_fri2 = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"
SRCREV_emgd_fri2 = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_fri2-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"

module_autoload_iwlwifi = "iwlwifi"

