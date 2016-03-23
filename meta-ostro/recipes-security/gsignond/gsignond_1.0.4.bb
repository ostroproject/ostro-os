SUMMARY = "gSSO daemon"
DESCRIPTION = "GLib-based Single Sign-On daemon"

DEPENDS = "glib-2.0 sqlite3 smack ecryptfs-utils"
RDEPENDS_${PN} = "glib-2.0 sqlite3 ecryptfs-utils"

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

EXTRA_OECONF = "--enable-dbus-type=p2p"

# keychain sysctx must be built in
#EXTRA_OECONF_append = " --enable-keychain=XXX"

SRC_URI = "git://gitlab.com/accounts-sso/gsignond.git;protocol=https"
SRCREV = "b12650ac5b6dd64d9fa59cb01b497eb0a181ec53"

S = "${WORKDIR}/git"

inherit pkgconfig autotools gtk-doc

do_install_append() {
	rm ${D}/usr/lib/libgsignond*.la
	rm ${D}/usr/lib/gsignond/extensions/*.la
	rm ${D}/usr/lib/gsignond/gplugins/*.la
}

FILES_${PN} = " \
	/usr/bin/gsignond \
	/usr/lib/libgsignond*.so* \
	/usr/lib/gsignond/extensions/*.so \
	/usr/lib/gsignond/gplugins/*.so \
	/usr/lib/gsignond/pluginloaders \
	/etc/gsignond.conf \
	/usr/share/dbus-1/interfaces/com.google.code.AccountsSSO.* \
	"
