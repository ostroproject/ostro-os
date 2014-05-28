SUMMARY = "Low Level Skeleton Library for Communication on Intel platforms"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=e8db6501ed294e65418a933925d12058"

# git is required to get a good version from git describe
DEPENDS = "nodejs swig-native git-native git"

SRC_URI = "git://github.com/intel-iot-devkit/maa.git;protocol=git;rev=b9352a9e8cff14addbfc215784f48b43a81717a7"
SRC_URI += "file://package.json"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/maa/examples/"

FILES_${PN}-dbg += "${libdir}/node_modules/maajs/.debug/ \
                  ${PYTHON_SITEPACKAGES_DIR}/.debug/"

do_compile_prepend () {
  # when yocto builds in ${D} it does not have access to ../git/.git so git
  # describe --tags fails. In order not to tag our version as dirty we use this
  # trick
  sed -i 's/-dirty//' src/version.c
}

do_install_append () {
  install -d ${D}${libdir}/node_modules/
  install -d ${D}${libdir}/node_modules/maajs
  cp ${WORKDIR}/build/src/javascript/maajs.node ${D}${libdir}/node_modules/maajs
  cp ${WORKDIR}/package.json ${D}${libdir}/node_modules/maajs

  install -d ${D}${PYTHON_SITEPACKAGES_DIR}
  cp ${WORKDIR}/build/src/python/_pymaa.so ${D}${PYTHON_SITEPACKAGES_DIR}
  cp ${WORKDIR}/build/src/python/pymaa.py ${D}${PYTHON_SITEPACKAGES_DIR}
}
