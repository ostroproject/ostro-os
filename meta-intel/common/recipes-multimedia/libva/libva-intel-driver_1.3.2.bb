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
SRC_URI += "file://wayland-include.patch"

SRC_URI[md5sum] = "3f4f08f1d42ee451b2fb9c239ee0b8d7"
SRC_URI[sha256sum] = "11d956ce11cb85bb009c8eb1ebb768403da2cb82675a6d66649f9c49ef4908d1"

inherit autotools pkgconfig

PACKAGECONFIG ??= "${@base_contains("DISTRO_FEATURES", "x11", "x11", "", d)} \
                   ${@base_contains("DISTRO_FEATURES", "opengl wayland", "wayland", "", d)}"
PACKAGECONFIG[x11] = "--enable-x11,--disable-x11"
PACKAGECONFIG[wayland] = "--enable-wayland,--disable-wayland,wayland virtual/egl"

FILES_${PN} += "${libdir}/dri/*.so"
FILES_${PN}-dev += "${libdir}/dri/*.la"
FILES_${PN}-dbg += "${libdir}/dri/.debug"
