require cdv-pvr-driver.inc

PR = "${INC_PR}.1"

DEPENDS = "libva"

SRC_URI = "http://repo.meego.com/MeeGo/updates/1.2.0/repos/non-oss/ia32/packages/psb-video-cdv-0.16-1.1.i586.rpm;name=psbrpm \
	   http://repo.meego.com/MeeGo/updates/1.2.0/repos/non-oss/ia32/packages/pvr-bin-cdv-1.7.788837_10-1.1.i586.rpm;name=pvrrpm \
	   http://repo.meego.com/MeeGo/updates/1.2.0/repos/oss/ia32/packages/libwsbm-cdv-1.1.0-3.1.i586.rpm;name=wsbmrpm \
		"
SRC_URI[pvrrpm.md5sum] = "06dbacd7f0f5bb10132eb5477ae9267a"
SRC_URI[pvrrpm.sha256sum] = "1e42c57485e46a1712e26f48df44a2f5305a82ca98afc5bf4f90a93c9631f509"

SRC_URI[psbrpm.md5sum] =  "fd213baa2af33d35e8b552e586b02b90"
SRC_URI[psbrpm.sha256sum] = "cda281798ebbd280b6d2caf2a09961db0d719f929b808c6360c81db323aeee71"

SRC_URI[wsbmrpm.md5sum] = "b8b21ca8325abd7850d197f9bf3071c7"
SRC_URI[wsbmrpm.sha256sum] = "f436386967c1adec5211e662251bd542bbe0b8cd55e1d9f9c203da5ee934d4f0"


S  = "${WORKDIR}/cdv-graphics-drivers_${PV}"

do_configure () {

# Extract  license files from rpms
rpm2cpio ${WORKDIR}/psb-video-cdv-0.16-1.1.i586.rpm |cpio -ivd ./usr/share/doc/psb-video-cdv-0.16/license.txt
rpm2cpio ${WORKDIR}/pvr-bin-cdv-1.7.788837_10-1.1.i586.rpm |cpio -ivd ./usr/share/doc/pvr-bin-cdv-1.7.788837_10/license.txt

}


