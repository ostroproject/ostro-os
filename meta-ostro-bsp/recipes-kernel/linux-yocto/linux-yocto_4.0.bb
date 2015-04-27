KBRANCH ?= "master"

require recipes-kernel/linux/linux-yocto.inc

S = "${WORKDIR}/linux-stable"
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Override COMPATIBLE_MACHINE to include your machine in a bbappend
# file. Leaving it empty here ensures an early explicit build failure.
COMPATIBLE_MACHINE = "quark"

SRCREV = "db4fd9c5d072a20ea6b7e40276a9822e04732610"

SRC_URI = " \
	git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git;bareclone=1;branch=${KBRANCH} \
	file://defconfig \
	"

LINUX_VERSION ?= "4.0.0"

