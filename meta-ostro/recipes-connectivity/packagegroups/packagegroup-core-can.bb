SUMMARY = "Ostro OS Connectivity package groups"
LICENSE = "MIT"
PR = "r1"

inherit packagegroup

SUMMARY_${PN} = "Ostro OS CAN stack"
RDEPENDS_${PN} = "\
    can-utils \
    can-init-scripts \
    "
