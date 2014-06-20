SUMMARY = "Workable systemd hack to have a sensible time when booting without RTC"
SECTION = "utils"
AUTHOR = "Matthias Hann, Brendan Le Foll"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

SRC_URI = "file://keep-shutdown-time \
           file://keep-shutdown-time.service \
           file://set-initial-date\
           file://set-initial-date.service \
           file://set-galileo-hostname.service"

inherit systemd

FILES_${PN} += "${sbindir}/keep-shutdown-time \
                ${sbindir}/set-initial-date \
                ${systemd_unitdir}/system/set-initial-date.service \
                ${systemd_unitdir}/system/keep-shutdown-time.service \
                ${systemd_unitdir}/set-galileo-hostname.service"

do_install () {
  install -d ${D}/${sbindir}
  install -m 0700 ${WORKDIR}/keep-shutdown-time ${D}${sbindir}
  install -m 0700 ${WORKDIR}/set-initial-date ${D}${sbindir}
  install -d ${D}${systemd_unitdir}/system/
  install -m 0644 ${WORKDIR}/set-initial-date.service ${D}${systemd_unitdir}/system/
  install -m 0644 ${WORKDIR}/keep-shutdown-time.service ${D}${systemd_unitdir}/system/
  install -m 0644 ${WORKDIR}/set-galileo-hostname.service ${D}${systemd_unitdir}/system/
}

SYSTEMD_SERVICE_${PN} = "keep-shutdown-time.service set-initial-date.service set-galileo-hostname.service"
