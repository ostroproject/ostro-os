DESCRIPTION = "Selection of tools for developers working with Smack"
HOMEPAGE = "https://github.com/smack-team/smack"
SECTION = "Security/Access Control"
LICENSE = "LGPL-2.1"
PV = "1.0.5"

# Alias needed to satisfy dependencies in other recipes.
# This recipe itself cannot be named "smack" because that
# would conflict with the "smack" override.
PROVIDES = "smack"
RPROVIDES_${PN} += "smack"

LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"
PV = "1.1.0+git${SRCPV}"
SRCREV = "0bd2831dae7500fcfc080519ded5ae2bf6752226"
SRC_URI += "git://review.tizen.org/platform/upstream/smack;nobranch=1"
S = "${WORKDIR}/git"

inherit autotools

BBCLASSEXTEND = "native"

# Fix copied from meta-tizen.
do_configure_prepend() {
  sed -i 's@systemd_new=no@systemd_new=yes@' ${S}/configure.ac
  sed -i '/PKG_CHECK_MODULES(/,/)/{s/b/r/p;d}' ${S}/configure.ac
}
