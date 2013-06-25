require ${COREBASE}/meta/recipes-graphics/xorg-app/xorg-app-common.inc

SUMMARY = "Intel GPU tools"
DESCRIPTION = "Variety of small tools for testing intel graphics."

SRC_URI += "file://install-fitter.patch"

SRC_URI[md5sum] = "67facd6241e26e2c68614728e3a932e9"
SRC_URI[sha256sum] = "51d22fdb3d415a1b3b7d0a172c1bb24dec6f16116e80a9ce49873f44527f20a0"

LIC_FILES_CHKSUM = "file://COPYING;md5=0918806acfedc3e8c0488f2dd61616dd"

DEPENDS += "libdrm libpciaccess cairo udev glib-2.0"

EXTRA_OECONF = "--disable-nouveau --disable-shader-debugger"
