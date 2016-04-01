SUMMARY = "Sensor/Actuator repository for Mraa"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby, Yevgeniy Kiveisha"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=d1cc191275d6a8c5ce039c75b2b3dc29"

DEPENDS = "nodejs swig-native mraa"

SRC_URI = "git://github.com/intel-iot-devkit/upm.git;protocol=git;rev=655ccee9afd259bff1773e9e8aea860f6e06b69f \
"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/upm/examples/"

PACKAGECONFIG ??= "python nodejs"
PACKAGECONFIG[python] = "-DBUILDSWIGPYTHON=OFF, -DBUILDSWIGPYTHON=OFF, swig-native python, python-mraa"
PACKAGECONFIG[nodejs] = "-DBUILDSWIGNODE=OFF, -DBUILDSWIGNODE=OFF, swig-native nodejs, node-mraa"
