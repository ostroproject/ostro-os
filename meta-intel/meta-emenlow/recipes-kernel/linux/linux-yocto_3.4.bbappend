FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd  = "emenlow"
KBRANCH_emenlow-noemgd  = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma600"

SRCREV_machine_pn-linux-yocto_emenlow ?= "0a1e7660733615106a2430e38bf6b835a8e5507d"
SRCREV_meta_pn-linux-yocto_emenlow ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"
SRCREV_emgd_pn-linux-yocto_emenlow ?= "f5c3a221f0e42d48ee5af369d73594e26ef7fae6"

SRCREV_machine_pn-linux-yocto_emenlow-noemgd ?= "0a1e7660733615106a2430e38bf6b835a8e5507d"
SRCREV_meta_pn-linux-yocto_emenlow-noemgd ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"

LINUX_VERSION = "3.4.46"
