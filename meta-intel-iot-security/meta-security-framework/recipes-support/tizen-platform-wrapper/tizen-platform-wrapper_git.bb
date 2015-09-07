require tizen-platform-wrapper.inc

PV = "2.0+git${SRCPV}"
SRCREV = "ce8e849a4632d168e420065445dbdc43df061a8a"
SRC_URI = "git://review.tizen.org/platform/core/appfw/tizen-platform-wrapper;nobranch=1 \
           file://0001-gcc-5.2.0-fix-linking-issues-caused-by-inline-keywor.patch \
           "
S = "${WORKDIR}/git"
