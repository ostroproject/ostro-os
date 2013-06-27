FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_sugarbay_append = " features/usb/usb-uvcvideo features/media/v4l2"

LINUX_VERSION = "3.8.13"

SRCREV_meta_sugarbay = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_sugarbay = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"
