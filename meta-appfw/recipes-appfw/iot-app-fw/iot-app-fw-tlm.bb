DESCRIPTION = "IoT App FW TLM launch mechanism"
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

DEPENDS =+ "tlm"
RDEPENDS_${PN} =+ "tlm"

S="${WORKDIR}/"

SRC_URI = "file://COPYING.MIT \
           file://tlm-launch \
          "

do_install_append() {
    install -D -m 755 ${S}tlm-launch ${D}/etc/session.d/tlm-launch
}


FILES_${PN} += "/etc/session.d/tlm-launch"

