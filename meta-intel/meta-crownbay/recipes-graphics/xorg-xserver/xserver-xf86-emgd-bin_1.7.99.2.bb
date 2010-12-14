SUMMARY = "EMGD 1.5 xserver binaries"
DESCRIPTION = "EMGD 1.5 includes some userspace binaries that use non-free licensing.  Intel Open Source Technology Center unfortunately has no power to change that, but tries to make their use as painless as possible.  Please see the README.before.building in meta-crownbay/recipes/xorg-xerver for instructions on the (simple) manual steps necessary to make the necessary binaries available to this recipe.  Please do that before building an image."

LICENSE = "Intel-binary-only"
LIC_FILES_CHKSUM = "file://${WORKDIR}/License.txt;md5=95c4d031b83ab803f3f2401b04ecfbcd"
PR = "r0"

FILESPATH = "${FILE_DIRNAME}/xserver-xf86-emgd-bin"

FILES_${PN} = "${libdir}/*.so.* ${libdir}/dri ${libdir}/xorg/modules/drivers"

SRC_URI = "file://emgd_dri.so \
           file://emgd_drv.so \
           file://emgd_drv_video.so \
           file://libEGL.so \
           file://libGLES_CM.so \
           file://libGLESv2.so \
           file://libIMGegl.so \
           file://libOpenVG.so \
           file://libOpenVGU.so \
           file://libPVROGL.so \
           file://libPVRScopeServices.so \
           file://libXegd_escape.so.2.0.0 \
           file://libglslcompiler.so \
           file://libpvr2d.so \
           file://libpvrPVR2D_DRIWSEGL.so \
           file://libsrv_init.so \
           file://libsrv_um.so \
           file://libva-x11.so.1.0.1 \
           file://libva.so.1.0.1 \
           file://License.txt"

S = "${WORKDIR}"

do_install () {
	install -d -m 0755 ${D}/${libdir}/dri ${D}/${libdir}/xorg/modules/drivers

	install -m 0755	${S}/emgd_dri.so			${D}${libdir}/dri/emgd_dri.so.1.1.15.3082
	ln -sf		emgd_dri.so.1.1.15.3082			${D}${libdir}/dri/emgd_dri.so

	install -m 0755	${S}/emgd_drv.so			${D}${libdir}/xorg/modules/drivers/emgd_drv.so
	install -m 0755	${S}/emgd_drv_video.so			${D}${libdir}/xorg/modules/drivers/emgd_drv_video.so

	install -m 0755	${S}/libEGL.so				${D}${libdir}/libEGL.so.1.1.15.3082
	ln -sf		libEGL.so.1.1.15.3082			${D}${libdir}/libEGL.so

	install -m 0755	${S}/libGLES_CM.so			${D}${libdir}/libGLES_CM.so.1.1.15.3082
	ln -sf		libGLES_CM.so.1.1.15.3082		${D}${libdir}/libGLES_CM.so

	install -m 0755	${S}/libGLESv2.so			${D}${libdir}/libGLESv2.so.1.1.15.3082
	ln -sf		libGLESv2.so.1.1.15.3082		${D}${libdir}/libGLESv2.so

	install -m 0755	${S}/libIMGegl.so			${D}${libdir}/libIMGegl.so.1.1.15.3082
	ln -sf		libIMGegl.so.1.1.15.3082		${D}${libdir}/libIMGegl.so

	install -m 0755	${S}/libOpenVG.so			${D}${libdir}/libOpenVG.so.1.1.15.3082
	ln -sf		libOpenVG.so.1.1.15.3082		${D}${libdir}/libOpenVG.so

	install -m 0755	${S}/libOpenVGU.so			${D}${libdir}/libOpenVGU.so.1.1.15.3082
	ln -sf		libOpenVG.so.1.1.15.3082		${D}${libdir}/libOpenVGU.so

	install -m 0755	${S}/libPVROGL.so			${D}${libdir}/libPVROGL.so.1.1.15.3082
	ln -sf		libPVROGL.so.1.1.15.3082		${D}${libdir}/libPVROGL.so

	install -m 0755	${S}/libPVRScopeServices.so		${D}${libdir}/libPVRScopeServices.so.1.1.15.3082
	ln -sf		libPVRScopeServices.so.1.1.15.3082	${D}${libdir}/libPVRScopeServices.so

	install -m 0755	${S}/libXegd_escape.so.2.0.0		${D}${libdir}/libXegd_escape.so.2.0.0

	install -m 0755	${S}/libglslcompiler.so			${D}${libdir}/libglslcompiler.so.1.1.15.3082
	ln -sf		libglslcompiler.so.1.1.15.3082		${D}${libdir}/libglslcompiler.so

	install -m 0755	${S}/libpvr2d.so			${D}${libdir}/libpvr2d.so.1.1.15.3082
	ln -sf		libpvr2d.so.1.1.15.3082			${D}${libdir}/libpvr2d.so

	install -m 0755	${S}/libpvrPVR2D_DRIWSEGL.so		${D}${libdir}/libpvrPVR2D_DRIWSEGL.so.1.1.15.3082
	ln -sf		libpvrPVR2D_DRIWSEGL.so.1.1.15.3082	${D}${libdir}/libpvrPVR2D_DRIWSEGL.so

	install -m 0755	${S}/libsrv_init.so			${D}${libdir}/libsrv_init.so.1.1.15.3082
	ln -sf		libsrv_init.so.1.1.15.3082		${D}${libdir}/libsrv_init.so

	install -m 0755	${S}/libsrv_um.so			${D}${libdir}/libsrv_um.so.1.1.15.3082
	ln -sf		libsrv_um.so.1.1.15.3082		${D}${libdir}/libsrv_um.so

	install -m 0755	${S}/libva-x11.so.1.0.1			${D}${libdir}/libva-x11.so.1.0.1

	install -m 0755	${S}/libva.so.1.0.1			${D}${libdir}/libva.so.1.0.1
}

LEAD_SONAME = "libEGL.so"
