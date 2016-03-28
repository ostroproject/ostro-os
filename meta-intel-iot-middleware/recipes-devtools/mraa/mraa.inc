SUMMARY = "Low Level Skeleton Library for Communication on Intel platforms"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=66493d54e65bfc12c7983ff2e884f37f"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/mraa/examples/"

FILES_${PN}-dbg += "${libdir}/node_modules/mraajs/.debug/ \
                    ${PYTHON_SITEPACKAGES_DIR}/.debug/"

# include .jar files in /usr/lib/java for 64 bit builds
FILES_${PN}_append = "${@' ${libdir}/../lib/*' if '${TARGET_ARCH}' == 'x86_64' else ''}"

# include .so symlinks in main package
FILES_${PN}_append = "${@' ${libdir}/../lib64/*.so' if '${TARGET_ARCH}' == 'x86_64' else ' ${libdir}/../lib/*.so'}"
INSANE_SKIP_${PN} = "dev-so"

PACKAGECONFIG ??= "python nodejs java"
PACKAGECONFIG[python] = "-DBUILDSWIGPYTHON=ON, -DBUILDSWIGPYTHON=OFF, swig-native python"
PACKAGECONFIG[nodejs] = "-DBUILDSWIGNODE=ON, -DBUILDSWIGNODE=OFF, swig-native nodejs"
PACKAGECONFIG[java] = "-DBUILDSWIGJAVA=ON, -DBUILDSWIGJAVA=OFF, swig-native icedtea7-native,"

# for ftdi support, not included by default
PACKAGECONFIG[usbplat] = "-DUSBPLAT=ON, -DUSBPLAT=OFF,,"
PACKAGECONFIG[ftdi4222] = "-DFTDI4222=ON, -DFTDI4222=OFF, libft4222, libft4222"

EXTRA_OECMAKE_append = "-DINSTALLGPIOTOOL=ON"

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

do_compile_prepend () {
  # when yocto builds in ${D} it does not have access to ../git/.git so git
  # describe --tags fails. In order not to tag our version as dirty we use this
  # trick
  sed -i 's/-dirty//' src/version.c
}