do_install() {
 	
	
	mv ${WORKDIR}/*.rpm  ${S}	
				
	rpm2cpio ${S}/libwsbm-cdv-1.1.0-3.1.i586.rpm | cpio -id
	
	install -d -m 0755                                    ${D}${libdir}/dri

	install -m 0755 ${S}/usr/lib/*                        ${D}${libdir}/

	rpm2cpio ${S}/psb-video-cdv-0.16-1.1.i586.rpm | cpio -id

	install -d -m 0755				      ${D}${base_libdir}/firmware

	install -m 0755 ${S}/usr/lib/dri/*     		      ${D}${libdir}/dri/

	install -m 0755 ${S}/lib/firmware/*		      ${D}${base_libdir}/firmware

	rpm2cpio ${S}/pvr-bin-cdv-1.7.788837_10-1.1.i586.rpm  | cpio -id

	install -d -m 0755                                    ${D}${libdir}/pvr/cdv/dri

	install -m 0755 ${S}/usr/lib/pvr/cdv/dri/*            ${D}${libdir}/pvr/cdv/dri

	install -d -m 0755                                    ${D}${sysconfdir}/X11/xorg.conf.d
	install -m 0755 ${S}/etc/powervr.ini		      ${D}${sysconfdir}/	
	install -m 0755 ${S}/etc/X11/xorg.conf.d/*            ${D}${sysconfdir}/X11/xorg.conf.d/
	install -m 0755 ${S}/usr/lib/dri/pvr_dri.so    	      ${D}${libdir}/dri/
	install -m 0755 ${S}/usr/lib/*.so.*                   ${D}${libdir}/    

	
	install -m 0755 ${S}/usr/lib/libegl4ogl.so.1.7.788837   			${D}${libdir}/libegl4ogl.so
	install -m 0755 ${S}/usr/lib/libEGL.so.1.7.788837  				${D}${libdir}/libEGL.so
	install -m 0755 ${S}/usr/lib/libGLES_CM.so.1.7.788837 				${D}${libdir}/libGLES_CM.so
	install -m 0755 ${S}/usr/lib/libGLES_CM.so.1.7.788837  				${D}${libdir}/libGLESv1_CM.so
	install -m 0755 ${S}/usr/lib/libGLESv2.so.1.7.788837  				${D}${libdir}/libGLESv2.so
	install -m 0755 ${S}/usr/lib/libglslcompiler.so.1.7.788837 			${D}${libdir}/libglslcompiler.so
	install -m 0755 ${S}/usr/lib/libIMGegl.so.1.7.788837  				${D}${libdir}/libIMGegl.so
	install -m 0755 ${S}/usr/lib/libOpenVG.so.1.7.788837 				${D}${libdir}/libOpenVG.so
	install -m 0755 ${S}/usr/lib/libOpenVGU.so.1.7.788837 				${D}${libdir}/libOpenVGU.so
	install -m 0755 ${S}/usr/lib/libpvr2d.so.1.7.788837  				${D}${libdir}/libpvr2d.so
	install -m 0755 ${S}/usr/lib/libPVROGL_MESA.so.1.7.788837 			${D}${libdir}/libPVROGL_MESA.so
	install -m 0755 ${S}/usr/lib/libpvrPVR2D_BLITWSEGL.so.1.7.788837 		${D}${libdir}/libpvrPVR2D_BLITWSEGL.so
	install -m 0755 ${S}/usr/lib/libpvrPVR2D_DRIWSEGL.so.1.7.788837 		${D}${libdir}/libpvrPVR2D_DRIWSEGL.so
	install -m 0755 ${S}/usr/lib/libpvrPVR2D_FLIPWSEGL.so.1.7.788837  		${D}${libdir}/libpvrPVR2D_FLIPWSEGL.so
	install -m 0755 ${S}/usr/lib/libpvrPVR2D_LINUXFBWSEGL.so.1.7.788837  		${D}${libdir}/libpvrPVR2D_LINUXFBWSEGL.so
	install -m 0755 ${S}/usr/lib/libPVRScopeServices.so.1.7.788837  		${D}${libdir}/libPVRScopeServices.so
	install -m 0755 ${S}/usr/lib/libsrv_init.so.1.7.788837  			${D}${libdir}/libsrv_init.so
	install -m 0755 ${S}/usr/lib/libsrv_um.so.1.7.788837 				${D}${libdir}/libsrv_um.so
	install -m 0755 ${S}/usr/lib/libusc.so.1.7.788837 				${D}${libdir}/libusc.so

	install -m 0755 ${S}/usr/lib/pvr/cdv/*.so.*           				${D}${libdir}/pvr/cdv/    

	install -d -m 0755 ${D}${libdir}/pvr/cdv/xorg/modules/drivers
	install -m 0755 ${S}/usr/lib/pvr/cdv/xorg/modules/drivers/* 			${D}${libdir}/pvr/cdv/xorg/modules/drivers/

    	install -d -m 0755                                    				${D}${libdir}/xorg/modules/drivers
   
	install -m 0755 ${S}/usr/lib/xorg/modules/drivers/*   				${D}${libdir}/xorg/modules/drivers/
   
	install -d -m 0755 ${D}${datadir}/doc/psb-video-cdv-0.16
	install -d -m 0755 ${D}${datadir}/doc/pvr-bin-cdv-1.7.788837_10

	install -m 0755 ${S}/usr/share/doc/psb-video-cdv-0.16/license.txt 		${D}${datadir}/doc/psb-video-cdv-0.16/license.txt
	install -m 0755 ${S}/usr/share/doc/pvr-bin-cdv-1.7.788837_10/license.txt	${D}${datadir}/doc/pvr-bin-cdv-1.7.788837_10/license.txt

}
