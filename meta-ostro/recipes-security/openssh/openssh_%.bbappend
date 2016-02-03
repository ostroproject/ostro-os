FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

RDEPENDS_${PN} += "iptables"

SRC_URI_append = "\
    file://${PN}-ipv4.conf \
    file://${PN}-ipv6.conf \
"

do_install_append() {
    install -d ${D}${systemd_unitdir}/system/sshd.socket.d
    install -m 0644 ${WORKDIR}/${PN}-ipv4.conf ${D}${systemd_unitdir}/system/sshd.socket.d
    if ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'true', 'false', d)}; then
        install -m 0644 ${WORKDIR}/${PN}-ipv6.conf ${D}${systemd_unitdir}/system/sshd.socket.d
    fi
}

FILES_${PN} += " \
    ${systemd_unitdir}/system/sshd.socket.d/${PN}-ipv4.conf \
    ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', \
        '${systemd_unitdir}/system/sshd.socket.d/${PN}-ipv6.conf', '', d)} \
"
