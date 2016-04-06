DESCRIPTION = "Broadcom wifi driver for the 43340"
LICENSE = "GPLv2"

SRC_URI = "git://github.com/01org/edison-bcm43340.git;branch=master;protocol=git;rev=9d609e1ffadbf8895a701e6283392bb54bd962f9"

LIC_FILES_CHKSUM = "file://COPYING;md5=f9986853fb3b3403700e7535a392d014"

# The module is compatible with Edison kernel only
COMPATIBLE_MACHINE="edison"

inherit module

PV = "1.141"
PR = "r49"

S = "${WORKDIR}/git/"

