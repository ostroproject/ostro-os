SUMMARY = "QA Tests"
LICENSE = "MIT"

inherit packagegroup

RDEPENDS_${PN} = " \
    example-app-c \
    example-app-node \
    example-app-python \
    bad-groups-app \
    appfw-test-app \
"
