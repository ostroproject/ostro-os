LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://app-runas.cpp;beginline=3;endline=19;md5=1ca447189bb2c54039033d50d8982d92"
SRC_URI = "file://app-runas.cpp"
DEPENDS = "security-manager"
S = "${WORKDIR}"

do_compile () {
    ${CXX} ${CXXFLAGS} ${S}/app-runas.cpp `pkg-config --cflags --libs security-manager` -o app-runas
}

do_install () {
    install -D app-runas ${D}/${bindir}/app-runas
    chmod u+s ${D}/${bindir}/app-runas
}

inherit deploy-files
DEPLOY_FILES_FROM[target] = "app-runas"
