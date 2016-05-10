LICENSE="GPLv2"
LIC_FILES_CHKSUM="file://COPYING;md5=b234ee4d69f5fce4486a80fdaf4a4263"

SRC_URI=" \
    git://git@github.com/megastep/makeself.git;protocol=https \
"	

SRCREV="a16bc8c4eb4fc8abaa4ea847e051ba164df51f2a"

S="${WORKDIR}/git"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${S}/makeself.1 ${D}${bindir}/ 
    install -m 0755 ${S}/makeself.lsm ${D}${bindir}/ 
    install -m 0755 ${S}/makeself.sh ${D}${bindir}/ 
    install -m 0755 ${S}/makeself-header.sh ${D}${bindir}/ 
}


BBCLASSEXTEND = "native"
