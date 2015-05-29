FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment.
SRC_URI_append = "\
                file://sensors.cfg \
                file://nfc.cfg \
                "
