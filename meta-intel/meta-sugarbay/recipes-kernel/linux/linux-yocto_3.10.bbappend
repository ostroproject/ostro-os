FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.10.11"

SRCREV_meta_sugarbay = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_sugarbay = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"
