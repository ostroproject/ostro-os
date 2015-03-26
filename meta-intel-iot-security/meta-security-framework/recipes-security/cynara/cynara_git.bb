require cynara.inc

PV = "0.6.1+git${SRCPV}"
SRCREV = "229ec1e1e8c5940c62f734e4b8a0b9c49eb8f9f2"
SRC_URI = "git://review.tizen.org/platform/core/security/cynara;nobranch=1"
S = "${WORKDIR}/git"

SRC_URI += " \
file://systemd-stop-using-compat-libs.patch \
file://systemd-configurable-unit-dir.patch \
file://cynara-db-migration-abort-on-errors.patch \
file://cynara-db-migration-sysroot-support.patch \
"
