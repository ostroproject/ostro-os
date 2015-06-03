SUMMARY = "Hello world from OTC IoT QA"
DESCRIPTION = "test application"
HOMEPAGE = "http://ostroproject.org/"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYRIGHT;md5=349c872e0066155e1818b786938876a4"
 
SRC_URI = "file://hello.c \
           file://COPYRIGHT \
"
S = "${WORKDIR}"
do_compile() {
    ${CC} hello.c -o hello
}
