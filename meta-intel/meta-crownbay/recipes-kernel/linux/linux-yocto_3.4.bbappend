FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

SRCREV_machine_pn-linux-yocto_crownbay ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_crownbay ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "08f65e2611877f7339a0626ab1c7255a35787adb"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"

LINUX_VERSION = "3.4.28"
