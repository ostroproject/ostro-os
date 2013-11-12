FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.10.17"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"
SRCREV_meta_fri2 = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_fri2 = "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_emgd_fri2 = "39c44dd7838bfd228938219cdb21ca30c4d0cbbf"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_fri2-noemgd = "c03195ed6e3066494e3fb4be69154a57066e845b"

module_autoload_iwlwifi = "iwlwifi"

