FILESEXTRAPATHS_prepend := "${THISDIR}/systemd:"

SRC_URI_append = "\
                 file://ethernet.network \
                 "

# Enable networkd and resolved by default
PACKAGECONFIG_append = " networkd resolved"

do_install_append() {
        # Only install the ethernet configuration in case networkd is enabled
        if [ "${@bb.utils.contains('PACKAGECONFIG', 'networkd', '1', '0', d)}" = "1" ] ; then
                install -D -m 0644 ${WORKDIR}/ethernet.network ${D}${sysconfdir}/systemd/network/ethernet.network
        fi
}
