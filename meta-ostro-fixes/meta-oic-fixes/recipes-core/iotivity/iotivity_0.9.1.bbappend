# Upstream-Status: Submitted [directly to maintainer]

SRC_URI += "file://cereal-use-dist.patch"

FILESEXTRAPATHS_prepend := "${THISDIR}:"
DEPENDS_append = " cereal util-linux"

python_append () {
	EXTRA_OESCONS = "TARGET_OS=yocto TARGET_ARCH=" + IOTIVITY_TARGET_ARCH + " RELEASE=1 TEST=0"
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
