# Fix QA issues caused by incomplete systemd dependency/usage
# 
# Looks like in some cases systemd can be found in the buildroot when
# cups' configure is run. Because of this, cups sets HAVE_SYSTEMD and
# installs it's org.cups.* systemd files.
#
# cups.inc does not handle org.cups.* but installs oe-core specific
# service files. Additionally, there's a missing (R)DEPENDS to systemd.
#
# To temporarily fix these issues, unconditionally depend on systemd
# (fixes 'build-deps') and remove cups' service files (fixes 
# 'installed-vs-shipped').
#
# There's a proper patch to fix these contributed by the community in
# review (along with a cups version upgrade). Therefore, setting upstream
# status to inapproriate.
#
# Upstream-Status: Inappropriate [Alternative oe-core fix in review] 

DEPENDS_append = " systemd"

do_install_append() {
    rm -f ${D}${systemd_unitdir}/system/org.cups.*
}
