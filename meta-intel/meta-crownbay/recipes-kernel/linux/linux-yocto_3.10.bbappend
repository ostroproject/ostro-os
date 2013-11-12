FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_append_crownbay = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.17"

SRCREV_meta_crownbay = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_crownbay = "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_emgd_crownbay = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"

SRCREV_meta_crownbay-noemgd = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_crownbay-noemgd = "c03195ed6e3066494e3fb4be69154a57066e845b"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
