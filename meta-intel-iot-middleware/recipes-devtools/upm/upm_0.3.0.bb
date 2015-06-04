SUMMARY = "Sensor/Actuator repository for Mraa"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby, Yevgeniy Kiveisha"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e8db6501ed294e65418a933925d12058"

DEPENDS = "nodejs swig-native mraa"

SRC_URI = "git://github.com/intel-iot-devkit/upm.git;protocol=git;rev=2f1bad1c29e66038b469affc984476e880115541 \
           file://0001-adafruitms1438-CMakeLists.txt-stop-RPATH-being-added.patch \
           file://0001-uart-result-of-mraa_uart_get_dev_path-is-a-const.patch"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/upm/examples/"
