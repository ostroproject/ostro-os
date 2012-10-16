SRC_URI += "file://nodolt.patch \
            file://crosscompile.patch"

# Misc build failure for master HEAD
SRC_URI += "file://fix_open_max_preprocessor_error.patch"

# What once were warnings now are errors, fix those up
SRC_URI += "file://werror-address-fix.patch \
            file://ptr-to-int-cast-fix.patch"

PROTO_DEPS += "xf86driproto dri2proto"
DEPENDS += "font-util"
EXTRA_OECONF += "--enable-dri --enable-dri2 --enable-dga"

LIC_FILES_CHKSUM = "file://COPYING;md5=3dd2bbe3563837f80ed8926b06c1c353"

SRC_URI[md5sum] = "5bef6839a76d029204ab31aa2fcb5201"
SRC_URI[sha256sum] = "864831f51e841ff37f2445d1c85b86b559c8860a435fb496aead4f256a2b141d"

PR = "r2"
