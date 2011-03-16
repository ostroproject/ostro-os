require recipes-graphics/xorg-xserver/xserver-xf86-dri-lite.inc

LIC_FILES_CHKSUM = "file://COPYING;md5=3dd2bbe3563837f80ed8926b06c1c353"

PROTO_DEPS += "xf86driproto dri2proto"

DEPENDS += "font-util"

PE = "1"
PR = "r0"

SRC_URI += "file://nodolt.patch \
            file://crosscompile.patch"

# Misc build failure for master HEAD
SRC_URI += "file://fix_open_max_preprocessor_error.patch"

SRC_URI[md5sum] = "cafc4e2d4ef6cf6e47f3e7dffeb3346a"
SRC_URI[sha256sum] = "a89f13b166b412930fe418ff50032dd2cde8bb181d8b47b5ca6f848d218fdcf2"

RDEPENDS_${PN} += "xserver-xf86-emgd-bin mesa-dri"

COMPATIBLE_MACHINE = "crownbay"

EXTRA_OECONF += "--enable-dga --enable-dri --enable-dri2"
