SUMMARY = "swupd sofware update from Clear Linux - server component"
LICENSE = "GPL-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=04d0b48662817042d80393e7511fa41b \
                    file://bsdiff/LICENSE;md5=0dbe7a50f028269750631fcbded3846a"

DEPENDS = "file xz glib-2.0 zlib bzip2 tar rsync openssl"

SRC_URI = "\
    https://download.clearlinux.org/releases/5940/clear/source/SRPMS/${BPN}-${PV}-4.src.rpm;extract=${BP}.tar.gz \
    file://0001-Add-option-S-to-take-the-state-data-dir-as-an-argume.patch \
    file://0002-Add-system_argv-helper-for-safer-calls-to-system-uti.patch \
    file://0003-Add-configure-option-to-re-enable-config-files-in-ma.patch \
    file://0004-Fix-regression-that-introduced-a-directory-named.patch \
    file://0005-xattrs.c-Avoid-freeing-dangling-pointers.patch \
    file://0006-Always-use-xattrs-when.patch \
    file://0007-Clean-up-tar-options-drop-a-for-the-extract-mode.patch \
    file://0008-Clean-up-tar-commands-always-put-files-after-options.patch \
    file://0009-Add-compatibility-with-libarchive-s-bsdtar-command.patch \
    file://fullfiles.c-work-around-pseudo-bug.patch \
"

SRC_URI[md5sum] = "14f25677b5a4f0b33785910b03860939"
SRC_URI[sha256sum] = "c2d0e595444fe198c4092dd83d20a929fd1402a13b66b410b76677ed3a993d99"

inherit autotools

EXTRA_OECONF = "--enable-bzip2 --enable-lzma --disable-stateless --enable-bsdtar"

# safer-calls-to-system-utilities.patch uses for loop initial declaration
CFLAGS_append = " -std=c99"

do_install_append () {
    mkdir -p ${D}${sysconfdir}/swupd-certs
    install -m 0755 ${S}/test/signature/* ${D}${sysconfdir}/swupd-certs/
}

# Work around lack of "RPROVIDES = bsdtar-native" in libarchive-native.
RDEPENDS_${PN}_class-target = "bsdtar rsync"
RDEPENDS_${PN}_class-native = "libarchive rsync"

BBCLASSEXTEND = "native"
