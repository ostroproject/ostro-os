SUMMARY = "Iotivity framework and SDK by the Open Interconnect Consortium."
DESCRIPTION = "IoTivity is an open source software framework enabling seamless device-to-device connectivity to address the emerging needs of the Internet of Things."
HOMEPAGE = "https://www.iotivity.org/"
DEPENDS = "boost virtual/gettext chrpath-replacement-native expat openssl"
EXTRANATIVEPATH += "chrpath-native"
SECTION = "libs"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://../git/resource/include/OCApi.h;beginline=1;endline=19;md5=fc5a615cf1dc3880967127bc853b3e0c"
SRC_URI = "git://gerrit.iotivity.org/gerrit/iotivity;protocol=https;branch=0.9.1-dev;name=iotivity \
          "

SRCREV_iotivity = "240655278f95148cc0a585d7155a9a5f81b78873"

S = "${WORKDIR}/git"

inherit scons 

python () {
    IOTIVITY_TARGET_ARCH = d.getVar("TARGET_ARCH", True)
    EXTRA_OESCONS = "TARGET_OS=yocto TARGET_ARCH=" + IOTIVITY_TARGET_ARCH + " RELEASE=1"
    d.setVar("EXTRA_OESCONS", EXTRA_OESCONS)
    d.setVar("IOTIVITY_TARGET_ARCH", IOTIVITY_TARGET_ARCH)
}

IOTIVITY_BIN_DIR = "/opt/iotivity"
IOTIVITY_BIN_DIR_D = "${D}${IOTIVITY_BIN_DIR}"

do_compile_prepend() {
    #Proxy settings go here below.
    export https_proxy=
}

