FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI_append = "\
    file://iptables.service \
    file://iptables.rules \
    file://ip6tables.service \
    file://ip6tables.rules \
"

inherit systemd

do_install_prepend() {
    install -d ${D}/etc/iptables
    install -m 0644 ${WORKDIR}/iptables.rules ${D}/etc/iptables

    install -d ${D}${systemd_unitdir}/system
    install -m 0644 ${WORKDIR}/iptables.service ${D}${systemd_unitdir}/system

    if ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'true', 'false', d)}; then
        install -m 0644 ${WORKDIR}/ip6tables.rules ${D}/etc/iptables
        install -m 0644 ${WORKDIR}/ip6tables.service ${D}${systemd_unitdir}/system
    fi
}

SYSTEMD_SERVICE_${PN} = " \
    iptables.service \
    ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'ip6tables.service', '', d)} \
"
