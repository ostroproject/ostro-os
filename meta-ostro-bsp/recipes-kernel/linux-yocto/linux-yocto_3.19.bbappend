FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Override COMPATIBLE_MACHINE to include your machine in a bbappend
# file. Leaving it empty here ensures an early explicit build failure.
COMPATIBLE_MACHINE = "quark"

SRC_URI += "file://quark.cfg"

SRC_URI += "file://0001-initial-commit-integrate-only-system-core.patch"
SRC_URI += "file://0002-add-README.md.patch"
SRC_URI += "file://0003-galileo-linux-stable-add-default-kernel-config.patch"
SRC_URI += "file://0004-README.md-fix-spelling.patch"
SRC_URI += "file://0005-x86-quark-break-after-registering-a-default-board.patch"
SRC_URI += "file://0006-x86-quark-fix-compiler-warning.patch"
SRC_URI += "file://0007-gpio-i2c-add-gpio-and-i2c-support.patch"
SRC_URI += "file://0008-.config-enable-Intel-Quark-GIP.patch"
SRC_URI += "file://0009-.config-update-default-config.patch"
SRC_URI += "file://0010-.config-update-config-for-3.19.0.patch"
SRC_URI += "file://0011-drivers-gpio-gpio-sch.c-remove-references-to-sch_gpi.patch"
SRC_URI += "file://0012-staging-iio-add-support-for-ADCs-and-hrtimer-triger.patch"
SRC_URI += "file://0013-Update-README.md.patch"
SRC_URI += "file://0014-.config-add-Galileo-Gen-2-support.patch"
SRC_URI += "file://0015-x86-quark-add-Galileo-Gen2-platform-device.patch"
SRC_URI += "file://0016-x86-quark-request-a-single-GPIO-for-pcal9555a-expand.patch"
SRC_URI += "file://0017-Fixed-build-error-for-DATE-macro.patch"
