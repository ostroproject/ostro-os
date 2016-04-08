SUMMARY = "Tools to generate block map (AKA bmap) and flash images using bmap"
DESCRIPTION = "Bmap-tools - tools to generate block map (AKA bmap) and flash images using \
bmap. Bmaptool is a generic tool for creating the block map (bmap) for a file, \
and copying files using the block map. The idea is that large file containing \
unused blocks, like raw system image files, can be copied or flashed a lot \
faster with bmaptool than with traditional tools like "dd" or "cp"."
HOMEPAGE = "http://git.infradead.org/users/dedekind/bmap-tools.git"
SECTION = "devel/python"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=b234ee4d69f5fce4486a80fdaf4a4263"

SRC_URI = "ftp://ftp.infradead.org/pub/bmap-tools/bmap-tools-${PV}.tgz"
SRC_URI[md5sum] = "92cdad1cb4dfa0cca7176c8e22752616"
SRC_URI[sha256sum] = "cc6c7f7dc0a37e2a32deb127308e24e6c4b80bfb54f3803c308efab02bf2d434"

inherit setuptools deploy

RDEPENDS_${PN} += "python-compression python-core python-unittest"

BBCLASSEXTEND = "nativesdk native"

do_install_append_class-native() {
    sed -i -e 's|^#!.*/usr/bin/env python|#! /usr/bin/env nativepython|' ${D}${bindir}/bmaptool
}

do_deploy[sstate-outputdirs] = "${DEPLOY_DIR_TOOLS}"
do_deploy_class-native() {
    cp bmaptool __main__.py
    python -m zipfile -c bmaptool.zip bmaptools __main__.py
    echo '#!/usr/bin/env python' | cat - bmaptool.zip > bmaptool-standalone
    install -d ${DEPLOYDIR}
    install -m 0755 bmaptool-standalone ${DEPLOYDIR}/bmaptool-${PV}
    rm -f ${DEPLOYDIR}/bmaptool
    ln -sf ./bmaptool-${PV} ${DEPLOYDIR}/bmaptool
}

do_deploy() {
        :
}

addtask deploy before do_package after do_install
