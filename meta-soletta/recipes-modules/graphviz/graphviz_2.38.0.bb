SUMMARY = "Graphviz - Graph Visualization Software."
DESCRIPTION = "Graphviz is open source graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and netorks. It has important applications in networking, bioinformatics,  software engineering, database and web design, machine learning, and in visual interfaces for other technical domains."
HOMEPAGE = "http://www.graphviz.org/"
SECTION = "graphics"
LICENSE = "EPL-1.0"
LIC_FILES_CHKSUM = "file://COPYING;beginline=1;endline=2;md5=737cf7b11c0759e6d3b0d6cb08b7c4f8"

DEPENDS += "graphviz-native bison flex libtool zlib"
DEPENDS_class-native = ""

SRC_URI_BASE = "${DEBIAN_MIRROR}/main/g/${BPN}/${BPN}_${PV}.orig.tar.gz;name=archive \
                ${DEBIAN_MIRROR}/main/g/${BPN}/${BPN}_${PV}-7.debian.tar.xz;name=patch \
"

SRC_URI = "${SRC_URI_BASE} \
        file://graphviz-engine-layout.service \
        file://graphviz_no_mkdef_build.patch"

SRC_URI_class-native = "${SRC_URI_BASE}"

SRC_URI[archive.md5sum] = "5b6a829b2ac94efcd5fa3c223ed6d3ae"
SRC_URI[archive.sha256sum] = "81aa238d9d4a010afa73a9d2a704fc3221c731e1e06577c2ab3496bdef67859e"
SRC_URI[patch.md5sum] = "5cbcff92169d682471cdfdf58d215098"
SRC_URI[patch.sha256sum] = "312ab8215fbe1800664675cfc284aecfeff3ce699407523b5bdefee64cf1a53c"

SYSTEMD_PATH = "${systemd_unitdir}/system/"
AUTOSTART_SYSTEMD_PATH = "/etc/systemd/system/multi-user.target.wants/"

FILES_${PN} += " \
    ${SYSTEMD_PATH}graphviz-engine-layout.service \
    ${AUTOSTART_SYSTEMD_PATH}graphviz-engine-layout.service \
"

inherit autotools-brokensep pkgconfig

LDFLAGS += "-Wunused-but-set-variable -Wmaybe-uninitialized -Wunused-variable"

PACKAGECONFIG_append = " ${@bb.utils.contains('DISTRO_FEATURES', 'x11', 'X11', '', d)}"
PACKAGECONFIG_class-native ??= ""

PACKAGECONFIG[sfdp] = "--enable-sfdp=yes, --disable-sfdp, ,"
PACKAGECONFIG[swig] = "--enable-swig=yes, --disable-swig, swig,"
PACKAGECONFIG[lua] = "--enable-lua=yes, --disable-lua, lua,"
PACKAGECONFIG[cairo] = "--with-pangocairo=yes, --with-pangocairo=no, cairo,"
PACKAGECONFIG[tcl] = "--enable-tcl=yes --with-tclsh=tclsh, --disable-tcl, tcl, tcl"
PACKAGECONFIG[glut] = "--with-glut=yes, --without-glut, mesa-glut,"
PACKAGECONFIG[gtk] = "--with-gtk=yes, --without-gtk, gtk+,"
PACKAGECONFIG[expect] = "--with-expect=yes, --without-expect, expect,"
PACKAGECONFIG[ghost] = "--with-ghostscript=yes, --without-ghostscript, ghostscript,"
PACKAGECONFIG[fontconfig] = "--with-fontconfig=yes, --without-fontconfig, fontconfig,"
PACKAGECONFIG[freetype] = "--with-freetype2=yes, --with-freetype2=no, freetype,"
PACKAGECONFIG[poppler] = "--with-poppler=yes, --with-poppler=no, poppler,"
PACKAGECONFIG[guile] = "--with-guile=yes, --with-guile=no, guile,"
PACKAGECONFIG[php] = "--with-php=yes, --with-php=no, php,"
PACKAGECONFIG[perl] = "--with-perl=yes, --with-perl=no, perl,"
PACKAGECONFIG[python] = "--with-python=yes, --with-python=no, python ,"
PACKAGECONFIG[ruby] = "--with-ruby=yes, --with-ruby=no, ruby, "
PACKAGECONFIG[qt] = "--with-qt=yes, --with-qt=no, qte,"
PACKAGECONFIG[glade] = "--with-glade=yes, --with-glade=no, glade3,"
PACKAGECONFIG[libgd] = "--with-libgd=yes, --with-libgd=no, libglade,"
PACKAGECONFIG[png] = "--with-libpng=yes, --with-libpng=no, libpng,"
PACKAGECONFIG[rsvg] = "--with-rsvg=yes, --with-rsvg=no, librsvg, librsvg"
PACKAGECONFIG[pixbuf] = "--with-gdk=yes --with-gdk-pixbuf=yes, --with-gdk=no --with-gdk-pixbuf=no, gdk-pixbuf,"
PACKAGECONFIG[X11] = "--with-x, --without-x, libx11 virtual/libx11 ,"

