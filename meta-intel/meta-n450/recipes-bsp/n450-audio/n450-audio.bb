SUMMARY = "Provide a basic init script to enable audio"
DESCRIPTION = "Set the volume and unmute the Front mixer setting during boot."
SECTION = "base"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${POKYBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58"

PR = "r3"

inherit update-rc.d

RDEPENDS = "alsa-utils-amixer"

SRC_URI = "file://n450-audio"

INITSCRIPT_NAME = "n450-audio"
INITSCRIPT_PARAMS = "defaults 90"

do_install() {
        install -d ${D}${sysconfdir} \
                   ${D}${sysconfdir}/init.d
	install -m 0755 ${WORKDIR}/n450-audio ${D}${sysconfdir}/init.d
}

