SUMMARY = "Ostro OS Software updates package groups"
LICENSE = "MIT"
PR = "r1"

inherit packagegroup

SUMMARY_${PN} = "Ostro OS Software updates stack"

RDEPENDS_${PN} = "\
    tar \
    swupd-client \
    clr-systemd-config \
    "
