SRC_URI += "file://0001-extlinux-fix-file-descriptors-leak.patch\
            file://0002-extlinux-fix-memory-leak.patch\
"
FILESEXTRAPATHS_prepend := "${THISDIR}/syslinux:"

