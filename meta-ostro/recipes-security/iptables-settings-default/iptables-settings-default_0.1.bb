# Copyright (C) 2016 Intel.
# Released under the MIT license (see COPYING.MIT for the terms)

DESCRIPTION = "Default iptables and ip6tables settings."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
    file://default-iptables.rules \
    file://default-ip6tables.rules \
"

inherit update-alternatives

# use update-alternatives for letting several rulesets to be installed
# to the same sysroot
ALTERNATIVE_${PN} += "iptables.rules"
ALTERNATIVE_LINK_NAME[iptables.rules] = "${datadir}/iptables-settings/iptables.rules"
ALTERNATIVE_TARGET[iptables.rules] = "${datadir}/iptables-settings/default-iptables.rules"

# update-alternatives does not add the generated files automatically to
# FILES_${PN}

FILES_${PN} += "${datadir}/iptables-settings/"

do_install() {
    install -d ${D}${datadir}/iptables-settings
    install -m 0644 ${WORKDIR}/default-iptables.rules ${D}${datadir}/iptables-settings/default-iptables.rules

    if ${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'true', 'false', d)}; then
        install -m 0644 ${WORKDIR}/default-ip6tables.rules ${D}${datadir}/iptables-settings/default-ip6tables.rules
    fi
}

python () {
    # if we have IPv6 support, set the alternative variables

    datadir = d.getVar("datadir", True)
    pn = d.getVar("PN", True)

    if bb.utils.contains('DISTRO_FEATURES', 'ipv6', 'True', 'False', d):
        d.appendVar('ALTERNATIVE_' + pn, ' ip6tables.rules')
        d.setVarFlag('ALTERNATIVE_LINK_NAME', 'ip6tables.rules', datadir + '/iptables-settings/ip6tables.rules')
        d.setVarFlag('ALTERNATIVE_TARGET', 'ip6tables.rules', datadir + '/iptables-settings/default-ip6tables.rules')
}
