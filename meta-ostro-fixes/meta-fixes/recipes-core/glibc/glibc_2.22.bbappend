FILESEXTRAPATHS_prepend := "${THISDIR}/glibc:"

SRC_URI_append = " file://0001-CVE-2015-7547-getaddrinfo-stack-based-buffer-overflo.patch"
