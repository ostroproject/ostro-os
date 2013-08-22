SUMMARY = "Gummiboot is a simple UEFI boot manager which executes configured EFI images."
HOMEPAGE = "http://freedesktop.org/wiki/Software/gummiboot"

LICENSE = "LGPLv2.1"
LIC_FILES_CHKSUM = "file://LICENSE;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "gnu-efi util-linux"

inherit autotools
inherit deploy

PV = "35+git${SRCPV}"
PR = "r0"
SRCREV = "6feb7d971f79e88ed395637390d58404fba5f3c3"
SRC_URI = "git://anongit.freedesktop.org/gummiboot"

S = "${WORKDIR}/git"

EXTRA_OECONF = "--disable-biostest --with-efi-includedir=${STAGING_INCDIR} \
	        --with-efi-ldsdir=${STAGING_LIBDIR} \
		--with-efi-libdir=${STAGING_LIBDIR}"

do_deploy () {
        install ${S}/gummiboot*.efi ${DEPLOYDIR}/
}
addtask deploy before do_build after do_compile
