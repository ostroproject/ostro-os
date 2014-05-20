PACKAGES =+ " libdns-sd"
EXTRA_OECONF =+ " --enable-compat-libdns_sd"
FILES_libdns-sd = "${libdir}/libdns_sd.so.*"
FILES_libdns-sd-dev = "${includedir}/avahi-compat-libdns_sd/dns_sd.h \
                       ${libdir}/libdns_sd.so"
