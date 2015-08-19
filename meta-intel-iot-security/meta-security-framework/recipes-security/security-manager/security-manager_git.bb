require security-manager.inc

PV = "1.0.2+git${SRCPV}"
SRCREV = "860305a595d681d650024ad07b3b0977e1fcb0a6"
SRC_URI += "git://github.com/Samsung/security-manager.git"
S = "${WORKDIR}/git"

SRC_URI += " \
file://systemd-stop-using-compat-libs.patch \
file://security-manager-policy-reload-do-not-depend-on-GNU-.patch \
"
