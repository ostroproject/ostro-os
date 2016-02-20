FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://main.conf"

FILES_${PN} += "${sysconfdir}/connman/main.conf"

do_install_append () {
    mkdir -p ${D}${sysconfdir}/connman
    touch ${D}${sysconfdir}/connman/main.conf
    blklist=$(cat ${D}${sysconfdir}/connman/main.conf | \
        grep ^NetworkInterfaceBlacklist | sed 's/ *//g')
    if test -z "$blklist"; then
        cat ${WORKDIR}/main.conf >> ${D}${sysconfdir}/connman/main.conf
    else
        echo "$blklist,ve-" > ${D}${sysconfdir}/connman/main.conf.blklist
        grep -v ^NetworkInterfaceBlacklist ${D}${sysconfdir}/connman/main.conf \
            >> ${D}${sysconfdir}/connman/main.conf.blklist
        mv ${D}${sysconfdir}/connman/main.conf.blklist \
            ${D}${sysconfdir}/connman/main.conf
    fi
}
