DESCRIPTION = "Bonjour, also known as zero-configuration networking, enables automatic discovery of computers, devices, and services on IP networks."
HOMEPAGE = "http://developer.apple.com/networking/bonjour/"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=31c50371921e0fb731003bbc665f29bf"

PR = "r1"

SRC_URI = "http://opensource.apple.com/tarballs/mDNSResponder/mDNSResponder-${PV}.tar.gz \
           file://build.patch \
           file://mdns.service \
"

SRC_URI[md5sum] = "39142ab70bd82a096801ce346f86cbab"
SRC_URI[sha256sum] = "c6ad1d53c28d28c0e3689bdf5efd9ce6f5c4c3692e8ad76e5eeb4d0c248929ac"

PARALLEL_MAKE = ""

S = "${WORKDIR}/mDNSResponder-544"

do_compile() {
    cd mDNSPosix
    oe_runmake os=linux DEBUG=0
}

do_install () {
    install -d ${D}${sbindir}
    install -m 0755 mDNSPosix/build/prod/mdnsd ${D}${sbindir}

    install -d ${D}${libdir}
    cp mDNSPosix/build/prod/libdns_sd.so ${D}${libdir}/libdns_sd.so.1
    chmod 0644 ${D}${libdir}/libdns_sd.so.1
    ln -s libdns_sd.so.1 ${D}${libdir}/libdns_sd.so

    install -d ${D}${includedir}
    install -m 0644 mDNSShared/dns_sd.h ${D}${includedir}

    install -d ${D}${mandir}/man8
    install -m 0644 mDNSShared/mDNSResponder.8 ${D}${mandir}/man8/mdnsd.8

    install -d ${D}${bindir}
    install -m 0755  Clients/build/dns-sd ${D}${bindir}

    install -d ${D}${libdir}
    oe_libinstall -C mDNSPosix/build/prod -so libnss_mdns-0.2 ${D}${libdir}
    ln -s libnss_mdns-0.2.so ${D}${libdir}/libnss_mdns.so.2

    install -d ${D}${sysconfdir}
    install -m 0644 mDNSPosix/nss_mdns.conf ${D}${sysconfdir}

    install -d ${D}${mandir}/man5
    install -m 0644 mDNSPosix/nss_mdns.conf.5 ${D}${mandir}/man5

    install -d ${D}${mandir}/man8
    install -m 0644 mDNSPosix/libnss_mdns.8 ${D}${mandir}/man8

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${WORKDIR}/mdns.service ${D}${systemd_unitdir}/system/
}

pkg_postinst_${PN} () {
    sed -e '/^hosts:/s/\s*\<mdns\>//' \
        -e 's/\(^hosts:.*\)\(\<files\>\)\(.*\)\(\<dns\>\)\(.*\)/\1\2 mdns\3\4\5/' \
        -i $D/etc/nsswitch.conf
}

pkg_prerm_${PN} () {
    sed -e '/^hosts:/s/\s*\<mdns\>//' \
        -e '/^hosts:/s/\s*mdns//' \
        -i $D/etc/nsswitch.conf
}

inherit systemd

SYSTEMD_SERVICE_${PN} = "mdns.service"

FILES_${PN} += "${systemd_unitdir}/system/mdns.service"
