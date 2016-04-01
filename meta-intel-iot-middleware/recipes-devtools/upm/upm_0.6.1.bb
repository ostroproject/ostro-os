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

PACKAGECONFIG ??= "python nodejs java"
PACKAGECONFIG[python] = "-DBUILDSWIGPYTHON=OFF, -DBUILDSWIGPYTHON=OFF, swig-native python, python-mraa"
PACKAGECONFIG[nodejs] = "-DBUILDSWIGNODE=OFF, -DBUILDSWIGNODE=OFF, swig-native nodejs, node-mraa"
PACKAGECONFIG[java] = "-DBUILDSWIGJAVA=ON, -DBUILDSWIGJAVA=OFF, swig-native icedtea7-native, java-mraa"

export JAVA_HOME="${STAGING_DIR}/${BUILD_SYS}/usr/lib/jvm/icedtea7-native"

cmake_do_generate_toolchain_file_append() {
  echo "
set (JAVA_AWT_INCLUDE_PATH ${JAVA_HOME}/include CACHE PATH \"AWT include path\" FORCE)
set (JAVA_AWT_LIBRARY ${JAVA_HOME}/jre/lib/amd64/libjawt.so CACHE FILEPATH \"AWT Library\" FORCE)
set (JAVA_INCLUDE_PATH ${JAVA_HOME}/include CACHE PATH \"java include path\" FORCE)
set (JAVA_INCLUDE_PATH2 ${JAVA_HOME}/include/linux CACHE PATH \"java include path\" FORCE)
set (JAVA_JVM_LIBRARY ${JAVA_HOME}/jre/lib/amd64/libjvm.so CACHE FILEPATH \"path to JVM\" FORCE)
" >> ${WORKDIR}/toolchain.cmake
}

# include .jar files in /usr/lib/java for 64 bit builds
FILES_${PN}_append = "${@' ${libdir}/../lib/java/*.jar' if '${TARGET_ARCH}' == 'x86_64' else ''}"

# include nodejs files in /usr/lib/node_modules for 64 bit builds
FILES_${PN}_append = "${@' ${libdir}/../lib/node_modules/*' if '${TARGET_ARCH}' == 'x86_64' else ''}"

# include .so symlinks in main package
FILES_${PN}_append = "${@' ${libdir}/../lib64/*.so' if '${TARGET_ARCH}' == 'x86_64' else ' ${libdir}/../lib/*.so'}"
INSANE_SKIP_${PN} = "dev-so"
