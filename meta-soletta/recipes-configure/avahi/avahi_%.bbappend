#  avahi_%.bbappend
#
# Configure to autostart avahi daemon on system boot

SYSTEMD_PATH = "${systemd_unitdir}/system/"
AUTOSTART_SYSTEMD_PATH = "/etc/systemd/system/multi-user.target.wants/"

FILES_${PN} += "${AUTOSTART_SYSTEMD_PATH}avahi-daemon.service"

do_install_append(){
    install -d ${D}${AUTOSTART_SYSTEMD_PATH}
    ln -sf ${SYSTEMD_PATH}avahi-daemon.service ${D}${AUTOSTART_SYSTEMD_PATH}avahi-daemon.service
}
