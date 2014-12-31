inherit scons

SUMMARY = "Iotivity framework and SDK by the Open Interconnect Consortium."
DESCRIPTION = "IoTivity is an open source software framework enabling seamless device-to-device connectivity to address the emerging needs of the Internet of Things."
HOMEPAGE = "https://www.iotivity.org/"
DEPENDS = "boost virtual/gettext"
SECTION = "libs"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://resource/include/OCApi.h;beginline=1;endline=19;md5=fc5a615cf1dc3880967127bc853b3e0c"
SRC_URI = "http://downloads.iotivity.org/0.9.0/iotivity-0.9.0.tar.gz;name=iotivity \
           git://github.com/USCiLab/cereal.git;protocol=https;name=cereal \
          "
SRC_URI[iotivity.md5sum] = "6a7bcba19f2d110144c65a7f033fd4d8"
SRC_URI[iotivity.sha256sum] = "e2da664bf464f4f2a11d0b0ad2923408f6c3fb0e92d97cd5c256feaeead4c1e8"
SRC_URI[cereal.md5sum] = "2d9adeb49a2cb54f259c601d34d2d959"
SRC_URI[cereal.sha256sum] = "33dfeed8f6345a4dff42e1057a79b1d5303624a4a3bdb362f9c17a0048c811ee"
SRCREV_cereal = "7121e91e6ab8c3e6a6516d9d9c3e6804e6f65245"

python () {
    EXTRA_OESCONS = ""
    IOTIVITY_TARGET_ARCH = d.getVar("TARGET_ARCH", True)
    if IOTIVITY_TARGET_ARCH == "i586":
        IOTIVITY_TARGET_ARCH = "x86"
    elif IOTIVITY_TARGET_ARCH == "x86_64":
        IOTIVITY_TARGET_ARCH = "x86_64"
    else:
        IOTIVITY_TARGET_ARCH = ""
    if IOTIVITY_TARGET_ARCH != "":
        EXTRA_OESCONS = "TARGET_OS=yocto TARGET_ARCH=" + IOTIVITY_TARGET_ARCH + " RELEASE=1"
    d.setVar("EXTRA_OESCONS", EXTRA_OESCONS)
    d.setVar("IOTIVITY_TARGET_ARCH", IOTIVITY_TARGET_ARCH)
}

IOTIVITY_BIN_DIR = "/opt/iotivity"
IOTIVITY_BIN_DIR_D = "${D}${IOTIVITY_BIN_DIR}"

do_patch() {
    mkdir -p ${S}/extlibs/cereal
    cp -R ${WORKDIR}/git/* ${S}/extlibs/cereal
    cd ${S}/extlibs/cereal
    patch -p1 < ../../resource/patches/cereal_gcc46.patch
}

do_install() {
    install -d ${D}${libdir}  

    #Resource runtimes
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/libcoap.so ${D}${libdir}
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc.so ${D}${libdir}
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboctbstack.so ${D}${libdir}
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger.so ${D}${libdir}
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/liboc_logger_core.so ${D}${libdir} 

    #Resource headers
    install -d ${D}${includedir}/iotivity/
    install -d ${D}${includedir}/iotivity/stack/
    install -d ${D}${includedir}/iotivity/ocsocket/
    install -d ${D}${includedir}/iotivity/oc_logger/
    cd ${S}/resource/include && find . -type d -exec install -d ${D}${includedir}/iotivity/"{}" \;
    cd ${S}/resource/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/"{}" \;
    cd ${S}/resource/csdk/stack/include && find . -type d -exec install -d ${D}${includedir}/iotivity/stack/"{}" \;
    cd ${S}/resource/csdk/stack/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/stack/"{}" \;
    cd ${S}/resource/csdk/ocsocket/include && find . -type d -exec install -d ${D}${includedir}/iotivity/ocsocket/"{}" \;
    cd ${S}/resource/csdk/ocsocket/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/ocsocket/"{}" \;
    cd ${S}/resource/oc_logger/include && find . -type d -exec install -d ${D}${includedir}/iotivity/oc_logger/"{}" \;
    cd ${S}/resource/oc_logger/include && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/iotivity/oc_logger/"{}" \;

    #Resource samples
    install -d ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceclient ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/presenceserver ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomclient ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/roomserver ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclient ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientserver ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserver ${IOTIVITY_BIN_DIR_D}/examples/resource
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeclient ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/fridgeserver ${IOTIVITY_BIN_DIR_D}/examples/resource   
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageclient ${IOTIVITY_BIN_DIR_D}/examples/resource   
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/garageserver ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleclientHQ ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/simpleserverHQ ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryserver ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/devicediscoveryclient ${IOTIVITY_BIN_DIR_D}/examples/resource  
    install -d ${IOTIVITY_BIN_DIR_D}/examples/resource/ocicuc
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/ocicuc/client ${IOTIVITY_BIN_DIR_D}/examples/resource/ocicuc
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/ocicuc/monoprocess ${IOTIVITY_BIN_DIR_D}/examples/resource/ocicuc	
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/ocicuc/server ${IOTIVITY_BIN_DIR_D}/examples/resource/ocicuc
    install -c -m 555 ${S}/out/yocto/${IOTIVITY_TARGET_ARCH}/release/resource/examples/ocicuc/small_example ${IOTIVITY_BIN_DIR_D}/examples/resource/ocicuc
}

#IOTIVITY packages:
#Resource: iotivity-resource, iotivity-resource-dev, iotivity-resource-dbg
#Resource Samples: iotivity-resource-samples, iotivity-resource-samples-dbg

FILES_iotivity-resource-dev = "\
                        ${includedir}/iotivity"
                    
FILES_iotivity-resource = "\
                        ${libdir}/libcoap.so \
                        ${libdir}/liboc.so \
                        ${libdir}/liboctbstack.so \
                        ${libdir}/liboc_logger.so \
                        ${libdir}/liboc_logger_core.so"

FILES_iotivity-resource-dbg = "\
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/resource \
                        ${prefix}/src/debug/${PN}/${EXTENDPE}${PV}-${PR}/${PN}-${PV}/extlibs \
                        ${libdir}/.debug/libcoap.so \
                        ${libdir}/.debug/liboc.so \
                        ${libdir}/.debug/liboctbstack.so \
                        ${libdir}/.debug/liboc_logger.so \
                        ${libdir}/.debug/liboc_logger_core.so"   

FILES_iotivity-resource-samples = "\
                      ${IOTIVITY_BIN_DIR}/examples/resource \
                      ${IOTIVITY_BIN_DIR}/examples/resource/ocicuc"

FILES_iotivity-resource-samples-dbg = "\
                      ${IOTIVITY_BIN_DIR}/examples/resource/.debug \
                      ${IOTIVITY_BIN_DIR}/examples/resource/ocicuc/.debug"

PACKAGES = "iotivity-resource-dbg iotivity-resource iotivity-resource-dev iotivity-resource-samples-dbg iotivity-resource-samples ${PN}-dev ${PN}"
ALLOW_EMPTY_${PN} = "1"
RDEPENDS_${PN} += "boost"
RRECOMMENDS_${PN} += "iotivity-resource"
RRECOMMENDS_${PN}-dev += "iotivity-resource-dev"
RRECOMMENDS_iotivity-resource-dev += "iotivity-resource"
RDEPENDS_iotivity-resource-samples += "iotivity-resource" 
BBCLASSEXTEND = "native nativesdk"

