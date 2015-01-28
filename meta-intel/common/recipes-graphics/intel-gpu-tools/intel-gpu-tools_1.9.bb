require ${COREBASE}/meta/recipes-graphics/xorg-app/xorg-app-common.inc

SUMMARY = "Intel GPU tools"
DESCRIPTION = "Variety of small tools for testing intel graphics."

SRC_URI[md5sum] = "1e768f2b1edc8613911b1d33bb361a7f"
SRC_URI[sha256sum] = "1de4c28ae0fe1e6c198ab559dbffcec6762798dc4adbdfdac54b2c7a9b0a1ed3"

LIC_FILES_CHKSUM = "file://COPYING;md5=0918806acfedc3e8c0488f2dd61616dd"

DEPENDS += "libdrm libpciaccess cairo udev glib-2.0 libxv libx11 libxext libxrandr"

EXTRA_OECONF = "--disable-nouveau --disable-shader-debugger --disable-dumper"
COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"

gputools_sysroot_preprocess() {
	rm -f ${SYSROOT_DESTDIR}${libdir}/pkgconfig/intel-gen4asm.pc
}
SYSROOT_PREPROCESS_FUNCS += "gputools_sysroot_preprocess"
