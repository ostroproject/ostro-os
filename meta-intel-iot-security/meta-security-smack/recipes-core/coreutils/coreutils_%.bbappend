# Smack patches are included in coreutils v8.22, we just need to enable them.
EXTRA_OECONF_append_smack = " --enable-libsmack"
DEPENDS_append_smack = " smack"
