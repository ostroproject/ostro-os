# This dependency is redundant because gnome-common-native is
# sufficient and gets pulled in by gnomebase.bbclass.
#
# We remove it here to avoid building a useless target
# component.
DEPENDS_remove = "gnome-common"
