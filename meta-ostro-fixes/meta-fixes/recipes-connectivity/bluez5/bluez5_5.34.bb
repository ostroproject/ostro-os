FILESEXTRAPATHS_prepend = "${COREBASE}/meta/recipes-connectivity/bluez5/bluez5"
require recipes-connectivity/bluez5/bluez5.inc
SRC_URI[md5sum] = "68581ef1c5e3e5bcec9c57a2d3c57495"
SRC_URI[sha256sum] = "e461ec2927f5491a202de4a180b2b42377f596b0ce372430d8204ae042d3b19c"

# noinst programs in Makefile.tools that are conditional on READLINE
# support
NOINST_TOOLS_READLINE ?= " \
    attrib/gatttool \
    tools/obex-client-tool \
    tools/obex-server-tool \
    tools/bluetooth-player \
    tools/obexctl \
"

# noinst programs in Makefile.tools that are conditional on EXPERIMENTAL
# support
NOINST_TOOLS_EXPERIMENTAL ?= " \
    emulator/btvirt \
    emulator/b1ee \
    emulator/hfp \
    tools/3dsp \
    tools/mgmt-tester \
    tools/gap-tester \
    tools/l2cap-tester \
    tools/sco-tester \
    tools/smp-tester \
    tools/hci-tester \
    tools/rfcomm-tester \
    tools/bdaddr \
    tools/avinfo \
    tools/avtest \
    tools/scotest \
    tools/amptest \
    tools/hwdb \
    tools/hcieventmask \
    tools/hcisecfilter \
    tools/btmgmt \
    tools/btinfo \
    tools/btattach \
    tools/btsnoop \
    tools/btproxy \
    tools/btiotest \
    tools/mcaptest \
    tools/cltest \
    tools/oobtest \
    tools/seq2bseq \
    tools/ibeacon \
    tools/btgatt-client \
    tools/btgatt-server \
    tools/gatt-service \
    profiles/iap/iapd \
"

# remove some ancient deprecated programs that cause issues
# in static analysis
do_install_append() {
    rm ${D}/${bindir}/ciptool
    rm ${D}/${bindir}/rfcomm
    rm ${D}/${bindir}/bccmd
}
