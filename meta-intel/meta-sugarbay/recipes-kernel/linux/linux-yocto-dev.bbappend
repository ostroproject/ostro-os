FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_sugarbay = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay = "sugarbay"
KBRANCH_sugarbay = "standard/common-pc-64/sugarbay"
KERNEL_FEATURES_append_sugarbay = " features/media/media-usb-webcams.scc"

LINUX_VERSION = "3.12.0"

SRCREV_meta_sugarbay = "75feecae0382601045f508bcce104b3d4af1923d"
SRCREV_machine_sugarbay = "1f274173a8335dc27daabd9d9fe2e19a8b3978d1"

SRCREV_machine_sugarbay = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_sugarbay = "fe20c99783387dab779472ff50a88666da1c6391"
