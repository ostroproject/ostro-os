DESCRIPTION = "Server for IOT REST APIs."
HOMEPAGE = "https://github.com/01org/iot-rest-api-server"
LICENSE = "Apache-2.0"

LIC_FILES_CHKSUM = "file://${WORKDIR}/git/LICENSE;md5=fa818a259cbed7ce8bc2a22d35a464fc"

DEPENDS = "nodejs-native iotivity iotivity-node"
RDEPENDS_${PN} += "bash iot-app-fw-node-bindings iot-app-fw-launcher"

SRC_URI = "git://git@github.com/01org/iot-rest-api-server.git;protocol=https"
SRCREV = "705bd09874862d31af8663b570906dd6ef888901"

S = "${WORKDIR}/git"

INSANE_SKIP_${PN} += "ldflags staticdev"

do_compile_prepend() {
    OCTBDIR="${STAGING_DIR_TARGET}${includedir}/iotivity/resource"
    export OCTBSTACK_CFLAGS="-I${OCTBDIR} -I${OCTBDIR}/stack -I${OCTBDIR}/logger -I${OCTBDIR}/oc_logger -I${OCTBDIR}/ocrandom -DROUTING_GATEWAY"
    export OCTBSTACK_LIBS="-loctbstack"
    export CFLAGS="$CFLAGS -fPIC"
    export CXXFLAGS="$CXXFLAGS -fPIC"
}

do_compile () {
    # changing the home directory to the working directory, the .npmrc will be created in this directory
    export HOME=${WORKDIR}

    # does not build dev packages
    npm config set dev false

    # access npm registry using http
    npm set strict-ssl false
    npm config set registry http://registry.npmjs.org/

    # configure http proxy if neccessary
    if [ -n "${http_proxy}" ]; then
        npm config set proxy ${http_proxy}
    fi
    if [ -n "${HTTP_PROXY}" ]; then
        npm config set proxy ${HTTP_PROXY}
    fi

    # configure cache to be in working directory
    npm set cache ${WORKDIR}/npm_cache

    # clear local cache prior to each compile
    npm cache clear

    case ${TARGET_ARCH} in
        i?86) targetArch="ia32"
            echo "targetArch = 32"
            ;;
        x86_64) targetArch="x64"
            echo "targetArch = 64"
            ;;
        arm) targetArch="arm"
            ;;
        mips) targetArch="mips"
            ;;
        sparc) targetArch="sparc"
            ;;
        *) echo "unknown architecture"
           exit 1
            ;;
    esac

    # compile and install  node modules in source directory
    npm --arch=${targetArch} --production --verbose install
}

do_install () {
    install -d ${D}${libdir}/node_modules/iot-rest-api-server/
    cp -r ${S}/* ${D}${libdir}/node_modules/iot-rest-api-server/
}

FILES_${PN} = "${libdir}/node_modules/iot-rest-api-server/ \
"

INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

PACKAGES = "${PN}"
