require ${COREBASE}/meta/recipes-graphics/xorg-app/xorg-app-common.inc

SUMMARY = "Intel GPU tools"
DESCRIPTION = "Variety of small tools for testing intel graphics."

SRC_URI[md5sum] = "49d2c3c65204d889189c4d8c14c598b3"
SRC_URI[sha256sum] = "ffe2a11bca57f7fe36e93d55e4b3685127640e3e6cdae19973b193fe25ff3759"

LIC_FILES_CHKSUM = "file://COPYING;md5=0918806acfedc3e8c0488f2dd61616dd"

DEPENDS += "libdrm libpciaccess cairo udev glib-2.0 libxv libx11 libxext libxrandr"

EXTRA_OECONF = "--disable-nouveau --disable-shader-debugger --disable-dumper"
COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"

gputools_sysroot_preprocess() {
	rm -f ${SYSROOT_DESTDIR}${libdir}/pkgconfig/intel-gen4asm.pc
}
SYSROOT_PREPROCESS_FUNCS += "gputools_sysroot_preprocess"
