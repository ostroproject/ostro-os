SUMMARY = "OAuth plugin for gSSO"
DESCRIPTION = "Plugin implementing OAuth functionality for gSSO framework"

DEPENDS = "glib-2.0 gsignond json-glib gnutls libsoup-2.4"
RDEPENDS_${PN} = "glib-2.0 gsignond json-glib gnutls libsoup-2.4"

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

SRC_URI = "git://gitlab.com/accounts-sso/gsignond-plugin-oa.git;protocol=https"
SRCREV = "af3586017891ac8bdc7d81f519cbc8e9025f943e"

S = "${WORKDIR}/git"

inherit pkgconfig autotools gtk-doc

do_install_append() {
	rm ${D}/usr/lib/gsignond/gplugins/*.la
}

FILES_${PN} = " \
	/usr/lib/gsignond/gplugins/liboauth.so \
	"
