DESCRIPTION = "Soletta Development Application"
DEPENDS = "soletta nodejs systemd graphviz git"
LICENSE = "BSD-3-Clause"
PV = "1_beta1"

LIC_FILES_CHKSUM = "file://LICENSE;md5=dbf9699ab0f60ec50f52ce70fcd07caf"
SRC_URI[archive.md5sum] = "5ccfdef2f6e8b4f72bdc5161e96c1e6c"
SRC_URI[archive.sha256sum] = "9349d9935c3cc61f705fff88b623ae5e3fc6645f7b29dc8fdf51781a39a5bb76"
SRC_URI = "https://github.com/solettaproject/soletta-dev-app/releases/download/v${PV}/soletta-dev-app_standalone_v${PV}.tar.gz;name=archive \
           file://soletta-dev-app.service \
           file://soletta-dev-app-mac.sh \
           file://soletta-dev-app-avahi-discover.service \
"

S = "${WORKDIR}/${PN}"

INSANE_SKIP_${PN} += "file-rdeps debug-files arch"

INSTALLATION_PATH = "/"
SYSTEMD_PATH = "${systemd_unitdir}/system/"
AUTOSTART_SYSTEMD_PATH = "/etc/systemd/system/multi-user.target.wants/"
AVAHI_SERVICE = "/etc/avahi/services/"

FILES_${PN} += " \
    ${INSTALLATION_PATH}soletta-dev-app \
    ${SYSTEMD_PATH}soletta-dev-app-server.service \
    ${SYSTEMD_PATH}fbp-runner@.service \
    ${AUTOSTART_SYSTEMD_PATH}soletta-dev-app-server.service \
    ${AVAHI_SERVICE}soletta-dev-app.service \
    ${SYSTEMD_PATH}soletta-dev-app-avahi-discover.service \
    /soletta-dev-app/scripts/soletta-dev-app-mac.sh \
"

do_install() {
  install -d ${D}${INSTALLATION_PATH}soletta-dev-app
  cp -r ${S}/* ${D}${INSTALLATION_PATH}soletta-dev-app

  #SYSTEMD Installation part
  install -d ${D}${SYSTEMD_PATH}
  install -m 0655 ${S}/scripts/units/fbp-runner@.service ${D}${SYSTEMD_PATH}
  install -m 0655 ${S}/scripts/units/soletta-dev-app-server.service.in ${D}${SYSTEMD_PATH}soletta-dev-app-server.service
  sed -i "s@PATH@"${INSTALLATION_PATH}soletta-dev-app"@" ${D}${SYSTEMD_PATH}soletta-dev-app-server.service
  sed -i "s@"NODE_BIN_NAME"@"node"@" ${D}${SYSTEMD_PATH}soletta-dev-app-server.service

  #Autostart soletta-dev-app-server service
  install -d ${D}${AUTOSTART_SYSTEMD_PATH}
  ln -sf ${SYSTEMD_PATH}soletta-dev-app-server.service ${D}${AUTOSTART_SYSTEMD_PATH}soletta-dev-app-server.service

  #Configure avahi to discover Soletta Dev App server
  install -d ${D}${AVAHI_SERVICE}
  install -m 0655 ${WORKDIR}/soletta-dev-app.service ${D}${AVAHI_SERVICE}

  #Configure services that will set MAC address to Soletta Dev-App name
  install -m 0655 ${WORKDIR}/soletta-dev-app-avahi-discover.service ${D}${SYSTEMD_PATH}
  ln -sf ${SYSTEMD_PATH}soletta-dev-app-avahi-discover.service ${D}${AUTOSTART_SYSTEMD_PATH}

 #Install set MAC address script
 install  -m 0755 ${WORKDIR}/soletta-dev-app-mac.sh ${D}${INSTALLATION_PATH}soletta-dev-app/scripts/

}
