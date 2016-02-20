# Enabling Smack support in util-linux enables special support
# in [lib]mount for Smack mount options: they get removed if
# Smack is not active in the current kernel. Important for
# booting with "security=none" when userspace otherwise is
# compiled to use Smack.

PACKAGECONFIG_append_class-target_smack = " smack"
PACKAGECONFIG[smack] = "--with-smack, --without-smack, smack-userspace"
