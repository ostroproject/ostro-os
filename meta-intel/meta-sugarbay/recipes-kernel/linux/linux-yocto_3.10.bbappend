FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/media/media-usb-webcams.scc"

LINUX_VERSION = "3.10.19"

SRCREV_meta_sugarbay = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_sugarbay = "a9ec82e355130160f9094e670bd5be0022a84194"
