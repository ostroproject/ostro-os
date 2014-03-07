require ${COREBASE}/meta/recipes-graphics/xorg-app/xorg-app-common.inc

SUMMARY = "Intel GPU tools"
DESCRIPTION = "Variety of small tools for testing intel graphics."

SRC_URI += "file://install-fitter.patch"

SRC_URI[md5sum] = "6165a9054de2609f5b1bf0ca0d913f31"
SRC_URI[sha256sum] = "115475b528c78d67741ae6cbedfbfced1d471b356140e48245cbad8fdfaad1d1"

LIC_FILES_CHKSUM = "file://COPYING;md5=0918806acfedc3e8c0488f2dd61616dd"

DEPENDS += "libdrm libpciaccess cairo udev glib-2.0"

EXTRA_OECONF = "--disable-nouveau --disable-shader-debugger --disable-dumper"
COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"
