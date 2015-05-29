require ima-evm-utils.inc

# 0.9 was released without tagging it. Using the commit which says "Release version 0.9".
PV = "0.9+git${SRCPV}"
SRCREV = "3d9bdc1de282846de3523fd7a698d473304650b0"
SRC_URI = "git://git.code.sf.net/p/linux-ima/ima-evm-utils"
S = "${WORKDIR}/git"

# Documentation depends on asciidoc, which we do not have, so
# do not build documentation.
SRC_URI += "file://disable-doc-creation.patch"