EXTRA_OECONF = "  --enable-ltdl"

EXTRA_OECONF += " \
    --with-pangocairo=no \
    --enable-sharp=no \
    --enable-java=no \
    --enable-ocaml=no \
    --enable-r=no \
    --with-devil=no \
    --with-lasi=no \
    --with-gtkgl=no \
    --with-gtkglext=no \
    --with-gts=no \
    --with-ann=no \
    --with-ortho=no \
    --with-digcola=no \
    --with-smyrna=no \
    --with-ipsepcola=no \
    -with-gdk-pixbuf=no \
    --without-gtk \
     "


EXTRA_OECONF_class-native = " \
    --disable-ltdl \
    --enable-sharp=no \
    --enable-java=no \
    --enable-ocaml=no \
    --enable-r=no \
    --with-devil=no \
    --with-lasi=no \
    --with-gtkgl=no \
    --with-gtkglext=no \
    --with-gts=no \
    --with-ann=no \
    --with-ortho=no \
    --with-digcola=no \
    --with-smyrna=no \
    --with-ipsepcola=no \
    --without-gtk \
     "

debian_do_patch() {
    cd ${S}
    while read line; do patch -p1 < ${WORKDIR}/debian/patches/$line; done < ${WORKDIR}/debian/patches/series
}

python do_patch() {
    bb.build.exec_func('debian_do_patch', d)
    bb.build.exec_func('patch_do_patch', d)
}

do_configure_prepend () {
    if [ "${PN}" != "graphviz-native" ]; then
        chmod -R +x ${WORKDIR}/graphviz-${PV}/*
        ./autogen.sh --host x86_64-unknown-linux-gnu
    fi
}

do_configure_append () {
    # copy mkdefs from the native graphviz build
    if [ "${PN}" != "graphviz-native" ]; then
        cp ${STAGING_BINDIR_NATIVE}/graphviz-${PV}/mkdefs ${S}/lib/gvpr/.
    fi
}

do_configure_class-native () {
   ./configure
}

do_compile_class-native () {
    oe_runmake -C ${WORKDIR}/graphviz-${PV}/lib/gvpr mkdefs
}

do_install_class-native () {
    install -d ${D}${bindir}/graphviz-${PV}
    install -m 755 ${WORKDIR}/graphviz-${PV}/lib/gvpr/mkdefs ${D}${bindir}/graphviz-${PV}/
}

do_install_append () {
    if [ "${PN}" != "graphviz-native" ]; then
        install -d ${D}${SYSTEMD_PATH}
        install -d ${D}${AUTOSTART_SYSTEMD_PATH}
        install -m 0755 ${WORKDIR}/graphviz-engine-layout.service ${D}${SYSTEMD_PATH}
        ln -sf ${SYSTEMD_PATH}graphviz-engine-layout.service ${D}${AUTOSTART_SYSTEMD_PATH}graphviz-engine-layout.service
    fi
}

INSANE_SKIP_${PN} += "dev-so file-rdeps"

RDEPENDS_${PN} = "libxml2 libcroco"
RDEPENDS_class-native = ""

BBCLASSEXTEND = "native"
