# rmc-systemd-boot bbclass
# Deploy central RMC database file to ESP

IMAGE_INSTALL_append = " rmc"

inherit systemd-boot

do_bootimg[depends] += "${MLPREFIX}rmc-db:do_deploy"

efi_populate_append() {
        install -m 0400 ${DEPLOY_DIR_IMAGE}/rmc.db ${DEST}/rmc.db
}
