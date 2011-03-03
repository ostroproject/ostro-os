SUMMARY = "Provide a basic init script to enable audio"
DESCRIPTION = "This package provides an init script which enables the audio on startup via the amixer command.  It address a problem with the development board that has the audio muted on power on."
SECTION = "base"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${POKYBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58"

PR = "r2"
RDEPENDS = "alsa-utils-amixer"

SRC_URI = "file://n450_audiofix"

do_install () {
	install -d ${D}${sysconfdir}/init.d
	install -d ${D}${sysconfdir}/rc5.d
	install -m 0755 ${WORKDIR}/n450_audiofix ${D}${sysconfdir}/init.d
	ln -sf ${D}${sysconfdir}/init.d/n450_audiofix ${D}/${sysconfdir}/rc5.d/S91n450_audiofix
}
