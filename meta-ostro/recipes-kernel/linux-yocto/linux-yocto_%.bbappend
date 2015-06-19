FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment.
SRC_URI_append = "\
                file://sensors.cfg \
                file://nfc.cfg \
                file://usb-serial.cfg \
                file://wireless.cfg \
                "
