require ima-evm-utils.inc

# 0.9 according to Tizen .spec file, but there is no such tag?
PV = "0.9+git${SRCPV}"
SRCREV = "d85dfd821c7a34da03634b81127b5dfc081912f9"
SRC_URI = "git://review.tizen.org/platform/upstream/ima-evm-utils;nobranch=1"
S = "${WORKDIR}/git"
