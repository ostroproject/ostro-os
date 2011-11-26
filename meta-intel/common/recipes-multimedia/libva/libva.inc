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

INC_PR = "r0"

DEPENDS = "libxext libxfixes libdrm"

inherit autotools pkgconfig

PACKAGES =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"
PACKAGES =+ "${PN}-x11-dev ${PN}-tpi-dev ${PN}-glx-dev ${PN}-egl-dev"

RDEPENDS_${PN} =+ "${PN}-x11 ${PN}-tpi ${PN}-glx ${PN}-egl"

FILES_${PN}-dbg += "${libdir}/dri/.debug"
FILES_${PN} += "${libdir}/dri"

FILES_${PN}-x11-dev =+ "${libdir}/libva-x11.so"
FILES_${PN}-tpi-dev =+ "${libdir}/libva-tpi.so"
FILES_${PN}-glx-dev =+ "${libdir}/libva-glx.so"
FILES_${PN}-egl-dev =+ "${libdir}/libva-egl.so"
FILES_${PN}-x11 =+ "${libdir}/libva-x11.*"
FILES_${PN}-tpi =+ "${libdir}/libva-tpi.*"
FILES_${PN}-glx =+ "${libdir}/libva-glx.*"
FILES_${PN}-egl =+ "${libdir}/libva-egl.*"
