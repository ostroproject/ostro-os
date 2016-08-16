require openjdk-7-common.inc

LIC_FILES_CHKSUM = "file://COPYING;md5=59530bdf33659b29e73d4adb9f9f6552"

FILESPATH =. "${FILE_DIRNAME}/patches-openjdk-7:"

inherit distro_features_check

REQUIRED_DISTRO_FEATURES = "x11"

PR = "${INC_PR}.1"

SRC_URI[iced.md5sum] = "cb66b595860c3d99a87c3a853667c145"
SRC_URI[iced.sha256sum] = "d8bce93bd33b299a52236f03fb57d42ae9de808c8337e6185930799dbfc78795"

SRC_URI[corba.md5sum] = "3345d1939663d1ef94459cf215b76b3f"
SRC_URI[corba.sha256sum] = "427969fdd78513a11ddd9d5131a068e0b26ca2c8f14951bf8b161fecd07fe77f"

SRC_URI[jaxp.md5sum] = "872a458cde954124eee9913e6ea906b0"
SRC_URI[jaxp.sha256sum] = "7bb5e1bc9f0807061e157aeb356dd0e3b9fa019fb316beee3aa0181a335ba37a"

SRC_URI[jaxws.md5sum] = "d0d559ca0d797c5dc9640bfa277a23c5"
SRC_URI[jaxws.sha256sum] = "4e759ade7e47713f6f26afc1ffcd02f2edf967582fae2ec6b4d73dc81be926d0"

SRC_URI[jdk.md5sum] = "13fa99cc310f27818867e8a9d0841892"
SRC_URI[jdk.sha256sum] = "cd3810553b1066c21f2fe08a73de72e38ba7e72295cd32dec70db481a24421ba"

SRC_URI[langtools.md5sum] = "2e951b311d0cfbd7ebc6e9fbb75de891"
SRC_URI[langtools.sha256sum] = "6c6c676c60af61638a0c3176f0312fcc0abad16d1d3cdbe11aeefcc3357a78d9"

SRC_URI[openjdk.md5sum] = "48d9f0e76f92d18aff1b9379b052b0cb"
SRC_URI[openjdk.sha256sum] = "c66f56a91a6fa9e3c889bbbc5432a4e082b7d3735188fb508fa7ec70c142abdb"

# hotspot changeset taken from hotspot/tags
SRC_URI[hotspot.md5sum] = "7e1bdaf4385c3b7e77d3599c52151485"
SRC_URI[hotspot.sha256sum] = "43983232fb10abeac99478e7045c04a93fef86185e2b9ee9c7b46f2903441cfc"

###############################################################################
# PATCHES - split up to allow overriding them separately
OEPATCHES = "\
    file://build-hacks.patch \
    file://fix_hotspot_crosscompile.patch \
    file://icedtea-makefile-unzip.patch \
"

ICEDTEAPATCHES = "\
    file://icedtea-zero-hotspotfix.patch;apply=no \
    file://icedtea-jdk-nio-use-host-cc.patch;apply=no \
    file://icedtea-jdk-rmi-crosscompile.patch;apply=no \
    file://icedtea-crosscompile-fix.patch;apply=no \
    file://icedtea-xawt-crosscompile-fix.patch;apply=no \
    file://icedtea-jdk-unzip.patch;apply=no \
    file://icedtea-dtrace-std_h.patch;apply=no \
"

DISTRIBUTION_PATCHES = "\
    patches/icedtea-zero-hotspotfix.patch \
    patches/icedtea-jdk-nio-use-host-cc.patch \
    patches/icedtea-jdk-rmi-crosscompile.patch \
    patches/icedtea-crosscompile-fix.patch \
    patches/icedtea-xawt-crosscompile-fix.patch \
    patches/icedtea-jdk-unzip.patch \
    patches/icedtea-dtrace-std_h.patch \
"

export DISTRIBUTION_PATCHES
