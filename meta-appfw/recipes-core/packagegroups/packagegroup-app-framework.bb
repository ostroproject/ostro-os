SUMMARY = "Application framework middleware components"
LICENSE = "MIT"

inherit packagegroup

RDEPENDS_${PN} = " \
    iot-app-fw \
    iot-app-fw-launcher \
    iot-app-fw-package-manager \
"
