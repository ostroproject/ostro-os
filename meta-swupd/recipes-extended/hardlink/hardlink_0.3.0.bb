SUMMARY = "hardlink is a tool which replaces multiple copies of a file with hardlinks."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://hardlink.c;endline=22;md5=168464a4fc92fa7389c53b0755b39fbb"

DEPENDS = "libpcre attr"

SRC_URI = "http://jak-linux.org/projects/hardlink/${BPN}_${PV}.tar.xz"
SRC_URI[md5sum] = "72f1a460adb6874c151deab766e434ad"
SRC_URI[sha256sum] = "e8c93dfcb24aeb44a75281ed73757cb862cc63b225d565db1c270af9dbb7300f"

EXTRA_OEMAKE = "'DESTDIR=${D}' 'PREFIX=${prefix}' BINDIR='${bindir}'"

do_compile () {
	oe_runmake
}

do_install () {
	oe_runmake install
}

BBCLASSEXTEND = "native nativesdk"
