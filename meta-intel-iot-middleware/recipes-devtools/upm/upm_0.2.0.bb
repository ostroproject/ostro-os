SUMMARY = "Sensor/Actuator repository for Mraa"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby, Yevgeniy Kiveisha"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e8db6501ed294e65418a933925d12058"

DEPENDS = "nodejs swig-native mraa"

SRC_URI = "git://github.com/intel-iot-devkit/upm.git;protocol=git;rev=78182278ccc0c268864ec7e14b6b58f02b3ee668 \
           file://0001-adafruitms1438-CMakeLists.txt-stop-RPATH-being-added.patch"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/upm/examples/"
