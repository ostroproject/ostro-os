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

RREPLACES_${PN} = "swig"

DEPENDS_append = " nodejs"

S = "${WORKDIR}/git"
SRC_URI = "git://github.com/oliver----/swig-v8.git;protocol=git;rev=f31c1dce7a45c4b8ed7e6ff845f4c74539e056f1;branch=devel"

SRC_URI[md5sum] = "9b1cd29b12ecdfa741cea7bd8c934c4b"
SRC_URI[sha256sum] = "818f87ce2d7d89c3f6ddd86e4e8cf18b54d965197fc24e7663cf2ca948b93218"

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
   # Fix include path for node in node.i file
   sed -i "s/src\/node.h/node\/node.h/g" Lib/javascript/v8/node.i
   oe_runconf
}

FILES_${PN} += "${datadir}/*"
FILES_${PN}-native += "${datadir}/*"
