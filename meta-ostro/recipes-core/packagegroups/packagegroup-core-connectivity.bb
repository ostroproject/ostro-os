SUMMARY = "Ostro OS Connectivity package groups"
LICENSE = "MIT"
PR = "r1"

inherit packagegroup

SUMMARY_${PN} = "Ostro OS Connectivity stack"
RDEPENDS_${PN} = "\
    bluez5 \
    bluez5-obex \
    connman \
    "
