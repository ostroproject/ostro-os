KBRANCH ?= "linux-4.0.y"

require recipes-kernel/linux/linux-yocto.inc

S = "${WORKDIR}/linux-stable"
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Override COMPATIBLE_MACHINE to include your machine in a bbappend
# file. Leaving it empty here ensures an early explicit build failure.
COMPATIBLE_MACHINE = "quark"

SRCREV = "be4cb235441a691ee63ba5e00843a9c210be5b8a"

SRC_URI_quark = " \
	git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git;bareclone=1;branch=${KBRANCH} \
	file://defconfig \
	"

LINUX_VERSION ?= "4.0.5"

