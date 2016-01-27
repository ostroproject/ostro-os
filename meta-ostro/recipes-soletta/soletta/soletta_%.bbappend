FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

DEPENDS_append = " systemd"

SRC_URI += " file://config"

do_configure_prepend() {
    cp ${WORKDIR}/config ${S}/.config
}
