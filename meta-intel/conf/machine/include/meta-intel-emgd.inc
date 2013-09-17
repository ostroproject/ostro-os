INHERIT += "emgd-gl"
GLSUFFIX = "-emgd"
PACKAGE_EXTRA_ARCHS_append = " ${TUNE_PKGARCH}${GLSUFFIX}"

PREFERRED_PROVIDER_virtual/mesa ?= "mesa-gl"
PREFERRED_PROVIDER_virtual/libgl ?= "mesa-gl"
PREFERRED_PROVIDER_virtual/libgles1 ?= "emgd-driver-bin"
PREFERRED_PROVIDER_virtual/libgles2 ?= "emgd-driver-bin"
PREFERRED_PROVIDER_virtual/egl ?= "emgd-driver-bin"
