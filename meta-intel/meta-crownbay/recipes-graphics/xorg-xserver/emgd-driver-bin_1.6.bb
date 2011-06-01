SUMMARY = "EMGD 1.6 xserver binaries"
DESCRIPTION = "EMGD 1.6 includes some userspace binaries that use non-free licensing.  Intel Open Source Technology Center unfortunately has no power to change that, but tries to make their use as painless as possible.  Please see the README in meta-crownbay/ for instructions on the (simple) manual steps necessary to make the necessary binaries available to this recipe.  Please do that before building an image."

LICENSE = "Intel-binary-only"
LIC_FILES_CHKSUM = "file://${WORKDIR}/License.txt;md5=b54f01caaf8483b3cb60c0c40f2bf22d"
PR = "r0"

FILESPATH = "${FILE_DIRNAME}/emgd-driver-bin-1.6"

FILES_${PN} = "${libdir}/*.so.* ${libdir}/dri ${libdir}/xorg/modules/drivers"

SRC_URI = "file://lib \
           file://License.txt"

S = "${WORKDIR}"

do_install () {
	install -d -m 0755 ${D}/${libdir}/dri ${D}/${libdir}/xorg/modules/drivers

	cp -PR	${S}/lib/lib*					${D}${libdir}
	install -m 0755	${S}/lib/xorg/modules/drivers/*		${D}${libdir}/xorg/modules/drivers/
	install -m 0755	${S}/lib/dri/*				${D}${libdir}/dri/
}

LEAD_SONAME = "libEGL.so"
