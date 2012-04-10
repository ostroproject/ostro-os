require cdv-pvr-driver.inc

PR = "${INC_PR}.0"

DEPENDS = "libva"

SRC_URI = "${MEEGO_MIRROR}/non-oss/MeeGo_1.2.0_CedarTrail/i586/psb-video-cdv-0.12-1.1.i586.rpm;name=psbrpm \ 
	   ${MEEGO_MIRROR}/oss/standard/i586/libwsbm-cdv-1.1.0-3.1.i586.rpm;name=wsbmrpm \
	   ${MEEGO_MIRROR}/non-oss/MeeGo_1.2.0_CedarTrail/i586/pvr-bin-cdv-1.7.788837_05-1.1.i586.rpm;name=pvrrpm \
           "

SRC_URI[pvrrpm.md5sum] = "951fa9edcbc2a3ddb30450079869362e"
SRC_URI[pvrrpm.sha256sum] = "537dd8a98ac2e3a101063abc62682c3be8c37ac29782a876eafce113ffa5b421"

SRC_URI[psbrpm.md5sum] =  "d4b6b383722264f3b781aeb240c88037"
SRC_URI[psbrpm.sha256sum] = "e88f95fc73a79adf76ee33d3d9874cec23bb1afe8149d7dc5842d67e58da72f5"

SRC_URI[wsbmrpm.md5sum] = "8d90436b151ddf72f620771f2552b597"
SRC_URI[wsbmrpm.sha256sum] = "82f78f47c151f0e7d567574ee372504e5b395fb13796caa765f9c30754b5bf63"


S  = "${WORKDIR}/cdv-graphics-drivers_${PV}"

do_configure () {

# Extract  license files from rpms
rpm2cpio ${WORKDIR}/psb-video-cdv-0.12-1.1.i586.rpm |cpio -ivd ./usr/share/doc/psb-video-cdv-0.12/license.txt
rpm2cpio ${WORKDIR}/pvr-bin-cdv-1.7.788837_05-1.1.i586.rpm |cpio -ivd ./usr/share/doc/pvr-bin-cdv-1.7.788837_05/license.txt

}


do_install() {
 	
	
	mv ${WORKDIR}/*.rpm  ${S}	
				
	rpm2cpio ${S}/libwsbm-cdv-1.1.0-3.1.i586.rpm | cpio -id
	
	install -d -m 0755                                    ${D}${libdir}/dri

	install -m 0755 ${S}/usr/lib/*                        ${D}${libdir}/

	rpm2cpio ${S}/psb-video-cdv-0.12-1.1.i586.rpm | cpio -id


	install -d -m 0755				      ${D}${base_libdir}/firmware

	install -m 0755 ${S}/usr/lib/dri/*     		      ${D}${libdir}/dri/

	install -m 0755 ${S}/lib/firmware/*		      ${D}${base_libdir}/firmware

	rpm2cpio ${S}/pvr-bin-cdv-1.7.788837_05-1.1.i586.rpm  | cpio -id
	
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
   
	install -d -m 0755 ${D}${datadir}/doc/psb-video-cdv-0.12
	install -d -m 0755 ${D}${datadir}/doc/pvr-bin-cdv-1.7.788837_05

    	install -m 0755 ${S}/usr/share/doc/psb-video-cdv-0.12/license.txt 		${D}${datadir}/doc/psb-video-cdv-0.12/license.txt
	install -m 0755 ${S}/usr/share/doc/pvr-bin-cdv-1.7.788837_05/license.txt	${D}${datadir}/doc/pvr-bin-cdv-1.7.788837_05/license.txt

}
