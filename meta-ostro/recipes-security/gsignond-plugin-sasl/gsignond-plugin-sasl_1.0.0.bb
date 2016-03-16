SUMMARY = "SASL plugin for gSSO"
DESCRIPTION = "Plugin implementing SASL functionality for gSSO framework"

DEPENDS = "glib-2.0 gsignond libgsasl"
RDEPENDS_${PN} = "glib-2.0 gsignond libgsasl"

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

SRC_URI = "git://gitlab.com/accounts-sso/gsignond-plugin-sasl.git;protocol=https"
SRCREV = "de3630891e664de32bd77e34977b237785809e8d"

S = "${WORKDIR}/git"

inherit pkgconfig autotools gtk-doc

do_install_append() {
	rm ${D}/usr/lib/gsignond/gplugins/*.la
}

FILES_${PN} = " \
	/usr/lib/gsignond/gplugins/libsasl.so \
	"
