FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.10.11"

SRCREV_meta_sugarbay = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_sugarbay = "702040ac7c7ec66a29b4d147665ccdd0ff015577"
