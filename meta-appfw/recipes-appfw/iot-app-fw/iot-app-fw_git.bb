DESCRIPTION = "Revised mininal application 'framework'."
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "BSD-3-Clause"

LIC_FILES_CHKSUM = "file://LICENSE-BSD;md5=f9f435c1bd3a753365e799edf375fc42"

DEPENDS = "json-c systemd"

SRC_URI = " \
    git://git@github.com/ostroproject/iot-app-fw.git;protocol=https;branch=kli/devel/1.x \
    file://80-container-host0.network \
    file://80-container-ve.network \
    file://appfw-packet-forward.conf \
  "

SRCREV = "ed04e87a583b3ec73c56a629533c1ff74527133a"

inherit autotools pkgconfig systemd

AUTO_LIBNAME_PKGS = ""

S = "${WORKDIR}/git"

# possible package configurations
PACKAGECONFIG ??= ""

FILES_${PN} = "${base_libdir}/systemd/system-generators/iot-service-generator \
               ${base_libdir}/systemd/systemd/applications.target \
               ${libexecdir}/iot-app-fw \
               ${libdir}/systemd/network/80-container-host0.network \
               ${libdir}/systemd/network/80-container-ve.network \
               ${libdir}/sysctl.d/appfw-packet-forward.conf \
"

FILES_${PN}-dbg =+ "${base_libdir}/systemd/system-generators/.debug"

SYSTEMD_PACKAGES      += "${PN}"
SYSTEMD_SERVICE_${PN}  = "applications.target"
SYSTEMD_AUTO_ENABLE    = "enable"

do_install_append () {
    mkdir -p ${D}${libdir}/systemd/network
    cp ../80-container-host0.network ${D}${libdir}/systemd/network
    cp ../80-container-ve.network ${D}${libdir}/systemd/network
    install -m 0755 -o root -g root -d ${D}${libdir}/sysctl.d && \
    install -m 0644 -o root -g root -t ${D}${libdir}/sysctl.d \
        ../appfw-packet-forward.conf
}
