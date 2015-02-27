SUMMARY = "VA-API support to GStreamer"
DESCRIPTION = "gstreamer-vaapi consists of a collection of VA-API \
based plugins for GStreamer and helper libraries: `vaapidecode', \
`vaapiconvert', and `vaapisink'."

REALPN = "gstreamer-vaapi"
FILESPATH = "${@base_set_filespath(["${FILE_DIRNAME}/${REALPN}", "${FILE_DIRNAME}/${REALPN}"], d)}"

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "libva"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/${REALPN}/${REALPN}-${PV}.tar.bz2 \
           file://install-tests.patch \
           "

SRC_URI[md5sum] = "3bd90b696b644be943450ba0c1497193"
SRC_URI[sha256sum] = "0dd236c7bf225322b8934fdba99a7a9e4542566a2acbe7564cdc3ec2c8b73c9d"

S = "${WORKDIR}/${REALPN}-${PV}"

inherit autotools pkgconfig gtk-doc

PACKAGES =+ "${PN}-tests"

EXTRA_OECONF += "--with-gstreamer-api=${GST_API_VERSION} --disable-builtin-libvpx"

PACKAGECONFIG ??= "drm \
                   ${@base_contains("DISTRO_FEATURES", "opengl x11", "glx", "", d)} \
                   ${@base_contains("DISTRO_FEATURES", "wayland", "wayland", "", d)} \
                   ${@base_contains("DISTRO_FEATURES", "x11", "x11", "", d)}"

PACKAGECONFIG[drm] = "--enable-drm,--disable-drm,udev libdrm"
PACKAGECONFIG[glx] = "--enable-glx,--disable-glx,virtual/mesa"
PACKAGECONFIG[wayland] = "--enable-wayland,--disable-wayland,wayland"
PACKAGECONFIG[x11] = "--enable-x11,--disable-x11,virtual/libx11 libxrandr libxrender"

FILES_${PN} += "${libdir}/gstreamer-*/*.so"
FILES_${PN}-dbg += "${libdir}/gstreamer-*/.debug"
FILES_${PN}-dev += "${libdir}/gstreamer-*/*.la ${libdir}/gstreamer-*/*.a"
FILES_${PN}-tests = "${bindir}/*"
