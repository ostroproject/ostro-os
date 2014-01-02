SUMMARY = "Provide a basic init script to generate a random MAC"
DESCRIPTION = "Set the MAC from the config file."
SECTION = "base"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690"

PR = "r0"

inherit update-rc.d

RDEPENDS_${PN} = "ranpwd"

SRC_URI = "file://genmac"

INITSCRIPT_NAME = "genmac"
# Run as early as possible to ensure we are before the networking scripts
INITSCRIPT_PARAMS = "start 39 S ."

do_install() {
	install -d ${D}${sysconfdir} \
	           ${D}${sysconfdir}/init.d
	install -m 0755 ${WORKDIR}/${INITSCRIPT_NAME} ${D}${sysconfdir}/init.d
        cat ${WORKDIR}/${INITSCRIPT_NAME} | \
            sed -e 's,/etc,${sysconfdir},g' \
                -e 's,/usr/sbin,${sbindir},g' \
                -e 's,/var,${localstatedir},g' \
                -e 's,/usr/bin,${bindir},g' \
                -e 's,/usr,${prefix},g' > ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
        chmod 755 ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
}
