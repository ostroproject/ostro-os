FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://egl-mesa-screen-surface-build-fix.patch \
            file://egl-mesa-screen-surface-query.patch \
            file://0001-xeglgears-Make-EGL_KHR_image-usage-portable.patch"
