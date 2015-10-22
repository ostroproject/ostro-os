SUMMARY = "Mmap binary used to test smack mmap attribute"
DESCRIPTION = "Mmap binary used to test smack mmap attribute"
LICENSE = "VERBATIM"
LIC_FILES_CHKSUM = "file://LICENSE;md5=52d0f7188d92ede618092599653e0a63"
NO_GENERIC_LICENSE[VERBATIM] = "1"

SRC_URI = "file://mmap.c file://LICENSE" 

S = "${WORKDIR}"
do_compile() {
    ${CC} mmap.c -o mmap_test
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 mmap_test ${D}${bindir}
}
