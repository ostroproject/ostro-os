SUMMARY = "EMGD 1.8 xserver binaries"
DESCRIPTION = "EMGD 1.8 includes some userspace binaries that use non-free \
licensing.  Intel Open Source Technology Center unfortunately has no power \
to change that, but tries to make their use as painless as possible.  Please \
see the README in meta-crownbay/ for instructions on the (simple) manual \
steps necessary to make the necessary binaries available to this recipe.  \
Please do that before building an image."
LICENSE = "Intel-binary-only"
PR = "r7"

LIC_FILES_CHKSUM = "file://${WORKDIR}/License.txt;md5=b54f01caaf8483b3cb60c0c40f2bf22d"

FILESPATH = "${FILE_DIRNAME}/emgd-driver-bin-1.8"

SRC_URI = "file://lib \
           file://License.txt"

FILES_${PN} += "${libdir}/dri ${libdir}/xorg/modules/drivers"
FILES_${PN}-dev += "${libdir}/*.so"
FILES_${PN}-dbg += "${libdir}/xorg/modules/drivers/.debug ${libdir}/dri/.debug"

S = "${WORKDIR}"

do_install () {
    install -d -m 0755                    ${D}/${libdir}/dri
    install -d -m 0755                    ${D}/${libdir}/xorg/modules/drivers
    install -m 0755 ${S}/lib/*.so.*       ${D}${libdir}/
    install -m 0755 ${S}/lib/dri/*        ${D}${libdir}/dri/
    install -m 0755 ${S}/lib/xorg/modules/drivers/* ${D}${libdir}/xorg/modules/drivers/

    ln -sf libEGL.so.1                    ${D}${libdir}/libEGL.so
    ln -sf libGLES_CM.so.1                ${D}${libdir}/libGLES_CM.so
    ln -sf libGLESv2.so.2                 ${D}${libdir}/libGLESv2.so
    ln -sf libEMGDScopeServices.so.1.5.15.3226 ${D}${libdir}/libPVRScopeServices.so
}

LEAD_SONAME = "libEGL.so"
