FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.8.13"

SRCREV_meta_sugarbay = "467a74c47bd70c52d0b81597007d8cc39cadaefd"
SRCREV_machine_sugarbay = "f20047520a57322f05d95a18a5fbd082fb15cb87"
