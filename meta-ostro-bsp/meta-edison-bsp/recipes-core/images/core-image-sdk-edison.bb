inherit core-image

DESCRIPTION = "Basic image without X support suitable native development. It includes \
the full meta-toolchain, plus development headers and libraries to form a standalone SDK."

IMAGE_FEATURES += "tools-sdk dev-pkgs tools-debug tools-profile"

IMAGE_INSTALL += "kernel-dev"
