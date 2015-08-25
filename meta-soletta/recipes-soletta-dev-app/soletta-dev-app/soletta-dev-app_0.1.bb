DESCRIPTION = "Soletta Development Application"
DEPENDS = "soletta nodejs systemd graphviz git"
LICENSE = "BSD-3-Clause"
PV = "1_beta0"

LIC_FILES_CHKSUM = "file://LICENSE;md5=dbf9699ab0f60ec50f52ce70fcd07caf"
SRC_URI[archive.md5sum] = "e5de0a6698813969f6dd1e953e7ed3f1"
SRC_URI[archive.sha256sum] = "420d1c200837fae7821037a8a7c596b3b9d1577ef8be13da34238319a3dcdea0"
SRC_URI = "https://github.com/solettaproject/soletta-dev-app/releases/download/v${PV}/soletta-dev-app_standalone_v1beta0.tar.gz;name=archive"

S = "${WORKDIR}/${PN}"

INSANE_SKIP_${PN} += "file-rdeps debug-files arch"

INSTALLATION_PATH = "/"
SYSTEMD_PATH = "${systemd_unitdir}/system/"
AUTOSTART_SYSTEMD_PATH = "/etc/systemd/system/multi-user.target.wants/"

FILES_${PN} += " \
    ${INSTALLATION_PATH}soletta-dev-app \
    ${SYSTEMD_PATH}soletta-dev-app-server.service \
    ${SYSTEMD_PATH}fbp-runner@.service \
    ${AUTOSTART_SYSTEMD_PATH}soletta-dev-app-server.service \
"

do_install() {
  install -d ${D}${INSTALLATION_PATH}soletta-dev-app
  cp -r ${S}/* ${D}${INSTALLATION_PATH}soletta-dev-app

  #SYSTEMD Installation part
  install -d ${D}${SYSTEMD_PATH}
  install -m 0755 ${S}/scripts/units/fbp-runner@.service ${D}${SYSTEMD_PATH}
  install -m 0755 ${S}/scripts/units/soletta-dev-app-server.service.in ${D}${SYSTEMD_PATH}soletta-dev-app-server.service
  sed -i "s@PATH@"${INSTALLATION_PATH}soletta-dev-app"@" ${D}${SYSTEMD_PATH}soletta-dev-app-server.service
  sed -i "s@"NODE_BIN_NAME"@"node"@" ${D}${SYSTEMD_PATH}soletta-dev-app-server.service

  #Autostart soletta-dev-app-server service
  install -d ${D}${AUTOSTART_SYSTEMD_PATH}
  ln -sf ${SYSTEMD_PATH}soletta-dev-app-server.service ${D}${AUTOSTART_SYSTEMD_PATH}soletta-dev-app-server.service
}
