require security-manager.inc

PV = "1.0.1+git${SRCPV}"
SRCREV = "6eb825a3876061b2e152d42974e117dcbedf7c70"
SRC_URI += "git://review.tizen.org/platform/core/security/security-manager;nobranch=1"
S = "${WORKDIR}/git"

SRC_URI += "file://systemd-stop-using-compat-libs.patch"
