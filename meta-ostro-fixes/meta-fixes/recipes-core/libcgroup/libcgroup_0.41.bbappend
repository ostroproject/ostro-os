SRC_URI += "file://0001-tests-handle-strings-right.patch \
            file://0002-config.c-fix-check-to-fail-if-memory-allocation-does.patch \
            file://0003-api.c-fix-a-double-free.patch \
            file://0004-cgrulesengd.c-close-non-negative-descriptors.patch \
            file://0005-cgsnapshot.c-free-memory-after-use.patch \
            file://0006-cgsnapshot.c-initialize-controller-matrix-before-sea.patch"
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

