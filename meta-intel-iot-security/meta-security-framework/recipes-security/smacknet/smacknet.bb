#SMACKNET Description
SUMMARY = "Smack network labels configuration"
DESCRIPTION = "Provide service that will be labeling the network rules"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/BSD-3-Clause;md5=550794465ba0ec5312d6919e203a55f9"
RDEPENDS_${PN} = "python"

SRC_URI += "file://smacknet \
        file://smacknet.service \
	"
S = "${WORKDIR}"

inherit systemd

inherit distro_features_check
REQUIRED_DISTRO_FEATURES = "smack"

#netlabel configuration service
SYSTEMD_SERVICE_${PN} = "smacknet.service"
SYSTEMD_AUTO_ENABLE = "enable"
do_install(){
        install -d ${D}${bindir}
        install -m 0551 ${WORKDIR}/smacknet ${D}${bindir}

        install -d -m 755 ${D}${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/smacknet.service ${D}${systemd_unitdir}/system
        sed -i -e 's,@BINDIR@,${bindir},g' ${D}${systemd_unitdir}/system/smacknet.service
}
   
