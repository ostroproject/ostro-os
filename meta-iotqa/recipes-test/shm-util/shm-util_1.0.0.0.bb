SUMMARY = "shm-util"
DESCRIPTION = "test application for shared memory segments. Alternative to ipcmk and ipcrm"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://shm-util.c \
"

S = "${WORKDIR}"

do_compile() {
    ${CC} shm-util.c ${LDFLAGS} -o shm-util
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 shm-util ${D}${bindir}
}
