FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
RDEPENDS_${PN}_sys940x_append += "genmac"
RDEPENDS_${PN}_sys940x-noemgd_append += "genmac"
PRINC := "${@int(PRINC) + 2}"
