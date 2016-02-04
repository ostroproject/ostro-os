# libpcre_%.bbappend
#
# Configure to build with proper suppot to utf-8, required
# by Soletta's string node types.

EXTRA_OECONF += "\
    --enable-utf8 \
    --enable-unicode-properties \
"
