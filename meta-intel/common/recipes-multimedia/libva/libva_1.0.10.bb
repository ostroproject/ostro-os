SUMMARY = "Video Acceleration (VA) API for Linux"
DESCRIPTION = "Video Acceleration API (VA API) is a library (libVA) \
and API specification which enables and provides access to graphics \
hardware (GPU) acceleration for video processing on Linux and UNIX \
based operating systems. Accelerated processing includes video \
decoding, video encoding, subpicture blending and rendering. The \
specification was originally designed by Intel for its GMA (Graphics \
Media Accelerator) series of GPU hardware, the API is however not \
limited to GPUs or Intel specific hardware, as other hardware and \
manufacturers can also freely use this API for hardware accelerated \
video decoding."

HOMEPAGE = "http://www.freedesktop.org/wiki/Software/vaapi"
BUGTRACKER = "https://bugs.freedesktop.org"

SECTION = "x11"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=2e48940f94acb0af582e5ef03537800f"

PR = "r1"

DEPENDS = "libxext libxfixes libdrm"

SRC_URI = "http://cgit.freedesktop.org/libva/snapshot/libva-${PV}.tar.bz2"

SRC_URI[md5sum] = "959de03d47654adab855e10bff614df3"
SRC_URI[sha256sum] = "05f757f0043dce9f753d354d15e0cb772b1240cc9d29d26bbb5526285a203693"

inherit autotools pkgconfig

LEAD_SONAME = "libva.so"

PACKAGES =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"
RDEPENDS_${PN} =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"
FILES_${PN}-x11 =+ "${libdir}/libva-x11.*"
FILES_${PN}-tpi =+ "${libdir}/libva-tpi.*"
FILES_${PN}-glx =+ "${libdir}/libva-glx.*"
FILES_${PN}-egl =+ "${libdir}/libva-egl.*"
