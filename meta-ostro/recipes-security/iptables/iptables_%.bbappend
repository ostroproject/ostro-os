FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI_append = "\
    file://iptables.service.in \
    file://ip6tables.service.in \
"

inherit systemd

# Depend on an iptables configuration. If no configuration is specified
# then use the default configuration.
VIRTUAL-RUNTIME_iptables-settings ?= "iptables-settings-default"
RDEPENDS_${PN} += "${VIRTUAL-RUNTIME_iptables-settings}"

do_install_append() {
    install -d ${D}${systemd_unitdir}/system

    sed -e 's#{datadir}#${datadir}#' ${WORKDIR}/iptables.service.in > ${WORKDIR}/iptables.service
    install -m 0644 ${WORKDIR}/iptables.service ${D}${systemd_unitdir}/system

    if ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'true', 'false', d)}; then
        sed -e 's#{datadir}#${datadir}#' ${WORKDIR}/ip6tables.service.in > ${WORKDIR}/ip6tables.service
        install -m 0644 ${WORKDIR}/ip6tables.service ${D}${systemd_unitdir}/system
    fi
}

SYSTEMD_SERVICE_${PN} = " \
    iptables.service \
    ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'ip6tables.service', '', d)} \
"
