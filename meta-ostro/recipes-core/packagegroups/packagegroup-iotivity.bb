SUMMARY = "Iotivity middleware components"
LICENSE = "MIT"

inherit packagegroup

# TODO: are all of these really needed in a minimal image?
RDEPENDS_${PN} = " \
    iotivity \
    iotivity-simple-client \
    iotivity-resource \
    iotivity-resource-samples \
"
