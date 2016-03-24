# swupd-client checks VERSION_ID, which must match the OS_VERSION
# used for generating swupd bundles in the current build.
VERSION_ID = "${OS_VERSION}"

FILES_${PN}_append = " /usr/lib/os-release "

# As swupd-client doesn't update files in /etc move os-release's
# content to /usr/lib
do_install_append() {
    install -d ${D}/usr/lib
    mv ${D}/etc/os-release ${D}/usr/lib
    lnr ${D}/usr/lib/os-release ${D}/etc/os-release
}
