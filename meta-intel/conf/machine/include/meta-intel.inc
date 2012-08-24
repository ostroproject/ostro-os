#
# BSP variables and settings specific to the meta-intel layer.
# You must include the meta-intel layer in your bblayers.conf
# to use them.
#

#
# XSERVER subcomponents, used to build the XSERVER variable
#
XSERVER_IA32_EMGD = "emgd-driver-bin \
           "

XSERVER_IA32_MATROX_MGA = "xserver-xorg-module-xaa \
           xf86-video-mga \
           "

