#
#  1- Appending DHCP configuration for networkd
#  2- Configuring to auto mount usb sticks
#

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += "file://any.network \
            file://10-automount-usbstick.rules \
            file://automount-handler@.service \
            file://umount-handler@.service \
            file://on_boot.fbp \
            file://warn-boot.service \
            file://warn-boot.timer \
            file://generate-avahi-name.service \
            file://avahi_conf_gen.sh \
            file://hostname-set.service \
            file://hostname-set.sh"

#Configuring to autostart samba systemd service
AUTOSTART_SYSTEMD_DIR = "/etc/systemd/system/multi-user.target.wants"
SYSTEMD_DIR = "/lib/systemd/system"
SYSTEM_ETC_DIR = "/etc/systemd/system"
UDEV_DIR = "/lib/udev/rules.d"

FILES_${PN}-services-networkd += "{sysconfdir}/systemd/network/ethernet.network"

FILES_${PN} += "${UDEV_DIR}/10-automount-usbstick.rules \
                ${SYSTEMD_DIR}/automount-handler@.service \
                ${SYSTEMD_DIR}/umount-handler@.service \
                ${SYSTEMD_DIR}/on_boot.fbp \
                ${SYSTEMD_DIR}/warn-boot.service \
                ${SYSTEMD_DIR}/warn-boot.timer \
                ${SYSTEMD_DIR}/generate-avahi-name.service \
                ${SYSTEMD_DIR}/avahi_conf_gen.sh \
                ${SYSTEMD_DIR}/hostname-set.service \
                ${SYSTEMD_DIR}/hostname-set.sh"

EXTRA_OECONF := "${@oe_filter_out('--disable-kdbus', '${EXTRA_OECONF}', d)}"
EXTRA_OECONF += "--disable-blkid --enable-kdbus"

do_install_append(){
    install -Dm0644 ${WORKDIR}/any.network ${D}${sysconfdir}/systemd/network/ethernet.network

    #Auto mount rules
    #Systemd Rules
    install -m 0755 ${WORKDIR}/automount-handler@.service ${D}${SYSTEMD_DIR}
    install -m 0755 ${WORKDIR}/umount-handler@.service ${D}${SYSTEMD_DIR}

    #Auto Start
    ln -sf ${SYSTEMD_DIR}/automount-handler@.service ${D}${AUTOSTART_SYSTEMD_DIR}/automount-handler@.service
    ln -sf ${SYSTEMD_DIR}/umount-handler@.service ${D}${AUTOSTART_SYSTEMD_DIR}/umount-handler@.service
    #Udev rules
    install -m 0755 ${WORKDIR}/10-automount-usbstick.rules ${D}${UDEV_DIR}

    #Service that will warn the user that system was booted
    install -m 0755 ${WORKDIR}/on_boot.fbp ${D}${SYSTEMD_DIR}
    install -m 0755 ${WORKDIR}/warn-boot.service ${D}${SYSTEMD_DIR}
    install -m 0755 ${WORKDIR}/warn-boot.timer ${D}${SYSTEMD_DIR}
    ln -sf ${SYSTEMD_DIR}/warn-boot.timer ${D}${AUTOSTART_SYSTEMD_DIR}/warn-boot.timer

    #Autostart avahi services
    ln -sf ${SYSTEMD_DIR}/avahi-daemon.socket ${D}${AUTOSTART_SOCKET_DIR}/avahi-daemon.socket

    #Install and autostart avahi autogenerate name service
    install -m 0755 ${WORKDIR}/avahi_conf_gen.sh ${D}${SYSTEMD_DIR}
    install -m 0755 ${WORKDIR}/generate-avahi-name.service ${D}${SYSTEMD_DIR}
    ln -sf ${SYSTEMD_DIR}/generate-avahi-name.service ${D}${AUTOSTART_SYSTEMD_DIR}/generate-avahi-name.service

    #Install and autostart hostname service
    install -m 0755 ${WORKDIR}/hostname-set.sh ${D}${SYSTEMD_DIR}
    install -m 0755 ${WORKDIR}//hostname-set.service ${D}${SYSTEMD_DIR}
    ln -sf ${SYSTEMD_DIR}/hostname-set.service ${D}${AUTOSTART_SYSTEMD_DIR}/hostname-set.service

}
