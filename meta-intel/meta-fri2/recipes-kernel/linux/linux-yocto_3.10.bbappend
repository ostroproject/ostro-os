FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_fri2 = "${MACHINE_ARCH}"
PACKAGE_ARCH_fri2-noemgd = "${MACHINE_ARCH}"

LINUX_VERSION = "3.10.19"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"
SRCREV_meta_fri2 = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_fri2 = "a9ec82e355130160f9094e670bd5be0022a84194"
SRCREV_emgd_fri2 = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_fri2-noemgd = "a9ec82e355130160f9094e670bd5be0022a84194"

module_autoload_iwlwifi = "iwlwifi"

