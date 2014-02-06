FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_append_crownbay = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.17"
LINUX_VERSION = "3.10.19"

SRCREV_meta_crownbay = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_crownbay = "a9ec82e355130160f9094e670bd5be0022a84194"
SRCREV_emgd_crownbay = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_crownbay-noemgd = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_crownbay-noemgd = "a9ec82e355130160f9094e670bd5be0022a84194"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
