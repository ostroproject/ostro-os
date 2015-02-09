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
SRC_URI[md5sum] = "dcb9638324461b9baba8e044fe59031d"
SRC_URI[sha256sum] = "9f4cb9e8f213f041853646f58fe5e8428d63250d05f5c943b6fa759c77322a3c"

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
