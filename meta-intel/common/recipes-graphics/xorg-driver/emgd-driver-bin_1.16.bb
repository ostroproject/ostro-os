SUMMARY = "EMGD 1.16 xserver binaries"
DESCRIPTION = "EMGD 1.16 includes some userspace binaries that use non-free \
licensing, which are now available via a non-click-through downloadable \
tarball, and is what this recipe now uses.  Since it is a non-free license, \
this recipe is marked as 'License_emgd-driver-bin_1.16' and you need to add \
to LICENSE_FLAGS_WHITELIST += \"license_emgd-driver-bin_1.16\" to your \
local.conf in order to enable it in a build."
LICENSE = "Intel-software-license-emgd-1.16 & Intel-user-space-graphics-driver-binary-license-emgd-1.16 & MIT"
LICENSE_FLAGS = "license_${PN}_${PV}"
PR = "r0"

COMPATIBLE_HOST = "(i.86).*-linux"

EMGD_LIC_DIR = "IEMGD_HEAD_Linux/License"
EMGD_RPM_DIR = "IEMGD_HEAD_Linux/MeeGo1.2"
EMGD_VIDEO_PLUGIN_DIR = "../common/video_plugin"

LIC_FILES_CHKSUM = "file://${WORKDIR}/${EMGD_LIC_DIR}/License.txt;md5=b54f01caaf8483b3cb60c0c40f2bf22d \
                    file://${WORKDIR}/${EMGD_LIC_DIR}/readme.txt;md5=73cbec7a0d2bc22faf567238e055bfc8"

DEPENDS = "rpm-native xz-native"
RDEPENDS_${PN} = "libxcb-dri2 cairo xserver-xorg"
RDEPENDS_emgd-gst-plugins-mixvideo = "libva-tpi"

# These libraries shouldn't get installed in world builds unless something
# explicitly depends upon them.
EXCLUDE_FROM_WORLD = "1"
PROVIDES = "virtual/libgles1 virtual/libgles2 virtual/egl"

# Add the ABI dependency at package generation time, as otherwise bitbake will
# attempt to find a provider for it (and fail) when it does the parse.
#
# This version *must* be kept correct.
python populate_packages_prepend() {
    pn = d.getVar("PN", True)
    d.appendVar("RDEPENDS_" + pn, " xorg-abi-video-8")
}

inherit distro_features_check
REQUIRED_DISTRO_FEATURES = "opengl"

SRC_URI = "https://edc.intel.com/App_Shared/Downloads/LIN_IEMGD_1_16_GOLD_3228.tgz \
           file://egl.pc \
           file://gles_cm.pc \
           file://glesv2.pc \
          "

SRC_URI[md5sum] = "339c902baeac0a5816108bea827b3685"
SRC_URI[sha256sum] = "33ef38b83914ef7d1e12a430ec009352b415b9d5840c9d0db25744b7dc6a2473"


# make sure generated rpm packages get non conflicting names
PKG_${PN} = "emgd-driver"
PKG_${PN}-dev = "emgd-driver-dev"
PKG_${PN}-dbg = "emgd-driver-dbg"
PKG_${PN}-doc = "emgd-driver-doc"

PACKAGES =+ "emgd-libmixcommon emgd-libmixvideo emgd-libmixvbp \
             emgd-gst-vabuffer emgd-gst-plugins-mixvideo \
             emgd-gst-plugins-va emgd-driver-video"

# These are closed binaries generated elsewhere so don't check ldflags & text relocations
INSANE_SKIP_emgd-driver-video = "ldflags textrel"
# Inhibit warnings about files being stripped, we can't do anything about it.
INHIBIT_PACKAGE_STRIP = "1"
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

# Avoid auto renaming of these packages
DEBIAN_NOAUTONAME_emgd-libmixcommon = "1"
DEBIAN_NOAUTONAME_emgd-libmixvideo = "1"
DEBIAN_NOAUTONAME_emgd-libmixvbp = "1"
DEBIAN_NOAUTONAME_emgd-gst-vabuffer = "1"

FILES_emgd-libmixcommon = "${libdir}/libmixcommon.so.0.10.8 ${libdir}/libmixcommon.so.0"
FILES_emgd-libmixvideo = "${libdir}/libmixvideo.so.0.10.10 ${libdir}/libmixvideo.so.0"
FILES_emgd-libmixvbp = "${libdir}/libmixvbp.so.0.10.9 ${libdir}/libmixvbp.so.0 \
                            ${libdir}/libmixvbp_h264.so.0.10.9 ${libdir}/libmixvbp_h264.so.0 \
                            ${libdir}/libmixvbp_mpeg4.so.0.10.9 ${libdir}/libmixvbp_mpeg4.so.0 \
                            ${libdir}/libmixvbp_vc1.so.0.10.9 ${libdir}/libmixvbp_vc1.so.0 "
FILES_emgd-gst-vabuffer = "${libdir}/libgstvabuffer.so.0.10.8 ${libdir}/libgstvabuffer.so.0"
FILES_emgd-gst-plugins-mixvideo = "${libdir}/gstreamer-0.10/libgstmixvideoplugin.so"
FILES_emgd-gst-plugins-va = "${libdir}/gstreamer-0.10/libgstvaplugin.so"
FILES_emgd-driver-video = "${libdir}/dri/emgd_drv_video.so"
FILES_${PN} += "${libdir}/dri ${libdir}/xorg/modules/drivers"
FILES_${PN}-dbg += "${libdir}/xorg/modules/drivers/.debug ${libdir}/dri/.debug ${libdir}/gstreamer-0.10/.debug"

