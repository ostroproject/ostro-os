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

INC_PR = "r1"

DEPENDS = "libxext libxfixes libdrm mesa"

inherit autotools pkgconfig

PACKAGES =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"
PROVIDES =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"
PACKAGES =+ "${PN}-x11-dev ${PN}-tpi-dev ${PN}-glx-dev ${PN}-egl-dev"
PACKAGES =+ "${PN}-x11-dbg ${PN}-tpi-dbg ${PN}-glx-dbg ${PN}-egl-dbg"
RPROVIDES_${PN}-dev =+ "${PN}-x11-dev ${PN}-tpi-dev ${PN}-glx-dev ${PN}-egl-dev"

RDEPENDS_${PN}-tpi =+ "${PN}"
RDEPENDS_${PN}-x11 =+ "${PN}"
RDEPENDS_${PN}-glx =+ "${PN}-x11"
RDEPENDS_${PN}-egl =+ "${PN}-x11"

FILES_${PN}-dbg += "${libdir}/dri/.debug"
FILES_${PN} += "${libdir}/dri"

FILES_${PN}-x11 =+ "${libdir}/libva-x11*${SOLIBS}"
FILES_${PN}-tpi =+ "${libdir}/libva-tpi*${SOLIBS}"
FILES_${PN}-glx =+ "${libdir}/libva-glx*${SOLIBS}"
FILES_${PN}-egl =+ "${libdir}/libva-egl*${SOLIBS}"

FILES_${PN}-x11-dev =+ "${libdir}/libva-x11*${SOLIBSDEV}"
FILES_${PN}-tpi-dev =+ "${libdir}/libva-tpi*${SOLIBSDEV}"
FILES_${PN}-glx-dev =+ "${libdir}/libva-glx*${SOLIBSDEV}"
FILES_${PN}-egl-dev =+ "${libdir}/libva-egl*${SOLIBSDEV}"
FILES_${PN}-x11-dev =+ "${libdir}/libva-x11*.la"
FILES_${PN}-tpi-dev =+ "${libdir}/libva-tpi*.la"
FILES_${PN}-glx-dev =+ "${libdir}/libva-glx*.la"
FILES_${PN}-egl-dev =+ "${libdir}/libva-egl*.la"
FILES_${PN}-x11-dev =+ "${libdir}/pkgconfig/libva-x11*.pc"
FILES_${PN}-tpi-dev =+ "${libdir}/pkgconfig/libva-tpi*.pc"
FILES_${PN}-glx-dev =+ "${libdir}/pkgconfig/libva-glx*.pc"
FILES_${PN}-egl-dev =+ "${libdir}/pkgconfig/libva-egl*.pc"

FILES_${PN}-x11-dbg =+ "${libdir}/.debug/libva-x11.*"
FILES_${PN}-tpi-dbg =+ "${libdir}/.debug/libva-tpi.*"
FILES_${PN}-glx-dbg =+ "${libdir}/.debug/libva-glx.*"
FILES_${PN}-egl-dbg =+ "${libdir}/.debug/libva-egl.*"
