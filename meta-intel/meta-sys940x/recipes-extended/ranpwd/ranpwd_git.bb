DESCRIPTION = "Random password generator"
LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://ranpwd.c;beginline=1;endline=11;md5=0e8585e19117526efedfaeb50c345d7a"
SECTION = "console/utils"
PV = "1.2+git${SRCPV}"
PR = "r0"

inherit autotools

SRC_URI = "git://git.zytor.com/utils/ranpwd.git"
SRCREV = "b62aab579e288715b82d5575befaa2b8ff210c2b"

S="${WORKDIR}/git"

do_configure_prepend () {
	if [ ! -e acinclude.m4 -a -e aclocal.m4 ]; then
		cp aclocal.m4 acinclude.m4
	fi
}

do_install() {
	install -d ${D}/${bindir}
	install -m 0755 ${S}/ranpwd ${D}/${bindir}/ranpwd
}
