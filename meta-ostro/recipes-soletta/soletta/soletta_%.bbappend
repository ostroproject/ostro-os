FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

DEPENDS_append = " systemd"

SRC_URI += " file://config"

INSANE_SKIP_${PN}-dev += "dev-elf"

do_configure_prepend() {
    cp ${WORKDIR}/config ${S}/.config
}
