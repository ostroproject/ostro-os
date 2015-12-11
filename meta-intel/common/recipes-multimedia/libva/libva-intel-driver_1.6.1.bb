SUMMARY = "VA driver for Intel G45 & HD Graphics family"
DESCRIPTION = "libva-driver-intel is the VA-API implementation \
for Intel G45 chipsets and Intel HD Graphics for Intel Core \
processor family."

HOMEPAGE = "http://www.freedesktop.org/wiki/Software/vaapi"
BUGTRACKER = "https://bugs.freedesktop.org"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=2e48940f94acb0af582e5ef03537800f"

COMPATIBLE_HOST = '(i.86|x86_64).*-linux'

DEPENDS = "libva libdrm"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/${BPN}/${BPN}-${PV}.tar.bz2"

SRC_URI[md5sum] = "ed1b04c1a3c029ad389b7e23822a2762"
SRC_URI[sha256sum] = "3656e99c5ecbe8fe179478306da157dca997a61bb1b453715f52881edfa156db"

inherit autotools pkgconfig

PACKAGECONFIG ??= "${@base_contains("DISTRO_FEATURES", "x11", "x11", "", d)} \
                   ${@base_contains("DISTRO_FEATURES", "opengl wayland", "wayland", "", d)}"
PACKAGECONFIG[x11] = "--enable-x11,--disable-x11"
PACKAGECONFIG[wayland] = "--enable-wayland,--disable-wayland,wayland virtual/egl"

FILES_${PN} += "${libdir}/dri/*.so"
FILES_${PN}-dev += "${libdir}/dri/*.la"
FILES_${PN}-dbg += "${libdir}/dri/.debug"
