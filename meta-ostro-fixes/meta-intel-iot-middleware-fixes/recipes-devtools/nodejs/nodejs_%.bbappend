# nodejs_0.10.35.bb rev 4860492 uses:
# DEPENDS = "openssl"
# DEPENDS_class-target = "nodejs-native"
#
# The second line *overrides* the first when when compiling
# for the target, despite depending on openssl in both cases.
# What must have been intended is appending to DEPENDS, like
# this:
# DEPENDS_append_class-target = "nodejs-native"
#
# Here we fix this by simply appending openssl unconditionally.
DEPENDS_append = " openssl"
