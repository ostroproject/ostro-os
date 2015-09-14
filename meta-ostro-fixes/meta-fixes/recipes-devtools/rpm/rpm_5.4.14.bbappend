FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\
     file://0001-rpm5-Extend-librpm-to-support-rpmtsTxn.patch \
     file://0002-rpm5-Fix-rpmcliFini-that-subsequent-cli-creation-wor.patch \
     file://0003-rpm5-Fake-chown-and-chmode-for-root-root-if-the-owne.patch \
"
