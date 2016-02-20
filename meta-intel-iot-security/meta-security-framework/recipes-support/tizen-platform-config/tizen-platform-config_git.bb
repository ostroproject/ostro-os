require tizen-platform-config.inc

PV = "2.0+git${SRCPV}"
SRCREV = "451432aade897491698e5e6fe7d18cd00e28b718"
SRC_URI += "git://review.tizen.org/platform/core/appfw/tizen-platform-config;nobranch=1"
S = "${WORKDIR}/git"

SRC_URI += "file://support-cross-compiling.patch"
