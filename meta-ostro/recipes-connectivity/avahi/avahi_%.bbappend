# libnss-mdns is not supported, so remove it from the RRECOMMENDS
RRECOMMENDS_avahi-daemon_remove_libc-glibc = " libnss-mdns"
RRECOMMENDS_${PN}_remove_libc-glibc = " libnss-mdns"
