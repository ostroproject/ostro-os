#
# Copyright (C) 2011 Intel Corporation.
# Author:  Kishore Bodke 
# kishore.k.bodke@intel.com
#

require recipes-sato/images/core-image-sato.bb

IMAGE_INSTALL += "web-webkit bigbuckbunny-ogg  ogg-CC-BY-3.0-music-samples"

LICENSE = "MIT"

PR = "r0"
