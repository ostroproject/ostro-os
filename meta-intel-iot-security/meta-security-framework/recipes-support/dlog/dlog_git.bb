require dlog.inc

PV = "0.4.1+git${SRCPV}"
# This version is what is included in Tizen images. It uses systemd
# journal, unconditionally. More recent revisions reverted that and
# restored the custom logging.
SRCREV = "c43bce370f4aaa09f48df4e2c1d2b99f133526d0"
SRC_URI += "git://review.tizen.org/platform/core/system/dlog;nobranch=1"
S = "${WORKDIR}/git"

SRC_URI += "file://systemd-stop-using-compat-libs.patch"
