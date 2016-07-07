require cynara.inc

PV = "0.11.0+git${SRCPV}"
SRCREV = "973765e329f8a84c1549cb2b0c65ccb1cce3c2d3"
SRC_URI = "git://github.com/Samsung/cynara.git"
S = "${WORKDIR}/git"

SRC_URI += " \
file://cynara-db-migration-abort-on-errors.patch \
file://cmake-Improves-directories-and-libsystemd.patch \
"
