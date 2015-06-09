SUMMARY = "Cereal - A C++ library for serialization."
DESCRIPTION = "cereal is a header-only C++11 serialization library. cereal takes arbitrary data types and reversibly turns them into different representations, such as compact binary encodings, XML, or JSON."
HOMEPAGE = "http://uscilab.github.com/cereal"
SECTION = "libs"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e612690af2f575dfd02e2e91443cea23"
SRC_URI = "git://github.com/USCiLab/cereal.git;protocol=https;name=cereal"
SRC_URI[cereal.md5sum] = "2d9adeb49a2cb54f259c601d34d2d959"
SRC_URI[cereal.sha256sum] = "33dfeed8f6345a4dff42e1057a79b1d5303624a4a3bdb362f9c17a0048c811ee"
SRC_URI += "file://cereal_gcc46.patch"
SRCREV_cereal = "7121e91e6ab8c3e6a6516d9d9c3e6804e6f65245"

S = "${WORKDIR}/git"

do_install() {
    install -d ${D}${includedir}/cereal
    cd ${S}/include/cereal && find . -type d -exec install -d ${D}${includedir}/cereal/"{}" \;
    cd ${S}/include/cereal && find . -type f -exec install -c -m 444 "{}" ${D}${includedir}/cereal/"{}" \;
}

FILES_cereal = "${includedir}/include/cereal"

ALLOW_EMPTY_${PN} = "1"
PACKAGES = "${PN}"
BBCLASSEXTEND = "native nativesdk"
