FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

#############################
# MACHINE = valleyisland-32 #
#############################
COMPATIBLE_MACHINE_valleyisland-32 = "valleyisland-32"
KMACHINE_valleyisland-32 = "valleyisland-32"
KBRANCH_valleyisland-32 = "standard/base"
KERNEL_FEATURES_valleyisland-32 = " features/valleyisland-io/valleyisland-io \
				    features/valleyisland-io/valleyisland-io-pci.scc"

LINUX_VERSION_valleyisland-32 = "3.10.40"
SRCREV_machine_valleyisland-32 = "f53a6114b3a6e8c03ca4752de829887015f4c942"
SRCREV_meta_valleyisland-32 = "90edb289dccfe838d4e364e1a5815447a6642b98"
SRCREV_valleyisland-io_valleyisland-32 = "8ea4fb625f2654bbdd5dfcb9db67328d21ebe504"

SRC_URI_valleyisland-32 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},valleyisland-io-1.0;name=machine,meta,valleyisland-io"

#############################
# MACHINE = valleyisland-64 #
#############################
COMPATIBLE_MACHINE_valleyisland-64 = "valleyisland-64"
KMACHINE_valleyisland-64 = "valleyisland"
KBRANCH_valleyisland-64 = "standard/base"
KERNEL_FEATURES_valleyisland-64 = " features/valleyisland-io/valleyisland-io \
				    features/valleyisland-io/valleyisland-io-pci.scc"

LINUX_VERSION_valleyisland-64 = "3.10.40"
SRCREV_machine_valleyisland-64 = "f53a6114b3a6e8c03ca4752de829887015f4c942"
SRCREV_meta_valleyisland-64 = "90edb289dccfe838d4e364e1a5815447a6642b98"
SRCREV_valleyisland-io_valleyisland-64 = "8ea4fb625f2654bbdd5dfcb9db67328d21ebe504"

SRC_URI_valleyisland-64 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},valleyisland-io-1.0;name=machine,meta,valleyisland-io"

KERNEL_MODULE_AUTOLOAD_valleyisland-32 += "i2c-dev"
KERNEL_MODULE_AUTOLOAD_valleyisland-64 += "i2c-dev"
