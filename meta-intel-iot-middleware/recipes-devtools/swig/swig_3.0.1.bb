DESCRIPTION = "SWIG - Simplified Wrapper and Interface Generator"
HOMEPAGE = "http://swig.sourceforge.net/"
LICENSE = "BSD & GPLv3"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e7807a6282784a7dde4c846626b08fc6 \
                    file://LICENSE-GPL;md5=d32239bcb673463ab874e80d47fae504 \
                    file://LICENSE-UNIVERSITIES;md5=8ce9dcc8f7c994de4a408b205c72ba08"

SECTION = "devel"

DEPENDS = "libpcre python"

inherit autotools pythonnative

BBCLASSEXTEND = "native"

DEPENDS_append = " nodejs"

S = "${WORKDIR}/git"
#this is a working revision to use -javascript -node, move to release as soon as possible
SRC_URI = "git://github.com/swig/swig.git;protocol=git;rev=d9cac664620d282aa423d3f0ef55ab9a677156a4"

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
