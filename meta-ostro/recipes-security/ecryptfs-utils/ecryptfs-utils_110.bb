SUMMARY = "Library and utilities for managing eCryptFS filesystems"
DESCRIPTION = "eCryptfs is a POSIX-compliant enterprise cryptographic stacked filesystem for Linux. eCryptfs stores cryptographic metadata in the header of each file, so that encrypted files can be copied between hosts; the file will be decrypted with the proper key in the Linux kernel keyring."

# by default ecryptfs-utils builds against NSS, but can be switched to gcrypt
DEPENDS = "virtual/gettext glib-2.0 keyutils nss"
RDEPENDS_${PN} = "keyutils nss"

LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://COPYING;md5=8ca43cbc842c2336e835926c2166c28b"

SRC_URI = "https://launchpad.net/ecryptfs/trunk/110/+download/ecryptfs-utils_110.orig.tar.gz"
SRC_URI[md5sum] = "3205ce74b2236ee7fe94509dc0fe3660"

EXTRA_OECONF = "--disable-pywrap"

PACKAGECONFIG ??= "openssl pkcs11-helper ${@bb.utils.contains('DISTRO_FEATURES', 'pam', 'pam', '', d)}"
PACKAGECONFIG[openssl] = "--enable-openssl,--disable-openssl,openssl"
PACKAGECONFIG[pkcs11-helper] = "--enable-pkcs11-helper,--disable-pkcs11-helper,pkcs11-helper"
PACKAGECONFIG[pam] = "--enable-pam,--disable-pam,libpam"

inherit pkgconfig autotools

FILES_${PN} = " \
	/sbin/*.ecryptfs* \
	/usr/bin/ecryptfs* \
	/usr/share/ecryptfs-utils \
	/lib/security/pam_ecryptfs.so \
	/usr/lib/libecryptfs.so* \
	/usr/lib/ecryptfs \
	"

