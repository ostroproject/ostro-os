# Normally one would use MACHINE_ESSENTIAL_EXTRA_RDEPENDS in a machine
# config, but we need to make changes to existing machine
# configurations and thus cannot do that. As it only needs to work for
# one image (at the moment!), install machine-specific packages via a
# .bbappend for now.

IMAGE_INSTALL_append_intel-corei7-64 = " \
		spi-minnowmax-board \
		"

IMAGE_INSTALL_append_edison = " systemd-watchdog"
IMAGE_INSTALL_append_beaglebone = " systemd-watchdog"
# Actually only relevant on MinnowMax, but causes little harm
# elsewhere (unnecessary sleep wakeup every 45 seconds).
IMAGE_INSTALL_append_intel-corei7-64 = " systemd-watchdog"
