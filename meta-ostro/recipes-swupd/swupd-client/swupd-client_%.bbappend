FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "file://0001-Disable-boot-file-heuristics.patch \
                  file://efi_combo_updater.c \
                 "

RDEPENDS_${PN}_class-target_append = " gptfdisk"

do_compile_append() {
  ${CC} ${LDFLAGS} ${WORKDIR}/efi_combo_updater.c  -Os -o ${B}/efi_combo_updater `pkg-config --cflags --libs glib-2.0`
}

do_install_append () {
    install -d ${D}/usr/bin
    install ${B}/efi_combo_updater ${D}/usr/bin/
}
