FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

LINUX_VERSION = "3.8.13"

SRCREV_meta_crownbay = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_crownbay = "f20047520a57322f05d95a18a5fbd082fb15cb87"
SRCREV_emgd_crownbay = "a18cbb7a2886206815dbf6c85caed3cb020801e0"

SRCREV_meta_crownbay-noemgd = "8ef9136539464c145963ac2b8ee0196fea1c2337"
SRCREV_machine_crownbay-noemgd = "f20047520a57322f05d95a18a5fbd082fb15cb87"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
