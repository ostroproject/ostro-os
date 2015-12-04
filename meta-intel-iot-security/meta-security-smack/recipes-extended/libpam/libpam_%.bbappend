FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Enable Smack support.
DEPENDS_append_smack = " smack"
SRC_URI_append_smack = " \
    file://pam-smack-so.patch \
    file://pam-smack-so-configure-${@ 'ac' if bb.utils.vercmp_string('${PV}', '1.2.1') >= 0 else 'in'}.patch \
"

# Tizen has to patch several pam files in different packages (ssh, shadow).
# In OE, we have common-session which gets included by those, so we
# only need to add pam_smack.so once.
do_install_append_smack () {
    for i in common-session-noninteractive common-session; do
        f=${D}/${sysconfdir}/pam.d/$i
        [ -f $f ] && echo >>$f "session required pam_smack.so"
    done
}

# Needed for the modified common-session.
RDEPENDS_${PN}-runtime_append_smack = " pam-plugin-smack"
