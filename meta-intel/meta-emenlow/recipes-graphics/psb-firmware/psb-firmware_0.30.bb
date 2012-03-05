DESCRIPTION = "Binary firmware for the Poulsbo (psb) 3D X11 driver"
LICENSE = "Intel-binary-only"
LIC_FILES_CHKSUM = "file://COPYING;md5=02c597a2f082b4581596065bb5a521a8"
PR = "r0"

SRC_URI = "https://launchpad.net/~gma500/+archive/ppa/+files/psb-firmware_0.30-0ubuntu1netbook1ubuntu1.tar.gz"

SRC_URI[md5sum] = "760005739edc64387240e56f6916e825"
SRC_URI[sha256sum] = "714bc9162409b172caaabdaff5a942bc9d104a9b3a47a165754f7090803ba4b3"

do_install() {
        install -d ${D}${base_libdir}/firmware/
	install -m 0644 ${WORKDIR}/psb-firmware-0.30/msvdx_fw.bin ${D}${base_libdir}/firmware/
}

FILES_${PN} += "${base_libdir}/firmware/msvdx_fw.bin"

COMPATIBLE_MACHINE = "emenlow"
