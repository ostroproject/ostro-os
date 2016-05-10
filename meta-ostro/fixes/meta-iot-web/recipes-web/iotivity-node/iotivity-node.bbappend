FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += "${@ 'file://oc-payload.cc-fix-signed-unsigned-char-issues.patch' if '${SRCREV}' == '38f76790e2d0f4960b0f3360c7bbcdf5a69907f4' else '' }"