do_install() {
    install -d ${D}${libdir}  

    #Resource Components
    #C++ APIs
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc.so ${D}${libdir}

    #Logger
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger.so ${D}${libdir}
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger_core.so ${D}${libdir}

    #CSDK Shared
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboctbstack.so ${D}${libdir}

    #CSDK Static
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libconnectivity_abstraction.a ${D}${libdir}
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libcoap.a ${D}${libdir} 
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboctbstack.a ${D}${libdir} 

    #Resource C++ Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp   
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp   
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientHQ ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserverHQ ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/threadingsample ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/lightserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/examples/OICMiddle/OICMiddle ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    chrpath -d ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp/*   

    #Resource CSDK Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientcoll ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserver ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserverbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientslow ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserverslow ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocservercoll ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlient ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    chrpath -d ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer/*

    install -d ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/secure/ocserverbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/secure/gen_sec_bin ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/secure/occlientbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    chrpath -d ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure/*
  
    #Resource Tests
    install -d ${IOTIVITY_BIN_DIR_D}/tests/resource    
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/ocrandom/test/randomtests ${IOTIVITY_BIN_DIR_D}/tests/resource/ocrandom_tests
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/unittests/unittests ${IOTIVITY_BIN_DIR_D}/tests/resource/oc_unittests
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/test/stacktests ${IOTIVITY_BIN_DIR_D}/tests/resource/octbstack_tests
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/connectivity/test/catests ${IOTIVITY_BIN_DIR_D}/tests/resource/ca_tests
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/oc_logger/examples/examples_cpp ${IOTIVITY_BIN_DIR_D}/tests/resource/logger_test_cpp
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/oc_logger/examples/examples_c ${IOTIVITY_BIN_DIR_D}/tests/resource/logger_test_c
    install -c -m 444 ${S}/extlibs/gtest/gtest-1.7.0/lib/.libs/libgtest.so ${D}${libdir}
    install -c -m 444 ${S}/extlibs/gtest/gtest-1.7.0/lib/.libs/libgtest_main.so ${D}${libdir}
    chrpath -d ${IOTIVITY_BIN_DIR_D}/tests/resource/*
    chrpath -d ${D}${libdir}/libgtest.so
    chrpath -d ${D}${libdir}/libgtest_main.so

    #Resource headers
    install -d ${D}${includedir}/iotivity/resource/stack/
    install -d ${D}${includedir}/iotivity/resource/logger/
    install -d ${D}${includedir}/iotivity/resource/ocmalloc/
    install -d ${D}${includedir}/iotivity/resource/connectivity/api
    install -d ${D}${includedir}/iotivity/resource/connectivity/external
    install -d ${D}${includedir}/iotivity/resource/connectivity/common
    install -d ${D}${includedir}/iotivity/resource/security/
    install -d ${D}${includedir}/iotivity/resource/ocrandom/
    install -d ${D}${includedir}/iotivity/resource/oc_logger/

    cd ${S}/resource/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/"{}" \;
    cd ${S}/resource/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/"{}" \;

    cd ${S}/resource/csdk/stack/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/stack/"{}" \;
    cd ${S}/resource/csdk/stack/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/stack/"{}" \;

    cd ${S}/resource/csdk/logger/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/logger/"{}" \;
    cd ${S}/resource/csdk/logger/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/logger/"{}" \;

    cd ${S}/resource/csdk/ocmalloc/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/ocmalloc/"{}" \;
    cd ${S}/resource/csdk/ocmalloc/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/ocmalloc/"{}" \;

    cd ${S}/resource/csdk/connectivity/inc && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/connectivity/"{}" \;
    cd ${S}/resource/csdk/connectivity/inc && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/connectivity/"{}" \;

    cd ${S}/resource/csdk/connectivity/external/inc && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/connectivity/external/"{}" \;
    cd ${S}/resource/csdk/connectivity/external/inc && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/connectivity/external/"{}" \;

    cd ${S}/resource/csdk/connectivity/api && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/connectivity/api/"{}" \;
    cd ${S}/resource/csdk/connectivity/api && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/connectivity/api/"{}" \;


    cd ${S}/resource/csdk/connectivity/common/inc && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/connectivity/common/"{}" \;
    cd ${S}/resource/csdk/connectivity/common/inc && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/connectivity/common/"{}" \;

    cd ${S}/resource/csdk/security/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/security/"{}" \;
    cd ${S}/resource/csdk/security/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/security/"{}" \;

    cd ${S}/resource/csdk/ocrandom/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/ocrandom/"{}" \;
    cd ${S}/resource/csdk/ocrandom/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/ocrandom/"{}" \;

    cd ${S}/resource/oc_logger/include && find . -type d -exec install -d ${D}${includedir}/iotivity/resource/oc_logger/"{}" \;
    cd ${S}/resource/oc_logger/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/resource/oc_logger/"{}" \;

    #Service Components
    #PPM
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libppm.a ${D}${libdir} 

    #PPM Implementation (with Cpluff)
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libpmimpl.so ${D}${libdir}

    #MQTT Protocol
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libmosquitto.a ${D}${libdir} 
 
    #Protocol Plugins
    install -d ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-fan
    install -d ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-light     
   
    #MQTT Fan Plugin
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/protocol-plugin/plugins/mqtt-fan/fanserver_mqtt_plugin.so ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-fan
    install -c -m 444 ${S}/service/protocol-plugin/plugins/mqtt-fan/build/linux/plugin.xml ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-fan

    #MQTT Light Plugin
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/protocol-plugin/plugins/mqtt-light/lightserver_mqtt_plugin.so ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-light
    install -c -m 444 ${S}/service/protocol-plugin/plugins/mqtt-light/build/linux/plugin.xml ${IOTIVITY_BIN_DIR_D}/service/protocol-plugins/mqtt-light

    #Protocol Plugin Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/protocol-plugin-apps/sample-app

    #Protocol Plugin Sample App
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/protocol-plugin/sample-app/linux/mqtt/mqttclient ${IOTIVITY_BIN_DIR_D}/examples/service/protocol-plugin-apps/sample-app
    install -c -m 444 ${S}/service/protocol-plugin/sample-app/linux/mqtt/pluginmanager.xml ${IOTIVITY_BIN_DIR_D}/examples/service/protocol-plugin-apps/sample-app

    #Things Manager Framework
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libTGMSDKLibrary.so ${D}${libdir} 
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libTGMSDKLibrary.a ${D}${libdir} 

    #Things Manager Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/configuration
    cd ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/configuration && find . -executable -exec install -c -m 555 "{}" ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/configuration/"{}" \;
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupaction
    cd ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/groupaction && find . -executable -exec install -c -m 555 "{}" ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupaction/"{}" \;
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupsyncaction
    cd ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/groupsyncaction && find . -executable -exec install -c -m 555 "{}" ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupsyncaction/"{}" \;

    #Notification Manager Framework
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/libNotificationManager.a ${D}${libdir} 

    #Notification Manager Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager/
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/notificationmanager ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/sampleconsumer ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/sampleprovider ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager

    #Soft Sensor Manager Core
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libSSMCore.so ${D}${libdir} 
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/libSSMSDK.a ${D}${libdir} 

    #Soft Sensor Plugins
    install -d ${IOTIVITY_BIN_DIR_D}/service/soft-sensor-plugins
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libBMISensor.so ${IOTIVITY_BIN_DIR_D}/service/soft-sensor-plugins
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libDiscomfortIndexSensor.so ${IOTIVITY_BIN_DIR_D}/service/soft-sensor-plugins
    install -c -m 444 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/SoftSensorDescription.xml ${IOTIVITY_BIN_DIR_D}/service/soft-sensor-plugins

    #Soft Sensor Manager Apps
    install -d ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager/
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/HeightSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/SSMTesterApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/THSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/THSensorApp1 ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/WeightSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager

    #Service Headers
    install -d ${D}${includedir}/iotivity/service/protocol-plugin/cpluff
    install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/Common/
    install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/SSMInterface/
    install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/QueryProcessor/
    install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/SensorProcessor/
    install -d ${D}${includedir}/iotivity/service/notification-manager/
    install -d ${D}${includedir}/iotivity/service/things-manager/

    cd ${S}/service/protocol-plugin/plugin-manager/src/ && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/protocol-plugin/"{}" \;

    cd ${S}/service/protocol-plugin/lib/cpluff/libcpluff && find . -type d -exec install -d ${D}${includedir}/iotivity/service/protocol-plugin/cpluff/"{}" \;
    cd ${S}/service/soft-sensor-manager/SSMCore/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/protocol-plugin/cpluff/"{}" \;

    cd ${S}/service/soft-sensor-manager/SSMCore/include && find . -type d -exec install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/"{}" \;
    cd ${S}/service/soft-sensor-manager/SSMCore/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/"{}" \;

    cd ${S}/service/soft-sensor-manager/SDK/cpp/include && find . -type d -exec install -d ${D}${includedir}/iotivity/service/soft-sensor-manager/"{}" \;
    cd ${S}/service/soft-sensor-manager/SDK/cpp/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/"{}" \;

    cd ${S}/service/soft-sensor-manager/SSMCore/src/Common && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/Common/"{}" \;

    cd ${S}/service/soft-sensor-manager/SSMCore/src/SSMInterface && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/SSMInterface/"{}" \;

    cd ${S}/service/soft-sensor-manager/SSMCore/src/QueryProcessor && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/QueryProcessor/"{}" \;

    cd ${S}/service/soft-sensor-manager/SSMCore/src/SensorProcessor && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/soft-sensor-manager/SensorProcessor/"{}" \;

    cd ${S}/service/notification-manager/NotificationManager/include && find . -type d -exec install -d ${D}${includedir}/iotivity/service/notification-manager/"{}" \;
    cd ${S}/service/notification-manager/NotificationManager/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/notification-manager/"{}" \;

    cd ${S}/service/things-manager/sdk/inc && find . -type d -exec install -d ${D}${includedir}/iotivity/service/things-manager/"{}" \;
    cd ${S}/service/things-manager/sdk/inc && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/service/things-manager/"{}" \;

    #CJSON Headers
    install -d ${D}${includedir}/iotivity/extlibs/cjson
    install -d ${D}${includedir}/iotivity/extlibs/timer
    cd ${S}/extlibs/cjson/ && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/extlibs/cjson/"{}" \;
    cd ${S}/extlibs/timer/ && find . -type f -name "*.h" -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/extlibs/timer/"{}" \;
}

#IOTIVITY packages:
#Resource: iotivity-resource, iotivity-resource-dev, iotivity-resource-staticdev, iotivity-resource-dbg
#Resource Samples: iotivity-resource-samples, iotivity-resource-samples-dbg
#Service: iotivity-service, iotivity-service-dev, iotivity-service-staticdev, iotivity-service-dbg
#Service Samples: iotivity-service-samples, iotivity-service-samples-dbg
#Tests: iotivity-tests, iotivity-tests-dbg

FILES_iotivity-resource-dev = "\
                        ${includedir}/iotivity/resource \
                        ${inclidedir}/iotivity/extlibs"
                    
FILES_iotivity-resource-staticdev = "\
                        ${libdir}/libconnectivity_abstraction.a \
                        ${libdir}/liboctbstack.a \
                        ${libdir}/libcoap.a"

FILES_iotivity-resource = "\
                        ${libdir}/liboc.so \
                        ${libdir}/liboctbstack.so \
                        ${libdir}/liboc_logger.so \
                        ${libdir}/liboc_logger_core.so"

FILES_iotivity-resource-dbg = "\
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/git/resource \
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/git/extlibs \
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/git/examples \
                        ${libdir}/.debug/liboc.so \
                        ${libdir}/.debug/liboctbstack.so \
                        ${libdir}/.debug/liboc_logger.so \
                        ${libdir}/.debug/liboc_logger_core.so"

FILES_iotivity-resource-samples-dbg = "\
                      ${IOTIVITY_BIN_DIR}/examples/resource/cpp/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/resource/c/SimpleClientServer/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/resource/c/secure/.debug"

FILES_iotivity-resource-samples = "\
                      ${IOTIVITY_BIN_DIR}/examples/resource"

FILES_iotivity-service-dbg = "\
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/git/service \
                        ${libdir}/.debug"   

FILES_iotivity-service-dev = "\
                        ${includedir}/iotivity/service"

FILES_iotivity-service = "\
    			${libdir}/libpmimpl.so \
                        ${IOTIVITY_BIN_DIR}/service/protocol-plugins/mqtt-fan/fanserver_mqtt_plugin.so \
                        ${IOTIVITY_BIN_DIR}/service/protocol-plugins/mqtt-fan/plugin.xml \
                        ${IOTIVITY_BIN_DIR}/service/protocol-plugins/mqtt-light/lightserver_mqtt_plugin.so \
                        ${IOTIVITY_BIN_DIR}/service/protocol-plugins/mqtt-light/plugin.xml \
			${libdir}/libTGMSDKLibrary.so \
			${libdir}/libSSMCore.so \
			${IOTIVITY_BIN_DIR}/service/soft-sensor-plugins/libBMISensor.so \
			${IOTIVITY_BIN_DIR}/service/soft-sensor-plugins/libDiscomfortIndexSensor.so \
                        ${IOTIVITY_BIN_DIR}/service/soft-sensor-plugins/SoftSensorDescription.xml" 

FILES_iotivity-service-staticdev = "\
			${libdir}/libppm.a \
                        ${libdir}/libmosquitto.a \
                        ${libdir}/libTGMSDKLibrary.a \
                        ${libdir}/libNotificationManager.a \
                        ${libdir}/libSSMSDK.a" 

FILES_iotivity-service-samples-dbg = "\
                      ${IOTIVITY_BIN_DIR}/examples/service/notification-manager/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/protocol-plugin-apps/sample-app/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/soft-sensor-manager/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/things-manager/groupaction/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/things-manager/groupsyncaction/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/things-manager/configuration/.debug"

FILES_iotivity-service-samples = "\
                      ${IOTIVITY_BIN_DIR}/examples/service"

FILES_iotivity-tests-dbg = "\
                      ${libdir}/.debug/libgtest.so \
                      ${libdir}/.debug/libgtest_main.so \
                      ${IOTIVITY_BIN_DIR}/tests/resource/.debug"

FILES_iotivity-tests = "\
                      ${libdir}/libgtest.so \
                      ${libdir}/libgtest_main.so \
                      ${IOTIVITY_BIN_DIR}/tests"

PACKAGES = "iotivity-tests-dbg iotivity-tests iotivity-resource-dbg iotivity-resource iotivity-resource-dev iotivity-resource-staticdev iotivity-resource-samples-dbg iotivity-resource-samples iotivity-service-dbg iotivity-service iotivity-service-dev iotivity-service-staticdev iotivity-service-samples-dbg iotivity-service-samples ${PN}-dev ${PN}"
ALLOW_EMPTY_${PN} = "1"
RDEPENDS_${PN} += "boost"
RRECOMMENDS_${PN} += "iotivity-resource iotivity-service"
RRECOMMENDS_${PN}-dev += "iotivity-resource-dev iotivity-resource-staticdev iotivity-service-dev iotivity-service-staticdev"
RRECOMMENDS_iotivity-resource-dev += "iotivity-resource iotivity-resource-staticdev"
RRECOMMENDS_iotivity-service-dev += "iotivity-service iotivity-service-staticdev iotivity-resource"
RDEPENDS_iotivity-resource-samples += "iotivity-resource" 
RDEPENDS_iotivity-tests += "iotivity-resource"
RDEPENDS_iotivity-service-samples += "iotivity-service iotivity-resource"
RDEPENDS_iotivity-service += "iotivity-resource"
BBCLASSEXTEND = "native nativesdk"

