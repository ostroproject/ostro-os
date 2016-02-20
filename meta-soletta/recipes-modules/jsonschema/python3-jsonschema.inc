DESCRIPTION = "An implementation of JSON-Schema validation for Python"
HOMEPAGE = "http://pypi.python.org/pypi/jsonschema"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=7a60a81c146ec25599a3e1dabb8610a8"

PR = "r0"
SRCNAME = "jsonschema"

SRC_URI = "http://pypi.python.org/packages/source/j/${SRCNAME}/${SRCNAME}-${PV}.zip"

SRC_URI[md5sum] = "f645c88123189976058fcf550c02e50f"
SRC_URI[sha256sum] = "acf1e360b4682d64ba6acc35dbc65d81d9bde68a291a97f14f16f4282733f5a4"

S = "${WORKDIR}/${SRCNAME}-${PV}"

inherit setuptools3
