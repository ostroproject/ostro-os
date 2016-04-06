#
DESCRIPTION = "ostro-6lowpan systemd service"
RDEPENDS_${PN} += "iproute2 lowpan-tools"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
PR = "r0"

SRC_URI = "file://ostro-6lowpan.service \
           file://ostro-6lowpan-start.sh \
           file://ostro-6lowpan-stop.sh \
           "

FILES_${PN} += " ${systemd_unitdir}/system/ostro-6lowpan.service \
                 ${libdir}/ostro-scripts/ostro-6lowpan-start.sh \
                 ${libdir}/ostro-scripts/ostro-6lowpan-stop.sh \
               "
# Sample configuring file
do_install_append () {
	install -d -m 755 ${D}${systemd_unitdir}/system/
	install -m 0644 ostro-6lowpan.service ${D}${systemd_unitdir}/system/
	install -d -m 755 ${D}${libdir}/ostro-scripts/
	install -m 0755 ostro-6lowpan-start.sh ${D}${libdir}/ostro-scripts/
	install -m 0755 ostro-6lowpan-stop.sh ${D}${libdir}/ostro-scripts/
}

S = "${WORKDIR}"

