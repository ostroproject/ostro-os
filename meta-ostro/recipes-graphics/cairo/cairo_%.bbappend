# Makes cairo available even if X11 is not included in the DISTRO_FEATURES
# Required for building meta-java without adding X11.

# enable x-lib; otherwise gtk+ will not build (which itself is dependency for java)
EXTRA_OECONF_append = " -enable-xlib"
EXTRA_OECONF_remove = " --disable-xlib"
# Add dependencies to fix QA errors
DEPENDS_append = " ${X11DEPENDS}"
