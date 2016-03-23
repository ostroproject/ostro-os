SUMMARY = "systemd service and configuration files needed by soletta demos"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690"

#
#  1- Appending DHCP configuration for networkd
#  2- Configuring to auto mount usb sticks
#
SRC_URI = "file://any.network \
           file://10-automount-usbstick.rules \
           file://automount-handler@.service \
           file://umount-handler@.service \
           file://on_boot.fbp \
           file://warn-boot.service \
           file://warn-boot.timer \
"

RDPEPENDS_${PN} = "systemd"

S = "${WORKDIR}/files"

FILES_${PN} = "${libdir}/udev/rules.d/* \
               ${systemd_system_unitdir}/* \
               ${sysconfdir}/systemd/* \
"

do_install(){
    install -d ${D}${systemd_system_unitdir}
    install -d ${D}${systemd_system_unitdir}/multi-user.target.wants
    install -d ${D}${libdir}/udev/rules.d
    install -d ${D}${sysconfdir}/systemd/network

    install -m0644 ${WORKDIR}/any.network ${D}${sysconfdir}/systemd/network/ethernet.network

    #Auto mount rules
    #Systemd Rules
    install -m 0755 ${WORKDIR}/automount-handler@.service ${D}${systemd_system_unitdir}
    install -m 0755 ${WORKDIR}/umount-handler@.service ${D}${systemd_system_unitdir}

    #Auto Start
    ln -sf ${systemd_system_unitdir}/automount-handler@.service ${D}${systemd_system_unitdir}/multi-user.target.wants/automount-handler@.service
    ln -sf ${systemd_system_unitdir}/umount-handler@.service ${D}${systemd_system_unitdir}/multi-user.target.wants/umount-handler@.service
    #Udev rules
    install -m 0755 ${WORKDIR}/10-automount-usbstick.rules ${D}${libdir}/udev/rules.d

    #Service that will warn the user that system was booted
    install -m 0755 ${WORKDIR}/on_boot.fbp ${D}${systemd_system_unitdir}
    install -m 0755 ${WORKDIR}/warn-boot.service ${D}${systemd_system_unitdir}
    install -m 0755 ${WORKDIR}/warn-boot.timer ${D}${systemd_system_unitdir}
    ln -sf ${systemd_system_unitdir}/warn-boot.timer ${D}${systemd_system_unitdir}/multi-user.target.wants/warn-boot.timer

}
