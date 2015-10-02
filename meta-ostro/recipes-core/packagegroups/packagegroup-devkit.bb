SUMMARY = "IoT DevKit related components"
LICENSE = "MIT"

inherit packagegroup

RDEPENDS_${PN} = " \
    hid-api \
    iotkit-agent \
    linuxptp \
    mraa \
    tempered \
    upm \
"
