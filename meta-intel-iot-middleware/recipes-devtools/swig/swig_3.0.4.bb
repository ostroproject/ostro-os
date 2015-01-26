DESCRIPTION = "SWIG - Simplified Wrapper and Interface Generator"
HOMEPAGE = "http://swig.sourceforge.net/"
LICENSE = "BSD & GPLv3"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e7807a6282784a7dde4c846626b08fc6 \
                    file://LICENSE-GPL;md5=d32239bcb673463ab874e80d47fae504 \
                    file://LICENSE-UNIVERSITIES;md5=8ce9dcc8f7c994de4a408b205c72ba08"

SECTION = "devel"

DEPENDS = "libpcre python nodejs"

inherit autotools pythonnative

BBCLASSEXTEND = "native"

SRC_URI = "http://prdownloads.sourceforge.net/swig/swig-${PV}.tar.gz"
SRC_URI[md5sum] = "9cb8c0efda39dc6db5f85389e671fb59"
SRC_URI[sha256sum] = "410ffa80ef5535244b500933d70c1b65206333b546ca5a6c89373afb65413795"

EXTRA_OECONF = " \
    --with-python=${PYTHON} \
    --without-allegrocl \
    --without-android \
    --without-boost \
    --without-chicken \
    --without-clisp \
    --without-csharp \
    --without-d \
    --without-gcj \
    --without-go \
    --without-guile \
    --without-java \
    --without-lua \
    --without-mzscheme \
    --without-ocaml \
    --without-octave \
    --without-perl5 \
    --without-pike \
    --without-php \
    --without-python3 \
    --without-r \
    --without-ruby \
    --without-tcl \
    --disable-ccache \
"

do_configure() {
   export NOCONFIGURE="no"; ./autogen.sh
   oe_runconf
}

FILES_${PN} += "${datadir}/*"
FILES_${PN}-native += "${datadir}/*"
