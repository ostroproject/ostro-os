SUMMARY = "RMC (Runtime Machine Configuration)"

DESCRIPTION = "RMC project provides a tool and libraries to identify types \
of hardware boards and access any file-based data specific to the board's \
type at runtime in a centralized way. Software (clients) can have a generic \
logic to query board-specific data from RMC without knowing the type of board. \
This make it possible to have a generic software work running on boards which \
require any quirks or customizations at a board or product level. \
"

LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING;md5=838c366f69b72c5df05c96dff79b35f2"

SRC_URI = "git://git.yoctoproject.org/rmc"

SRCREV = "2e38d056f86c0457f3a5ca7ef848545bbb190e47"

S = "${WORKDIR}/git"

DEPENDS_class-target = "gnu-efi"

EXTRA_OEMAKE='RMC_CFLAGS="-Wl,--hash-style=both"'

# from gnu-efi, we should align arch-mapping with it.
def rmc_efi_arch(d):
    import re
    arch = d.getVar("TARGET_ARCH", True)
    if re.match("i[3456789]86", arch):
        return "ia32"
    return arch

do_compile_class-target() {
	oe_runmake
	oe_runmake RMC_EFI_HEADER_PREFIX=${STAGING_INCDIR}/efi RMC_EFI_ARCH="${@rmc_efi_arch(d)}" -f Makefile.efi
}

do_install() {
	oe_runmake RMC_EFI_ARCH="${@rmc_efi_arch(d)}" RMC_INSTALL_PREFIX=${D}/usr install
	oe_runmake RMC_EFI_ARCH="${@rmc_efi_arch(d)}" RMC_INSTALL_PREFIX=${D}/usr -f Makefile.efi install
}

do_install_class-native() {
	install -d ${D}${STAGING_BINDIR_NATIVE}
	install -m 0755 ${S}/src/rmc ${D}${STAGING_BINDIR_NATIVE}
}

BBCLASSEXTEND = "native"
