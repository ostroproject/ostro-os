# Install default Smack rules, copied from a running Tizen IVI 3.0.
# Corresponds to manifest file from default-access-domains in Tizen:
# https://review.tizen.org/git?p=platform/core/security/default-ac-domains.git;a=blob;f=packaging/default-ac-domains.manifest
do_install_append_smack () {
    mkdir -p ${D}/${sysconfdir}/smack/accesses.d/
    cat >${D}/${sysconfdir}/smack/accesses.d/default-access-domains <<EOF
System _ -----l
System System::Log rwxa--
System System::Run rwxat-
System System::Shared rwxat-
System ^ rwxa--
System User rwx---
_ System::Run rwxat-
_ System -wx---
^ System::Log rwxa--
^ System::Run rwxat-
^ System rwxa--
User _ -----l
User User::App:Shared rwxat-
User User::Home rwxat-
User System::Log rwxa--
User System::Run rwxat-
User System::Shared r-x---
User System -wx---
EOF
}

# Do not rely on an rpm with manifest support. Apparently that approach
# will no longer be used in Tizen 3.0. Instead set special Smack attributes
# via postinst. This is much easier to use with bitbake, too:
# - no need to maintain a patched rpm
# - works for directories which are not packaged by default when empty
RDEPENDS_${PN}_append_smack = " smack-userspace"
DEPENDS_append_smack = " smack-userspace-native"
pkg_postinst_${PN}_smack() {
    #!/bin/sh -e

    # https://review.tizen.org/gerrit/gitweb?p=platform/upstream/filesystem.git;a=blob;f=packaging/filesystem.manifest:
    # <filesystem path="/etc" label="System::Shared" type="transmutable" />
    install -d $D${sysconfdir}
    # This has no effect on files installed into /etc during image construction
    # because pseudo does not know the special semantic of SMACK::TRANSMUTE.
    # To avoid having different xattrs on files inside /etc when pre-installed
    # in an image vs. installed on a device, the xattr-images.bbclass has
    # a workaround for this deficiency in pseudo.
    chsmack -t $D${sysconfdir}
    chsmack -a 'System::Shared' $D${sysconfdir}

    # Same for /var. Any daemon running as "System" will get write access
    # to everything.
    install -d $D${localstatedir}
    chsmack -t $D${localstatedir}
    chsmack -a 'System::Shared' $D${localstatedir}

    # <filesystem path="/tmp" label="*" />
    mkdir -p $D/tmp
    chsmack -a '*' $D/tmp

    # <filesystem path="/var/log" label="System::Log" type="transmutable" />
    # <filesystem path="/var/tmp" label="*" />
    # These are in a file system mounted by systemd. We patch the systemd service
    # to set these attributes.

    # From https://review.tizen.org/git/?p=platform/core/appfw/tizen-platform-config.git;a=blob;f=packaging/tizen-platform-config.spec
    find $D${sysconfdir}/skel | xargs chsmack -a User
    chsmack -a User::Home $D${sysconfdir}/skel
}
