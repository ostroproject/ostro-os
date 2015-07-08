SUMMARY = "test_get_sensor_list"
DESCRIPTION = "Test get_sensor_list method of IoT sensor framework"
HOMEPAGE = "http://ostroproject.org/"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
DEPENDS = " sensord "
 
SRC_URI = "file://test_get_sensor_type_by_id.c \
file://test_connect_sensor_already_connected.c "

S = "${WORKDIR}"

do_compile() {
    ${CC} test_get_sensor_type_by_id.c -o test_get_sensor_type_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_connect_sensor_already_connected.c -o test_connect_sensor_already_connected -I${STAGING_INCDIR}/sensor -lsensor
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 test_get_sensor_type_by_id ${D}${bindir}
    install -m 0755 test_connect_sensor_already_connected ${D}${bindir}
}
