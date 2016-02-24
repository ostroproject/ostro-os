# Configure RPM to not use external beecrypt crypto library. This means less
# dependencies and thus smaller maintenance burden.
#
PACKAGECONFIG_remove = "beecrypt"

# Temporarily backport OE-Core rev ed1c47e7c621491b892fb82bd18644dba42212b9
# to be able to use --with-beecrypt=internal with PACKAGECONFIG.
# This backport will be removed once we pull from OE-Core next time.
#
# Upstream-Status: Backport [ed1c47e7c621491b892fb82bd18644dba42212b9]
PACKAGECONFIG[beecrypt] = "--with-beecrypt=external,--with-beecrypt=internal,beecrypt,"
