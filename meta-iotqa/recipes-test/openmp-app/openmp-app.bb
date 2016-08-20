DESCRIPTION = "Test OpenMP support functionality"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://openmp-app.c"

S = "${WORKDIR}"

do_configure() {
}

do_compile() {
	${CC} ${CFLAGS} -fopenmp ${LDFLAGS} -o ${WORKDIR}/openmp-app ${S}/openmp-app.c
}

do_install() {
	install -m 0755 -d ${D}${bindir}
	install -m 0755 ${WORKDIR}/openmp-app ${D}${bindir}
}

