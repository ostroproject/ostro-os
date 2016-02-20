VERSION_ID = "${@bb.data.getVar('BUILD_ID',d,1).split('-')[-1].join(['', '0']) }"

FILES_${PN}_append = " /usr/lib/os-release "

do_install_append() {
    install -d ${D}/usr/lib
    mv ${D}/etc/os-release ${D}/usr/lib
    ln -s ../usr/lib/os-release ${D}/etc/os-release
}
