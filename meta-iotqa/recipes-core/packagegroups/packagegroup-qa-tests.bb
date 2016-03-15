SUMMARY = "QA Tests"
LICENSE = "MIT"

inherit packagegroup

RDEPENDS_${PN} = " \
    example-app-c \
    example-app-node \
    bad-groups-app \
"
