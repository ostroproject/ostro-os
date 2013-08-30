FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.10.10"

SRCREV_meta_sugarbay = "ea900d1db60ba48962227f0976ac55f9e25bfa24"
SRCREV_machine_sugarbay = "ebc8428fdd938cfdfcdcadd77c3308ece6a57de1"
