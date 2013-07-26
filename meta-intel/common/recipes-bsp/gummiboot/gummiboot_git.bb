SUMMARY = "Gummiboot is a simple UEFI boot manager which executes configured EFI images."
HOMEPAGE = "http://freedesktop.org/wiki/Software/gummiboot"

LICENSE = "LGPLv2.1"
LIC_FILES_CHKSUM = "file://LICENSE;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "gnu-efi util-linux"

inherit autotools
inherit deploy

PV = "33"
PR = "r0"
SRCREV = "cbc63ae9d6161fe6412f0457e72a276f5acb6e2a"
SRC_URI = "git://anongit.freedesktop.org/gummiboot \
           file://0001-configure.ac-Add-option-to-disable-configuring-the-B.patch \
           file://0002-configure.ac-Use-AC_CHECK_HEADER-to-detect-the-efi-i.patch \
           file://0003-Makefile.am-Allow-for-user-override-of-EFI-include-d.patch \
           file://0004-configure.ac-Allow-for-more-than-just-i686-for-ia32.patch \
           file://0005-Auto-detect-both-x64-and-ia32-boot-.efi-payloads.patch \
           file://0006-Add-32-bit-compatible-rdtsc-asm.patch"

S = "${WORKDIR}/git"

EXTRA_OECONF = "--disable-biostest"
EXTRA_OEMAKE = "INCDIR=${STAGING_INCDIR} GNUEFI_LDS_DIR=${STAGING_LIBDIR} \
	        GNUEFI_LIBS='-L ${STAGING_LIBDIR}'"

do_deploy () {
        install ${S}/gummiboot*.efi ${DEPLOYDIR}/
}
addtask deploy before do_build after do_compile
