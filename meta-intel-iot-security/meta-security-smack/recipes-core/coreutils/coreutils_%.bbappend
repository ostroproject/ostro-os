# Smack patches are included in coreutils v8.22, we just need to enable them.
EXTRA_OECONF += "--enable-libsmack"
DEPENDS += "smack"
