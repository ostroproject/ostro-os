FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "d560dc224c77283a400cf1ffee301b7089a52a68"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "ae3e64c077972fe87f09946bd215620df68ca327"
