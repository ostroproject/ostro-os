SUMMARY = "Libraries for producing EFI binaries"
HOMEPAGE = "http://sourceforge.net/projects/gnu-efi/"
SECTION = "devel"
LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://debian/copyright;md5=5fb358a180f484b285b0d99acdc29666"

PR = "r3"

SRCREV = "74"

SRC_URI = "http://downloads.sourceforge.net/gnu-efi/gnu-efi_3.0m.orig.tar.gz \
           file://cross-compile-support.patch \
           file://parallel-make.patch \
           file://parallel-make-archives.patch \
          "
SRC_URI[md5sum] = "d0a21125aee56c0c7291ad260e916cb3"
SRC_URI[sha256sum] = "b7fb638f5ec8faa6edebe54beb90957f01ccccf70a2a948d1b58b834c8d7f86d"

COMPATIBLE_HOST = "(x86_64.*|i.86.*)-linux"

S = "${WORKDIR}/gnu-efi-3.0"

def gnu_efi_arch(d):
    import re
    tarch = d.getVar("TARGET_ARCH", True)
    if re.match("i[3456789]86", tarch):
        return "ia32"
    return tarch

EXTRA_OEMAKE = "'ARCH=${@gnu_efi_arch(d)}' 'CC=${CC}' 'AS=${AS}' 'LD=${LD}' 'AR=${AR}' \
                'RANLIB=${RANLIB}' 'OBJCOPY=${OBJCOPY}' \
                "

do_install() {
    oe_runmake install INSTALLROOT="${D}${prefix}"
}

FILES_${PN} += "${libdir}/*.lds"
