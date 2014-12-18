DESCRIPTION = "A UEFI OS loader"
LICENSE = "BSD-2-Clause"
LIC_FILES_CHKSUM = "file://efilinux.h;beginline=5;endline=31;md5=2316abda893ef24e6cd55cef33aa0edd"

DEPENDS = "gnu-efi"

inherit deploy

SRCREV = "75b62111f83dab433e901c1a7b0f05e058aa29de"
PV = "1.0+git${SRCPV}"
PR = "r0"

SRC_URI = "git://git.kernel.org/pub/scm/boot/efilinux/efilinux.git"

S = "${WORKDIR}/git"

COMPATIBLE_HOST = '(x86_64|i.86).*-(linux|freebsd.*)'

EXTRA_OEMAKE = "INCDIR=${STAGING_INCDIR} LIBDIR=${STAGING_LIBDIR}"

# syslinux uses $LD for linking, strip `-Wl,' so it can work
export LDFLAGS = "`echo $LDFLAGS | sed 's/-Wl,//g'`"

do_deploy () {
        install ${S}/efilinux.efi ${DEPLOYDIR}/efilinux.efi
}
addtask deploy before do_build after do_compile

