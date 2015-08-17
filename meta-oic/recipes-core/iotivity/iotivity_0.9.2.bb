SUMMARY = "Iotivity framework and SDK by the Open Interconnect Consortium."
DESCRIPTION = "IoTivity is an open source software framework enabling seamless device-to-device connectivity to address the emerging needs of the Internet of Things."
HOMEPAGE = "https://www.iotivity.org/"
DEPENDS = "boost virtual/gettext chrpath-replacement-native expat openssl util-linux curl"
EXTRANATIVEPATH += "chrpath-native"
SECTION = "libs"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://resource/include/OCApi.h;beginline=1;endline=19;md5=fc5a615cf1dc3880967127bc853b3e0c"
SRC_URI = "https://downloads.iotivity.org/0.9.2/iotivity-0.9.2.tar.gz;name=iotivity \
           git://github.com/01org/tinycbor.git;protocol=https;name=cbor;destsuffix=iotivity-0.9.2/extlibs/tinycbor/tinycbor \
           https://googletest.googlecode.com/files/gtest-1.7.0.zip;name=gtest \
           https://github.com/dascandy/hippomocks/archive/2f40aa11e31499432283b67f9d3449a3cd7b9c4d.zip \
           file://arch.patch;patch=1 \
          "	  
SRC_URI[iotivity.md5sum] = "cf32e10a8f355fe1327db98ffc9a6173"
SRC_URI[iotivity.sha256sum] = "abe078cc75f2094fe21266aedbc7a890625635d1db289a4a99947b6e4ffdf21a"
SRCREV_cbor = "47a78569c082905572c7a7c12b5ddbc8248b46e0"
SRC_URI[gtest.md5sum] = "2d6ec8ccdf5c46b05ba54a9fd1d130d7"
SRC_URI[gtest.sha256sum] = "247ca18dd83f53deb1328be17e4b1be31514cedfc1e3424f672bf11fd7e0d60d"
SRC_URI[md5sum] = "d54eb32ea45d6d2b624c87e117f6c0cf"
SRC_URI[sha256sum] = "0f57fa8cc1e2f76f1769891a266f2715295baf2333d504f628c674767646ac48"

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
    if [ ! -d "${S}/extlibs/gtest/gtest-1.7.0/" ]; then    
        mv ${WORKDIR}/gtest-1.7.0 ${S}/extlibs/gtest/
    fi
    if [ ! -d "${S}/extlibs/hippomocks-master/" ]; then        
        mv ${WORKDIR}/hippomocks-2f40aa11e31499432283b67f9d3449a3cd7b9c4d ${S}/extlibs/hippomocks-master
    fi
}

make_dir() {
    install -d $1
}

copy_file() {
    install -c -m 444 $1 $2
}

copy_exec() {
    install -c -m 555 $1 $2
}

copy_file_recursive() {
    cd $1 && find . -type d -exec install -d $2/"{}" \;
    cd $1 && find . -type f -exec install -c -m 444 "{}" $2/"{}" \;
}

copy_exec_recursive() {
    cd $1 && find . -executable -exec install -c -m 555 "{}" $2/"{}" \;
}

