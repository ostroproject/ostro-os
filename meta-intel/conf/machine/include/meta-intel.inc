#
# BSP variables and settings specific to the meta-intel layer.
# You must include the meta-intel layer in your bblayers.conf
# to use them.
#

#
# XSERVER subcomponents, used to build the XSERVER variable
#

# for Xserver older than 1.13.0
OLD_XSERVER_X86_EXT = "xserver-xorg-extension-dri \
           xserver-xorg-extension-dri2 \
           xserver-xorg-extension-extmod \
           xserver-xorg-extension-dbe \
           "

XSERVER_X86_EMGD = "emgd-driver-bin \
           ${OLD_XSERVER_X86_EXT} \
           "

XSERVER_X86_MATROX_MGA = "xf86-video-mga \
           "

