SUMMARY = "EMGD 1.10 xserver binaries"
DESCRIPTION = "EMGD 1.10 includes some userspace binaries that use non-free \
licensing, which are now available via a non-click-through downloadable \
tarball, and is what this recipe now uses.  Since it is a non-free license, \
this recipe is marked as 'License_emgd-driver-bin_1.10' and you need to add \
to LICENSE_FLAGS_WHITELIST += \"License_emgd-driver-bin_1.10\" to your \
local.conf in order to enable it in a build."
LICENSE = "Intel-binary-only"
LICENSE_FLAGS = "license_${PN}_${PV}"
PR = "r0"

EMGD_LIC_DIR = "IEMGD_HEAD_Linux/License"
EMGD_RPM_DIR = "IEMGD_HEAD_Linux/MeeGo1.2"
EMGD_VIDEO_PLUGIN_DIR = "../common/video_plugin"

LIC_FILES_CHKSUM = "file://${WORKDIR}/${EMGD_LIC_DIR}/License.txt;md5=b54f01caaf8483b3cb60c0c40f2bf22d"

DEPENDS = "rpm-native xz-native"

SRC_URI = "https://edc.intel.com/App_Shared/Downloads/LIN_EMGD_1_10_RC_2209.tgz"

SRC_URI[md5sum] = "e4a38d9efa0b086ae21b68145c4db4e9"
SRC_URI[sha256sum] = "acea5f0f93a31553553428623c007d7ed0c604cf715fd87dfe075751da4be548"

FILES_${PN} += "${libdir}/dri ${libdir}/gstreamer-0.10 ${libdir}/xorg/modules/drivers"
FILES_${PN}-dev += "${libdir}/dri ${libdir}/xorg/modules/drivers"
FILES_${PN}-dbg += "${libdir}/xorg/modules/drivers/.debug ${libdir}/dri/.debug"

S = "${WORKDIR}/${EMGD_RPM_DIR}"

do_install () {
    # A gstreamer VA buffer library
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-vabuffer*.rpm | cpio -id

    # MIX Common contains common classes, datatype, header files used by other MIX components
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixcommon*.rpm | cpio -id

    # MIX Video Bitstream Parser is an user library interface for various video format bitstream parsing
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixvbp*.rpm | cpio -id

    # MIX Video is an user library interface for various video codecs available on the platform.
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixvideo*.rpm | cpio -id

    install -d -m 0755                                    ${D}${libdir}/gstreamer-0.10
    install -m 0755 ${S}/usr/lib/*                        ${D}${libdir}/

    # A gstreamer plugin that uses MIX Video for hardware accelerated video decoding and rendering.
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-plugins-mixvideo*.rpm | cpio -id

    # A collection of gstreamer plugins that uses VA libraries for hardware accelerated video rendering and text overlay.
    rpm2cpio ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-plugins-va*.rpm | cpio -id

    install -m 0755 ${S}/usr/lib/gstreamer-0.10/*         ${D}${libdir}/gstreamer-0.10/

    # EMGD runtime graphics libraries
    rpm2cpio ${S}/emgd-bin*.rpm | xz -d | cpio -id

    install -d -m 0755                                    ${D}${libdir}/dri
    install -d -m 0755                                    ${D}${libdir}/xorg/modules/drivers
    install -d -m 0755                                    ${D}${sysconfdir}
    install -d -m 0755                                    ${D}${mandir}/man4
    install -m 0755 ${S}/usr/lib/*.so.*                   ${D}${libdir}/
    install -m 0755 ${S}/usr/lib/dri/*                    ${D}${libdir}/dri/
    install -m 0755 ${S}/usr/lib/xorg/modules/drivers/*   ${D}${libdir}/xorg/modules/drivers/
    install -m 0755 ${S}/etc/*                            ${D}${sysconfdir}/
    install -m 0755 ${S}/usr/share/man/man4/*             ${D}${mandir}/man4/

    # Khronos development headers needed for EGL, OpenGL-ES, and OpenVG development
    rpm2cpio ${S}/emgd-devel*.rpm | xz -d | cpio -id

    install -d -m 0755                                    ${D}${includedir}/EGL
    install -m 0755 ${S}/usr/include/EGL/*.h              ${D}${includedir}/EGL/
    install -d -m 0755                                    ${D}${includedir}/GLES
    install -m 0755 ${S}/usr/include/GLES/*.h             ${D}${includedir}/GLES/
    install -d -m 0755                                    ${D}${includedir}/GLES2
    install -m 0755 ${S}/usr/include/GLES2/*.h            ${D}${includedir}/GLES2/
    install -d -m 0755                                    ${D}${includedir}/KHR
    install -m 0755 ${S}/usr/include/KHR/*.h              ${D}${includedir}/KHR/
    install -d -m 0755                                    ${D}${includedir}/VG
    install -m 0755 ${S}/usr/include/VG/*.h               ${D}${includedir}/VG/

    ln -sf libEGL.so.1                                    ${D}${libdir}/libEGL.so
    ln -sf libGLES_CM.so.1                                ${D}${libdir}/libGLES_CM.so
    ln -sf libGLESv2.so.2                                 ${D}${libdir}/libGLESv2.so
    ln -sf libOpenVG.so.1                                 ${D}${libdir}/libOpenVG.so
    ln -sf libOpenVGU.so.1                                ${D}${libdir}/libOpenVGU.so
}

LEAD_SONAME = "libEGL.so"
