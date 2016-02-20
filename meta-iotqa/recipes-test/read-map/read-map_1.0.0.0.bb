SUMMARY = "read-map"
DESCRIPTION = "test binary to read outside of mapped memory. should exit with segfault"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
SRC_URI = "file://read-map.c \
"

S = "${WORKDIR}"

do_compile() {
    ${CC} read-map.c -o read-map
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 read-map ${D}${bindir}
}
