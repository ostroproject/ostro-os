require ostro-image.bb

DESCRIPTION = "Development image for Ostro OS on-device development. It includes \ 
everything within ostro-image plus a native toolchain, profiling and debug tools."

IMAGE_FEATURES += "tools-debug tools-develop tools-profile"
