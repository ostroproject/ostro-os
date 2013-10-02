FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.10.11"

SRCREV_meta_sugarbay = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_sugarbay = "e1aa804148370cda6f85640281af156ffa007d52"
