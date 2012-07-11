FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
RDEPENDS_${PN} += "genmac"
PRINC := "${@int(PRINC) + 2}"
