# Makes gtk+ available even if X11 is not included in the DISTRO_FEATURES
# Required for building meta-java without adding X11.

# Add dependencies to fix QA errors
DEPENDS_append = " ${X11DEPENDS}"
# override distro feature check
ANY_OF_DISTRO_FEATURES_remove = " x11 directfb"
