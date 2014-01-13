FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#LINUX_VERSION = "3.10.19"

SRCREV_meta = "0580cffb6f760a22c056f8ada43a60c444a4ca3e"
SRCREV_machine = "7446bf268c69a88faef816be7a1efc35b1f96b9b"

COMPATIBLE_MACHINE_intel-core2-32 = "intel-core2-32"
KMACHINE_intel-core2-32 = "common-pc"
KBRANCH_intel-core2-32 = "standard/base"
KERNEL_FEATURES_append_intel-core2-32 = " cfg/vesafb"
#SRCREV_meta_intel-core2-32 = "d9cd83c0292bd4e2a6754a96761027252e726a42"
#SRCREV_machine_intel-core2-32 = "a9ec82e355130160f9094e670bd5be0022a84194"

COMPATIBLE_MACHINE_intel-corei7-64 = "intel-corei7-64"
KMACHINE_intel-corei7-64 = "common-pc-64"
KBRANCH_intel-corei7-64 = "standard/base"
KERNEL_FEATURES_append_intel-corei7-64 = " cfg/vesafb"
#SRCREV_meta_intel-corei7-64 = "d9cd83c0292bd4e2a6754a96761027252e726a42"
#SRCREV_machine_intel-corei7-64 = "a9ec82e355130160f9094e670bd5be0022a84194"
