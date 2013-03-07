DESCRIPTION = "Video Acceleration Add-ons for Intel BSPs"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

PR = "r1"

def map_valibs(d):
    # The emgd mixvideo implementation requires libva-x11/tpi/glx/egl
    if base_contains('MACHINE_FEATURES', 'va-impl-mixvideo', "1", "0", d) == "1":
       return "libva libva-x11 libva-tpi libva-glx libva-egl"
    # The intel implementation requires the libva-intel-driver package
    if base_contains('MACHINE_FEATURES', 'va-impl-intel', "1", "0", d) == "1":
       return "libva libva-intel-driver"
    # All meta-intel video acceleration requires libva
    return "libva"

VA_IMPL = "${@map_valibs(d)}"

PACKAGES = "\
    va-intel \
    "

ALLOW_EMPTY_va-intel = "1"

RDEPENDS_va-intel = " \
    ${VA_IMPL} \
    "

COMPATIBLE_HOST = '(i.86|x86_64).*-linux*'
