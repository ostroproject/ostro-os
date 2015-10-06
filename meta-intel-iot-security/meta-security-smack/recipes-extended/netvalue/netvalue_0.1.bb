SUMMARY = "IP network information Display"

# this license is temporary and it will be reviewed under sdl process
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/BSD-3-Clause;md5=550794465ba0ec5312d6919e203a55f9"


BBCLASSEXTEND = "native"
SRC_URI += "file://netvalue.c"

do_compile(){
        ${CC} -o netvalue ../netvalue.c
}

do_install(){
        install -d ${D}${bindir}
        install -m 551 netvalue ${D}${bindir}/netvalue
}