do_install() {
    make_dir ${D}${libdir}
    #Resource
    #C++ APIs
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc.so ${D}${libdir}

    #Logger
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger_core.so ${D}${libdir}

    #CSDK Shared
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboctbstack.so ${D}${libdir}

    #CSDK Static
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libconnectivity_abstraction.a ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libcoap.a ${D}${libdir} 
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboctbstack.a ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libc_common.a ${D}${libdir}     
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libocsrm.a ${D}${libdir}     

    #Resource C++ Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/oic_svr_db_client.json ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/oic_svr_db_server.json ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp    
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp   
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp   
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientHQ ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserverHQ ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/groupclient ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/threadingsample ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp  
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/lightserver ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/examples/OICMiddle/OICMiddle ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp   
    chrpath -d `find ${IOTIVITY_BIN_DIR_D}/examples/resource/cpp/ -type f | grep -v ".json"`    

    #Resource CSDK Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientcoll ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserver ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserverbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientslow ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocserverslow ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlientbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/ocservercoll ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/SimpleClientServer/occlient ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer
    chrpath -d ${IOTIVITY_BIN_DIR_D}/examples/resource/c/SimpleClientServer/*

    make_dir ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/secure/ocserverbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/samples/linux/secure/occlientbasicops ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/oic_svr_db_client.json ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/oic_svr_db_server.json ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure     
    chrpath -d `find ${IOTIVITY_BIN_DIR_D}/examples/resource/c/secure/ -type f | grep -v ".json"`
    
    #Resource Tests
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/resource    
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/ocrandom/test/randomtests ${IOTIVITY_BIN_DIR_D}/tests/resource/ocrandom_tests
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/unittests/unittests ${IOTIVITY_BIN_DIR_D}/tests/resource/oc_unittests
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/stack/test/stacktests ${IOTIVITY_BIN_DIR_D}/tests/resource/octbstack_tests
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/csdk/connectivity/test/catests ${IOTIVITY_BIN_DIR_D}/tests/resource/ca_tests
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/oc_logger/examples/examples_cpp ${IOTIVITY_BIN_DIR_D}/tests/resource/logger_test_cpp
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/oc_logger/examples/examples_c ${IOTIVITY_BIN_DIR_D}/tests/resource/logger_test_c
    copy_file ${S}/extlibs/gtest/gtest-1.7.0/lib/.libs/libgtest.so ${D}${libdir}
    copy_file ${S}/extlibs/gtest/gtest-1.7.0/lib/.libs/libgtest_main.so ${D}${libdir}
    chrpath -d ${IOTIVITY_BIN_DIR_D}/tests/resource/*
    chrpath -d ${D}${libdir}/libgtest.so
    chrpath -d ${D}${libdir}/libgtest_main.so

    #Resource headers
    make_dir ${D}${includedir}/iotivity/resource/stack/
    make_dir ${D}${includedir}/iotivity/resource/logger/
    make_dir ${D}${includedir}/iotivity/resource/connectivity/api
    make_dir ${D}${includedir}/iotivity/resource/connectivity/external
    make_dir ${D}${includedir}/iotivity/resource/connectivity/common
    make_dir ${D}${includedir}/iotivity/resource/security/
    make_dir ${D}${includedir}/iotivity/resource/ocrandom/
    make_dir ${D}${includedir}/iotivity/resource/oc_logger/

    copy_file_recursive ${S}/resource/include ${D}${includedir}/iotivity/resource   
    copy_file_recursive ${S}/resource/csdk/stack/include ${D}${includedir}/iotivity/resource/stack
    copy_file_recursive ${S}/resource/csdk/logger/include  ${D}${includedir}/iotivity/resource/logger
    copy_file_recursive ${S}/resource/csdk/connectivity/inc  ${D}${includedir}/iotivity/resource/connectivity
    copy_file_recursive ${S}/resource/csdk/connectivity/external/inc ${D}${includedir}/iotivity/resource/connectivity/external
    copy_file_recursive ${S}/resource/csdk/connectivity/api ${D}${includedir}/iotivity/resource/connectivity/api
    copy_file_recursive ${S}/resource/csdk/connectivity/common/inc ${D}${includedir}/iotivity/resource/connectivity/common
    copy_file_recursive ${S}/resource/csdk/security/include  ${D}${includedir}/iotivity/resource/security
    copy_file_recursive ${S}/resource/csdk/ocrandom/include ${D}${includedir}/iotivity/resource/ocrandom
    copy_file_recursive ${S}/resource/oc_logger/include ${D}${includedir}/iotivity/resource/oc_logger
    copy_file ${S}/resource/c_common/oic_string/include/oic_string.h ${D}${includedir}/iotivity/resource
    copy_file ${S}/resource/c_common/oic_malloc/include/oic_malloc.h ${D}${includedir}/iotivity/resource

    #Service Components
    #Resource Encapsulation Framework
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_common.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_server.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_container.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libHueBundle.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libSoftSensorBundle.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_client.a ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_server.a ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_container.a ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/librcs_common.a ${D}${libdir}    

    #Resource Encapsulation Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-container
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/sampleResourceClient ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/sampleResourceServer ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/resourceContainer/ContainerSampleClient ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-container
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/resourceContainer/ContainerSample ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-container   

    #Resource Encapsulation Tests
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/service/resource-encapsulation/resource-broker
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/service/resource-encapsulation/resource-cache
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/service/resource-encapsulation/common
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/service/resource-encapsulation/server-builder
    make_dir ${IOTIVITY_BIN_DIR_D}/tests/service/resource-encapsulation/resource-container    
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/unittests/ResourceClientTest ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/resourceBroker/unittest/broker_test ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-broker
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/resourceCache/unittests/cache_test ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-cache
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/common/rcs_common_test ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/common
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/serverBuilder/rcs_server_test ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/server-builder
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/resource-encapsulation/src/resourceContainer/unittests/container_test ${IOTIVITY_BIN_DIR_D}/examples/service/resource-encapsulation/resource-container
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libTestBundle.so ${D}${libdir}     

    #Things Manager Framework
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libTGMSDKLibrary.so ${D}${libdir} 
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libTGMSDKLibrary.a ${D}${libdir} 

    #Things Manager Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/configuration
    copy_exec_recursive ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/configuration ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/configuration
    
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupaction
    copy_exec_recursive ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/groupaction ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupaction
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupsyncaction
    copy_exec_recursive ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/things-manager/sampleapp/linux/groupsyncaction ${IOTIVITY_BIN_DIR_D}/examples/service/things-manager/groupsyncaction

    #Notification Manager Framework
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/libNotificationManager.a ${D}${libdir} 

    #Notification Manager Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager/
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/notificationmanager ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/sampleconsumer ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/notification-manager/SampleApp/linux/sampleprovider ${IOTIVITY_BIN_DIR_D}/examples/service/notification-manager

    #Soft Sensor Manager Core
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libSSMCore.so ${D}${libdir} 
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/libSSMSDK.a ${D}${libdir} 

    #Soft Sensor Plugins
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libBMISensor.so ${D}${libdir}
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libDiscomfortIndexSensor.so ${D}${libdir}

    #Soft Sensor Manager Apps
    make_dir ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager/
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/HeightSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/SSMTesterApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    copy_file ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/SoftSensorDescription.xml ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/THSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/THSensorApp1 ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager
    copy_exec ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/service/soft-sensor-manager/WeightSensorApp ${IOTIVITY_BIN_DIR_D}/examples/service/soft-sensor-manager

    #Service Headers
    make_dir ${D}${includedir}/iotivity/service/soft-sensor-manager
    make_dir ${D}${includedir}/iotivity/service/notification-manager/
    make_dir ${D}${includedir}/iotivity/service/things-manager/
    make_dir ${D}${includedir}/iotivity/service/resource-encapsulation/   

    #Soft Sensor Manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SSMCore/include ${D}${includedir}/iotivity/service/soft-sensor-manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SDK/cpp/include  ${D}${includedir}/iotivity/service/soft-sensor-manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SSMCore/src/Common ${D}${includedir}/iotivity/service/soft-sensor-manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SSMCore/src/SSMInterface  ${D}${includedir}/iotivity/service/soft-sensor-manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SSMCore/src/QueryProcessor ${D}${includedir}/iotivity/service/soft-sensor-manager
    copy_file_recursive ${S}/service/soft-sensor-manager/SSMCore/src/SensorProcessor ${D}${includedir}/iotivity/service/soft-sensor-manager

    #Notification Manager
    copy_file_recursive ${S}/service/notification-manager/NotificationManager/include ${D}${includedir}/iotivity/service/notification-manager
    copy_file_recursive ${S}/service/things-manager/sdk/inc ${D}${includedir}/iotivity/service/things-manager

    #Resource Encapsulation 
    copy_file_recursive ${S}/service/resource-encapsulation/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/common/expiryTimer/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/common/primitiveResource/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/common/utils/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/resourceBroker/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/resourceCache/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/resourceContainer/bundle-api/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/resourceContainer/include ${D}${includedir}/iotivity/service/resource-encapsulation
    copy_file_recursive ${S}/service/resource-encapsulation/src/serverBuilder/include ${D}${includedir}/iotivity/service/resource-encapsulation

    #Misc headers
    make_dir ${D}${includedir}/iotivity/extlibs/cjson
    make_dir ${D}${includedir}/iotivity/extlibs/timer
    copy_file_recursive ${S}/extlibs/cjson/ ${D}${includedir}/iotivity/extlibs/cjson
    copy_file_recursive ${S}/extlibs/timer/ ${D}${includedir}/iotivity/extlibs/timer
}

#IOTIVITY packages:
#Resource: iotivity-resource, iotivity-resource-dev, iotivity-resource-thin-staticdev, iotivity-resource-dbg
#Resource Samples: iotivity-resource-samples, iotivity-resource-samples-dbg
#Service: iotivity-service, iotivity-service-dev, iotivity-service-staticdev, iotivity-service-dbg
#Service Samples: iotivity-service-samples, iotivity-service-samples-dbg
#Tests: iotivity-tests, iotivity-tests-dbg

FILES_iotivity-resource-dev = "\
                        ${includedir}/iotivity/resource \
                        ${inclidedir}/iotivity/extlibs"
                    
FILES_iotivity-resource-thin-staticdev = "\
                        ${libdir}/libocsrm.a \
                        ${libdir}/libconnectivity_abstraction.a \
                        ${libdir}/liboctbstack.a \
                        ${libdir}/libcoap.a \
                        ${libdir}/libc_common.a"

FILES_iotivity-resource = "\
                        ${libdir}/liboc.so \
                        ${libdir}/liboctbstack.so \
                        ${libdir}/liboc_logger.so \
                        ${libdir}/liboc_logger_core.so"

FILES_iotivity-resource-dbg = "\
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/resource \
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/extlibs \
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/examples \
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
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/service \
                        ${libdir}/.debug"   

FILES_iotivity-service-dev = "\
                        ${includedir}/iotivity/service"

FILES_iotivity-service = "\            
                        ${libdir}/libBMISensor.so \
                        ${libdir}/libDiscomfortIndexSensor.so \              
                        ${libdir}/librcs_server.so \
                        ${libdir}/librcs_common.so \
                        ${libdir}/librcs_container.so \
                        ${libdir}/libHueBundle.so \
                        ${libdir}/libSoftSensorBundle.so \
			${libdir}/libTGMSDKLibrary.so \
			${libdir}/libSSMCore.so"

FILES_iotivity-service-staticdev = "\
                        ${libdir}/librcs_client.a \
                        ${libdir}/librcs_server.a \
                        ${libdir}/librcs_common.a \
                        ${libdir}/librcs_container.a \
                        ${libdir}/libTGMSDKLibrary.a \
                        ${libdir}/libNotificationManager.a \
                        ${libdir}/libSSMSDK.a" 

FILES_iotivity-service-samples-dbg = "\
                      ${IOTIVITY_BIN_DIR}/examples/service/notification-manager/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/soft-sensor-manager/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/things-manager/groupaction/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/things-manager/groupsyncaction/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/resource-encapsulation/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/service/resource-encapsulation/resource-container/.debug \
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

PACKAGES = "iotivity-tests-dbg iotivity-tests iotivity-resource-dbg iotivity-resource iotivity-resource-dev iotivity-resource-thin-staticdev iotivity-resource-samples-dbg iotivity-resource-samples iotivity-service-dbg iotivity-service iotivity-service-dev iotivity-service-staticdev iotivity-service-samples-dbg iotivity-service-samples ${PN}-dev ${PN}"
ALLOW_EMPTY_${PN} = "1"
RDEPENDS_${PN} += "boost"
RRECOMMENDS_${PN} += "iotivity-resource iotivity-service"
RRECOMMENDS_${PN}-dev += "iotivity-resource-dev iotivity-resource-thin-staticdev iotivity-service-dev iotivity-service-staticdev"
RRECOMMENDS_iotivity-resource-thin-staticdev += "iotivity-resource-dev"
RRECOMMENDS_iotivity-service-dev += "iotivity-service iotivity-service-staticdev iotivity-resource"
RDEPENDS_iotivity-resource-samples += "iotivity-resource" 
RDEPENDS_iotivity-tests += "iotivity-resource"
RDEPENDS_iotivity-service-samples += "iotivity-service iotivity-resource"
RDEPENDS_iotivity-service += "iotivity-resource"
BBCLASSEXTEND = "native nativesdk"
