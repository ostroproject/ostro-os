KBRANCH ?= "linux-4.0.y"

require recipes-kernel/linux/linux-yocto.inc

S = "${WORKDIR}/linux-stable"
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Override COMPATIBLE_MACHINE to include your machine in a bbappend
# file. Leaving it empty here ensures an early explicit build failure.
COMPATIBLE_MACHINE = "quark"

SRCREV = "a0ce889438e8204b87d1f30f941646636e26837e"

SRC_URI_quark = " \
	git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git;bareclone=1;branch=${KBRANCH} \
	file://quark/PATCHv6-1-1-thermal-intel-Quark-SoC-X1000-DTS-thermal-driver.patch \
	file://defconfig \
	"

LINUX_VERSION ?= "4.0.6"

