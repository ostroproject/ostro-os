# Needed to replace certain files.
# Upstream-status: Submitted (OE-core "[PATCH 0/4] some init/finish enhancements for initramfs-framework")
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://rootfs"

do_install_append() {
    install -m 0755 ${WORKDIR}/rootfs ${D}/init.d/90-rootfs
}

FILES_${PN}-base += "/init.d/90-rootfs"
