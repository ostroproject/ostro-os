SUMMARY = "Cedartrail PowerVR Graphics Driver version [Gold] 1.0 binaries"
DESCRIPTION = "2D, 3D and Media user space driver for Cedartrail platform \
The binaries are covered by the Intel Free Distribution Binary License. \ 
The user must make himself/herself aware of the Licensing terms \
before enabling build of the Cedartrail PowerVR Graphics Driver via \
this recipe.  Please see the README in meta-cedartrail for instructions \
for enabling the build of the driver "
 
LICENSE_FLAGS = "license_${PN}_${PV}"
LICENSE = "Intel Free Distribution Binary License"

LIC_FILES_CHKSUM = " \
    file://${S}/usr/share/doc/psb-video-cdv-0.16/license.txt;md5=b14d99f8d4ed664e9ce95057f0bb5b65  \
    file://${S}/usr/share/doc/pvr-bin-cdv-1.7.788837_10/license.txt;md5=b14d99f8d4ed664e9ce95057f0bb5b65"

INC_PR = "r1"

DEPENDS = "rpm-native"

FILES_${PN} += "${libdir}/dri ${libdir}/pvr/cdv/dri ${libdir}/pvr/cdv ${libdir}/xorg/modules/drivers"
FILES_${PN}-dev += "${libdir}/dri ${libdir}/pvr/cdv/dri ${libdir}/xorg/modules/drivers"
FILES_${PN}-dbg += "${libdir}/xorg/modules/drivers/.debug ${libdir}/dri/.debug ${libdir}/pvr/cdv/dri/.debug"

FILES_${PN} += "${base_libdir}/firmware"
FILES_${PN} += "${sysconfdir}/X11/xorg.conf.d"

FILES_${PN} += "${libdir}/lib*.so"
FILES_${PN}-dev += "${libdir}/lib*.so"
FILES_${PN}-dbg += "${libdir}/.debug"

FILES_${PN} += "${libdir}/pvr/cdv/xorg/modules/drivers"

FILES_${PN} += "${datadir}/doc/psb-video-cdv-0.16/license.txt"
FILES_${PN} += "${datadir}/doc/pvr-bin-cdv-1.7.788837_10/license.txt"


                        
