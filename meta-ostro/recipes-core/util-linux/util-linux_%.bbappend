# util-linux-native tooling enables to use either lzo or lz4 compression.
# We prefer lz4 so switch to use it.
#
# Upstream-Status: Inappropriate [Downstream configuration] 

DEPENDS_remove_class-native = "lzo-native"
DEPENDS_remove_class-nativesdk = "lzo-native"
DEPENDS_append_class-native = " lz4-native"
DEPENDS_append_class-nativesdk = " lz4-native"
