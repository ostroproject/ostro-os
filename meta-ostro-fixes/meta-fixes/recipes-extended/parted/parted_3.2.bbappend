SRC_URI += "file://UI-Avoid-memory-leaks.patch\
            file://libparted-Fix-memory-leaks.patch\
            file://libparted-Fix-possible-memory-leaks.patch\
"
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
