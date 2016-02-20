# Smack patches are included in coreutils v8.22, we just need to enable them.
# The default is not deterministic (enabled if libsmack found), so disable
# explicitly otherwise.
EXTRA_OECONF_SMACK = "--disable-libsmack"
EXTRA_OECONF_SMACK_smack = "--enable-libsmack"
EXTRA_OECONF_append = " ${EXTRA_OECONF_SMACK}"
DEPENDS_append_smack = " smack"
