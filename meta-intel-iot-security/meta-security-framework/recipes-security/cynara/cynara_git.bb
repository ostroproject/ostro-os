require cynara.inc

PV = "0.8.0+git${SRCPV}"
SRCREV = "b4cb3d8e86ef3a2bea256c2215d4d2f9bd73bb97"
SRC_URI = "git://github.com/Samsung/cynara.git"
S = "${WORKDIR}/git"

SRC_URI += " \
file://systemd-stop-using-compat-libs.patch \
file://systemd-configurable-unit-dir.patch \
file://cynara-db-migration-abort-on-errors.patch \
file://cynara-db-migration-sysroot-support.patch \
file://PolicyKeyFeature-avoid-complex-global-constants.patch \
file://globals-avoid-copying-other-globals.patch \
file://chsgen-include-logging-code-in-debug-mode.patch \
"
