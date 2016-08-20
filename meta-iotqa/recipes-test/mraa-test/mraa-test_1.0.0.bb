SUMMARY = "mraa"
DESCRIPTION = "test application for mraa lib"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
DEPENDS = "mraa" 
SRC_URI = "file://hello_mraa.c \
"

S = "${WORKDIR}"

do_compile() {
    ${CC} hello_mraa.c ${LDFLAGS} -o hello_mraa -lmraa
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 hello_mraa ${D}${bindir}
}
