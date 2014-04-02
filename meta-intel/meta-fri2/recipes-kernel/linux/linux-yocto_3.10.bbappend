FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"
LINUX_VERSION_fri2 = "3.10.34"
SRCREV_meta_fri2 = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_fri2 = "c7739be126930006e3bfbdb2fb070a967abc5e09"
SRCREV_emgd_fri2 = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.10.34"
SRCREV_meta_fri2-noemgd = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_fri2-noemgd = "c7739be126930006e3bfbdb2fb070a967abc5e09"

module_autoload_iwlwifi = "iwlwifi"

