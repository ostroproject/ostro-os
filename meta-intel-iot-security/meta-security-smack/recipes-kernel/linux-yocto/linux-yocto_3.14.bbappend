FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# This is the only Smack-related patch from Tizen IVI 3.0.
SRC_URI += " \
file://0001-Smack-Cgroup-filesystem-access.patch \
"
