require recipes-connectivity/bluez5/bluez5.inc

SRC_URI[md5sum] = "432b1f292c0b78771818c67140baf3d9"
SRC_URI[sha256sum] = "fe4f35e701cbec04478818adf014ed9bbd1f7d11e2603370f1b70a78106f57f7"

# to get bluetooth.conf
FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "\
    ${KERNELORG_MIRROR}/linux/bluetooth/bluez-${PV}.tar.xz \
    file://bluetooth.conf \
    file://obex_set_dbus_session_service.patch \
"

RDEPENDS_${PN} += "glibc-gconv-utf-16"

PACKAGECONFIG[alsa] = ""

EXTRA_OECONF += "\
  --enable-sixaxis \
  --enable-experimental \
"

do_install_append() {
	install -d ${D}${sysconfdir}/bluetooth/
	if [ -f ${S}/profiles/proximity/proximity.conf ]; then
	    install -m 0644 ${S}/profiles/proximity/proximity.conf ${D}/${sysconfdir}/bluetooth/
	fi
	if [ -f ${S}/src/main.conf ]; then
	    install -m 0644 ${S}/src/main.conf ${D}/${sysconfdir}/bluetooth/
	fi
	if [ -f ${S}/tools/btmgmt ]; then
	    install -m 0755 ${S}/tools/btmgmt ${D}${bindir}
	fi
	if [ -f ${S}/tools/obexctl ]; then
	    install -m 0755 ${S}/tools/obexctl ${D}${bindir}
	fi

	if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
		# Copy file service
		install -d ${D}/${systemd_unitdir}/system
		install -m 644 ${S}/obexd/src/obex.service ${D}/${systemd_unitdir}/system/
	fi
}

