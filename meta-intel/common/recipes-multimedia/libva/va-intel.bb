DESCRIPTION = "Video Acceleration Add-ons for Intel BSPs"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

PR = "r0"

VA_IMPL = "${@base_contains('MACHINE_FEATURES', 'gst-va-mixvideo', \
          'libva libva-x11 libva-tpi libva-glx libva-egl', \
          'libva libva-intel-driver', d)}"

PACKAGES = "\
    va-intel \
    "

ALLOW_EMPTY = "1"

RDEPENDS_va-intel = " \
    ${VA_IMPL} \
    "

COMPATIBLE_HOST = '(i.86|x86_64).*-linux*'
