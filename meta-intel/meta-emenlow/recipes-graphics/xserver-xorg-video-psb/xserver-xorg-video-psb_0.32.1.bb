DESCRIPTION = "2D graphics driver for Poulsbo"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://MIT_License.txt;md5=732825ecdcf420261531d935fcd914a7"
PR = "r3"

inherit autotools

SRC_URI = "https://launchpad.net/~gma500/+archive/ppa/+files/xserver-xorg-video-psb_0.36.0-0ubuntu3~1004um9.tar.gz \
	file://xorg-x11-drv-psb-0.31.0-ignoreacpi.patch;patch=1 \
	file://xorg-x11-drv-psb-0.31.0-xserver17.patch;patch=1 \
	file://xserver-xorg-video-psb-0.31.0-assert.patch;patch=1 \
	file://xserver-xorg-video-psb-0.31.0-comment_unused.patch;patch=1 \
	file://xserver-xorg-video-psb-0.31.0-greedy.patch;patch=1 \
	file://xserver-xorg-video-psb-0.31.0-loader.patch;patch=1 \
	file://stubs.patch;patch=1 \
	file://01_disable_lid_timer.patch;patch=1 \
	file://psb_xvtempfix.patch;patch=1 \
	file://psb_mixed.patch;patch=1 \
	file://dri-h.patch \
	file://libdrm-poulsbo.patch"

SRC_URI[md5sum] = "67bd808960db4fe9b3a7ff2582da1608"
SRC_URI[sha256sum] = "deeaf6e4d059e709d8a4268bd013a172f7fbd70778236d7d1e2712d1951de72c"

export DRI_CFLAGS="-I${STAGING_INCDIR}/psb -I${STAGING_INCDIR}/psb/drm \
	-I${STAGING_INCDIR}/X11/dri"

export CFLAGS = "-fvisibility=default"
export XORG_CFLAGS="-fvisibility=default -I${STAGING_INCDIR}/xorg \
       -I${STAGING_INCDIR}/pixman-1"

FILES_${PN} += "${libdir}/xorg/modules/drivers/libmm.so \
	     ${libdir}/xorg/modules/drivers/psb_drv.so"

DEPENDS += "virtual/libgl virtual/xserver"

RDEPENDS_${PN} = "xserver-psb-module-exa"

COMPATIBLE_MACHINE = "emenlow"
