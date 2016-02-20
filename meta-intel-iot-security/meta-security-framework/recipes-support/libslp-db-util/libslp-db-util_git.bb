require libslp-db-util.inc

PV = "0.1.1+git${SRCPV}"
SRCREV = "4ef37c0712f5f5043768c66ffef2a7f5b76ba940"
SRC_URI += "git://review.tizen.org/platform/core/appfw/libslp-db-util;nobranch=1"
S = "${WORKDIR}/git"
