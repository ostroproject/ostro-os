FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\
    file://bluez-enable-le-gatt-interfaces.patch \
"

DEPENDS += " icu"