S = "${WORKDIR}/${EMGD_RPM_DIR}"

RPM2CPIO = "${COREBASE}/scripts/rpm2cpio.sh"

do_install () {
    # cleanup previous files if any
    rm -rf usr

    # A gstreamer VA buffer library
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-vabuffer*.rpm | cpio -id

    # MIX Common contains common classes, datatype, header files used by other MIX components
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixcommon*.rpm | cpio -id

    # MIX Video Bitstream Parser is an user library interface for various video format bitstream parsing
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixvbp*.rpm | cpio -id

    # MIX Video is an user library interface for various video codecs available on the platform.
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/mixvideo*.rpm | cpio -id

    install -d -m 0755                                    ${D}${libdir}/gstreamer-0.10
    install -m 0755 ${S}/usr/lib/*                        ${D}${libdir}/

    # A gstreamer plugin that uses MIX Video for hardware accelerated video decoding and rendering.
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-plugins-mixvideo*.rpm | cpio -id

    # A collection of gstreamer plugins that uses VA libraries for hardware accelerated video rendering and text overlay.
    ${RPM2CPIO} ${S}/${EMGD_VIDEO_PLUGIN_DIR}/gst-plugins-va*.rpm | cpio -id

    install -m 0755 ${S}/usr/lib/gstreamer-0.10/*         ${D}${libdir}/gstreamer-0.10/

    # EMGD runtime graphics libraries
    ${RPM2CPIO} ${S}/emgd-bin*.rpm | cpio -id

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
    ${RPM2CPIO} ${S}/emgd-devel*.rpm | cpio -id

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

    EMGD_SNAPSHOT="1.5.15.3226"
    ln -sf libEGL.so.${EMGD_SNAPSHOT}                     ${D}${libdir}/libEGL.so.1
    ln -sf libEGL.so.1                                    ${D}${libdir}/libEGL.so
    ln -sf libGLES_CM.so.${EMGD_SNAPSHOT}                 ${D}${libdir}/libGLES_CM.so.1
    ln -sf libGLES_CM.so.1                                ${D}${libdir}/libGLES_CM.so
    ln -sf libGLESv2.so.${EMGD_SNAPSHOT}                  ${D}${libdir}/libGLESv2.so.2
    ln -sf libGLESv2.so.2                                 ${D}${libdir}/libGLESv2.so
    ln -sf libOpenVG.so.${EMGD_SNAPSHOT}                  ${D}${libdir}/libOpenVG.so.1
    ln -sf libOpenVG.so.1                                 ${D}${libdir}/libOpenVG.so
    ln -sf libOpenVGU.so.${EMGD_SNAPSHOT}                 ${D}${libdir}/libOpenVGU.so.1
    ln -sf libOpenVGU.so.1                                ${D}${libdir}/libOpenVGU.so
    ln -sf libEMGD2d.so.${EMGD_SNAPSHOT}                  ${D}${libdir}/libEMGD2d.so
    ln -sf libEMGDegl.so.${EMGD_SNAPSHOT}                 ${D}${libdir}/libEMGDegl.so
    ln -sf libemgdglslcompiler.so.${EMGD_SNAPSHOT}        ${D}${libdir}/libemgdglslcompiler.so
    ln -sf libEMGDOGL.so.${EMGD_SNAPSHOT}                 ${D}${libdir}/libEMGDOGL.so
    ln -sf libemgdPVR2D_DRIWSEGL.so.${EMGD_SNAPSHOT}      ${D}${libdir}/libemgdPVR2D_DRIWSEGL.so
    ln -sf libEMGDScopeServices.so.${EMGD_SNAPSHOT}       ${D}${libdir}/libEMGDScopeServices.so
    ln -sf libemgdsrv_init.so.${EMGD_SNAPSHOT}            ${D}${libdir}/libemgdsrv_init.so
    ln -sf libemgdsrv_um.so.${EMGD_SNAPSHOT}              ${D}${libdir}/libemgdsrv_um.so

    #Replace duplicate files with symlinks
    rm -f ${D}${libdir}/libmixvideo.so.0
    ln -sf libmixvideo.so.0.10.10                          ${D}${libdir}/libmixvideo.so.0
    rm -f ${D}${libdir}/libmixvbp_h264.so.0
    ln -sf libmixvbp_h264.so.0.10.9                       ${D}${libdir}/libmixvbp_h264.so.0
    rm -f ${D}${libdir}/libmixvbp.so.0
    ln -sf libmixvbp.so.0.10.9                            ${D}${libdir}/libmixvbp.so.0
    rm -f ${D}${libdir}/libmixvbp_vc1.so.0
    ln -sf libmixvbp_vc1.so.0.10.9                        ${D}${libdir}/libmixvbp_vc1.so.0
    rm -f ${D}${libdir}/libmixvbp_mpeg4.so.0
    ln -sf libmixvbp_mpeg4.so.0.10.9                      ${D}${libdir}/libmixvbp_mpeg4.so.0
    rm -f ${D}${libdir}/libmixcommon.so.0
    ln -sf libmixcommon.so.0.10.8                         ${D}${libdir}/libmixcommon.so.0
    rm -f ${D}${libdir}/libgstvabuffer.so.0
    ln -sf libgstvabuffer.so.0.10.8                       ${D}${libdir}/libgstvabuffer.so.0

    # Copy the .pc files
    install -d -m 0755                                    ${D}${libdir}/pkgconfig
    install -m 0644  ${WORKDIR}/*.pc                      ${D}${libdir}/pkgconfig/
}

LEAD_SONAME = "libEGL.so"
