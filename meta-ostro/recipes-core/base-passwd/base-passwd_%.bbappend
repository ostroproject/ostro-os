# This .bbappend overrides the default users and groups from Debian
# with just those really needed in Ostro OS. This is where we
# define and (where necessary) activate special groups.

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += " \
    file://passwd.master \
    file://group.master \
"

do_patch[postfuncs] += "override_files"
override_files () {
    cp ${WORKDIR}/passwd.master ${WORKDIR}/group.master ${S}
}
