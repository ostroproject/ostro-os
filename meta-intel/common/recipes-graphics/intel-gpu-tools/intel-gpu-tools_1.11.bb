require ${COREBASE}/meta/recipes-graphics/xorg-app/xorg-app-common.inc

SUMMARY = "Intel GPU tools"
DESCRIPTION = "Variety of small tools for testing intel graphics."

SRC_URI[md5sum] = "836e9fd084f63da2a29fe81a47eb3db8"
SRC_URI[sha256sum] = "48823450452b57c52c74e00c8c763ed7cdd0c81cc877e8c2f619f7f6c45dade4"

LIC_FILES_CHKSUM = "file://COPYING;md5=0918806acfedc3e8c0488f2dd61616dd"

inherit autotools gtk-doc

DEPENDS += "libdrm libpciaccess cairo udev glib-2.0 libxv libx11 libxext libxrandr"
RDEPENDS_${PN} += "bash"

PACKAGECONFIG ??= ""
PACKAGECONFIG[libunwind] = "--with-libunwind,--without-libunwind,libunwind,libunwind"

EXTRA_OECONF = "--disable-nouveau --disable-shader-debugger --disable-dumper"
COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"

gputools_sysroot_preprocess() {
	rm -f ${SYSROOT_DESTDIR}${libdir}/pkgconfig/intel-gen4asm.pc
}
SYSROOT_PREPROCESS_FUNCS += "gputools_sysroot_preprocess"
