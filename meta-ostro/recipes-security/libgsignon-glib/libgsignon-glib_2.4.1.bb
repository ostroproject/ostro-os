SUMMARY = "gSSO client library"
DESCRIPTION = "GLib-based client library for Single Sign-On daemon"

DEPENDS = "glib-2.0"
RDEPENDS_${PN} = "glib-2.0"

LICENSE = "LGPLv2.1"
LIC_FILES_CHKSUM = "file://COPYING;md5=243b725d71bb5df4a1e5920b344b86ad"

EXTRA_OECONF = "--enable-dbus-type=p2p --enable-vala=no --enable-introspection=no --disable-python"

SRC_URI = "git://gitlab.com/accounts-sso/libgsignon-glib.git;protocol=https"
SRCREV = "9934e8fd036675d76ea751d2cea45521ff090ce8"

S = "${WORKDIR}/git"

inherit pkgconfig autotools gtk-doc

do_install_append() {
	rm -rf ${D}/usr/bin
}

FILES_${PN} = " \
	/usr/lib/libgsignon-glib* \
	"
