FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_append_crownbay = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.34"

SRCREV_meta_crownbay = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_crownbay = "c7739be126930006e3bfbdb2fb070a967abc5e09"
SRCREV_emgd_crownbay = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"

SRCREV_meta_crownbay-noemgd = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_crownbay-noemgd = "c7739be126930006e3bfbdb2fb070a967abc5e09"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
