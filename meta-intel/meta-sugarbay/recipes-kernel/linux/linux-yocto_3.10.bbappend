FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.10.17"

SRCREV_meta_sugarbay = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_sugarbay = "c03195ed6e3066494e3fb4be69154a57066e845b"
