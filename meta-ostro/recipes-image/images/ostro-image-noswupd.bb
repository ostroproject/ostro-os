SUMMARY = "Ostro image for local builds with swupd disabled."

# Image configuration cannot always be done using the _pn-ostro-image
# notation, because then the configuration of the base image and
# potential virtual images created from it would be different.
#
# Instead extend these variables. We cannot just use OSTRO_IMAGE_EXTRA_FEATURES
# and OSTRO_IMAGE_EXTRA_INSTALL because those affect all images based
# on ostro-image.bbclass.
OSTRO_IMAGE_NOSWUPD_EXTRA_FEATURES ?= "${OSTRO_IMAGE_FEATURES_REFERENCE}"
OSTRO_IMAGE_NOSWUPD_EXTRA_INSTALL ?= "${OSTRO_IMAGE_INSTALL_REFERENCE}"
OSTRO_IMAGE_EXTRA_FEATURES += "${OSTRO_IMAGE_NOSWUPD_EXTRA_FEATURES}"
OSTRO_IMAGE_EXTRA_INSTALL += "${OSTRO_IMAGE_NOSWUPD_EXTRA_INSTALL}"

# If the default "ostro-image-noswupd" name is
# undesirable, write a custom image recipe similar to this one here
# or customize the image file names.
#
# Example for customization in local.conf when building ostro-image-noswupd.bb:
# IMAGE_BASENAME_pn-ostro-image-noswupd = "my-ostro-image-reference"
# OSTRO_IMAGE_NOSWUPD_EXTRA_INSTALL_append = "my-own-package"
# OSTRO_IMAGE_NOSWUPD_EXTRA_FEATURES_append = "dev-pkgs"

inherit ostro-image
