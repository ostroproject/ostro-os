# This .bbappend overrides the default users and groups from Debian
# with just those really needed in Ostro OS. This is where we
# define and (where necessary) activate special groups.

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += " \
    file://passwd.master \
    file://group.master \
    file://rfkill-udev.rules \
"

do_patch[postfuncs] += "override_files"
override_files () {
    cp ${WORKDIR}/passwd.master ${WORKDIR}/group.master ${S}
}

do_install_append () {
    install -d ${D}/${base_libdir}/udev/rules.d
    install -m 0644 ${WORKDIR}/rfkill-udev.rules ${D}/${base_libdir}/udev/rules.d/90-rfkill.rules
}

