SUMMARY = "test_get_sensor_list"
DESCRIPTION = "Test get_sensor_list method of IoT sensor framework"
HOMEPAGE = "http://ostroproject.org/"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

DEPENDS = " sensord"
 
SRC_URI = "file://test_get_sensor_list_by_type.c \
file://test_get_sensor_by_id.c \
file://test_get_sensor_name_by_id.c \
file://test_get_sensor_type_by_id.c \
file://test_get_sensor_status_by_id.c \
file://test_sensor_type_is_supported.c \
file://test_get_default_sensor_and_manipulation.c \
file://test_sensor_register_unregister_misc.c \
file://test_sensor_register_duplicated.c \
file://test_set_sensor_data_after_unregister.c \
file://test_get_all_installed_sensor.c \
file://test_get_all_installed_sensor_count.c \
file://test_get_sensor_count_by_type.c \
file://test_get_default_sensor_by_type.c \
file://test_connect_sensor_already_connected.c \
file://test_disconnect_unconnected_sensor.c \
file://test_disconnect_sensor_invalid_id.c \
file://test_get_sensor_type_list.c \
file://test_get_sensor_type_list_incorrect_count.c \
file://test_unregister_unregistered_sensor.c \
file://test_get_sensor_data_by_id.c \
file://test_set_sensor_data_by_id.c \
file://test_get_sensor_raw_data_by_id.c \
file://test_sensor_framework_ready.c \
file://test_connect_sensor_maximum_times.c \
file://test_stress_connect_disconnect_sensor.c \
file://test_stress_set_get_data_of_sensor.c \
file://test_get_data_of_unconnected_sensor.c "

S = "${WORKDIR}"

do_compile() {
    ${CC} test_get_sensor_list_by_type.c -o test_get_sensor_list_by_type -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_by_id.c -o test_get_sensor_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_name_by_id.c -o test_get_sensor_name_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_type_by_id.c -o test_get_sensor_type_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_status_by_id.c -o test_get_sensor_status_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_sensor_type_is_supported.c -o test_sensor_type_is_supported -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_default_sensor_and_manipulation.c -o test_get_default_sensor_and_manipulation -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_sensor_register_unregister_misc.c -o test_sensor_register_unregister_misc -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_sensor_register_duplicated.c -o test_sensor_register_duplicated -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_set_sensor_data_after_unregister.c -o test_set_sensor_data_after_unregister -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_all_installed_sensor.c -o test_get_all_installed_sensor -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_all_installed_sensor_count.c -o test_get_all_installed_sensor_count -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_count_by_type.c -o test_get_sensor_count_by_type -I${STAGING_INCDIR}/sensor -lsensor	
    ${CC} test_get_default_sensor_by_type.c -o test_get_default_sensor_by_type -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_connect_sensor_already_connected.c -o test_connect_sensor_already_connected -I${STAGING_INCDIR}/sensor -lsensor	
    ${CC} test_disconnect_unconnected_sensor.c -o test_disconnect_unconnected_sensor -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_disconnect_sensor_invalid_id.c -o test_disconnect_sensor_invalid_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_type_list.c -o test_get_sensor_type_list -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_type_list_incorrect_count.c -o test_get_sensor_type_list_incorrect_count -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_unregister_unregistered_sensor.c -o test_unregister_unregistered_sensor -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_data_by_id.c -o test_get_sensor_data_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_set_sensor_data_by_id.c -o test_set_sensor_data_by_id -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_get_sensor_raw_data_by_id.c -o test_get_sensor_raw_data_by_id -I${STAGING_INCDIR}/sensor -lsensor 
    ${CC} test_sensor_framework_ready.c -o test_sensor_framework_ready -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_connect_sensor_maximum_times.c -o test_connect_sensor_maximum_times -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_stress_connect_disconnect_sensor.c -o test_stress_connect_disconnect_sensor -I${STAGING_INCDIR}/sensor -lsensor
    ${CC} test_stress_set_get_data_of_sensor.c -o test_stress_set_get_data_of_sensor -I${STAGING_INCDIR}/sensor -lsensor 
    ${CC} test_get_data_of_unconnected_sensor.c -o test_get_data_of_unconnected_sensor -I${STAGING_INCDIR}/sensor -lsensor
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 test_get_sensor_list_by_type ${D}${bindir}
    install -m 0755 test_get_sensor_by_id ${D}${bindir}
    install -m 0755 test_get_sensor_name_by_id ${D}${bindir}
    install -m 0755 test_get_sensor_type_by_id ${D}${bindir}
    install -m 0755 test_get_sensor_status_by_id ${D}${bindir}
    install -m 0755 test_sensor_type_is_supported ${D}${bindir}
    install -m 0755 test_get_default_sensor_and_manipulation ${D}${bindir}
    install -m 0755 test_sensor_register_unregister_misc ${D}${bindir}
    install -m 0755 test_sensor_register_duplicated ${D}${bindir}
    install -m 0755 test_set_sensor_data_after_unregister ${D}${bindir}
    install -m 0755 test_get_all_installed_sensor ${D}${bindir}
    install -m 0755 test_get_all_installed_sensor_count ${D}${bindir}
    install -m 0755 test_get_sensor_count_by_type ${D}${bindir}
    install -m 0755 test_connect_sensor_already_connected ${D}${bindir}
    install -m 0755 test_disconnect_unconnected_sensor ${D}${bindir}
    install -m 0755 test_disconnect_sensor_invalid_id ${D}${bindir}
    install -m 0755 test_get_sensor_type_list ${D}${bindir}
    install -m 0755 test_get_sensor_type_list_incorrect_count ${D}${bindir}
    install -m 0755 test_unregister_unregistered_sensor ${D}${bindir}
    install -m 0755 test_get_sensor_data_by_id ${D}${bindir}
    install -m 0755 test_set_sensor_data_by_id ${D}${bindir}
    install -m 0755 test_get_sensor_raw_data_by_id ${D}${bindir}
    install -m 0755 test_sensor_framework_ready ${D}${bindir}
    install -m 0755 test_connect_sensor_maximum_times ${D}${bindir}
    install -m 0755 test_stress_connect_disconnect_sensor ${D}${bindir}
    install -m 0755 test_stress_set_get_data_of_sensor ${D}${bindir}
    install -m 0755 test_get_data_of_unconnected_sensor ${D}${bindir}

}

