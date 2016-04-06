# Configure RPM to not use external beecrypt crypto library. This means less
# dependencies and thus smaller maintenance burden.
#
PACKAGECONFIG_remove = "beecrypt"