inherit copybin
TARGET_FILES += "${WORKDIR}/test_get_sensor_type_by_id ${WORKDIR}/test_connect_sensor_already_connected ${WORKDIR}/test_get_all_installed_sensor_count ${WORKDIR}/test_get_sensor_count_by_type ${WORKDIR}/test_get_all_installed_sensor ${WORKDIR}/test_get_sensor_list_by_type ${WORKDIR}/test_get_sensor_by_id ${WORKDIR}/test_get_default_sensor_by_type ${WORKDIR}/test_get_sensor_status_by_id ${WORKDIR}/test_disconnect_sensor_invalid_id ${WORKDIR}/test_disconnect_unconnected_sensor ${WORKDIR}/test_get_sensor_name_by_id ${WORKDIR}/test_get_sensor_type_list ${WORKDIR}/test_get_sensor_type_list_incorrect_count ${WORKDIR}/test_unregister_unregistered_sensor ${WORKDIR}/test_sensor_register_unregister_misc ${WORKDIR}/test_get_sensor_data_by_id ${WORKDIR}/test_set_sensor_data_by_id ${WORKDIR}/test_sensor_type_is_supported ${WORKDIR}/test_get_default_sensor_and_manipulation ${WORKDIR}/test_set_sensor_data_after_unregister ${WORKDIR}/test_sensor_register_duplicated ${WORKDIR}/test_get_sensor_raw_data_by_id ${WORKDIR}/test_sensor_framework_ready ${WORKDIR}/test_connect_sensor_maximum_times ${WORKDIR}/test_stress_connect_disconnect_sensor ${WORKDIR}/test_stress_set_get_data_of_sensor ${WORKDIR}/test_get_data_of_unconnected_sensor"
