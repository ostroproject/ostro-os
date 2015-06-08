# Optionally, compilation of the main package with the daemon gets moved into
# dbus-cynara. That is necessary to break a dependency cycle once the
# daemon gets compiled with Cynara support (dbus -> cynara -> systemd
# -> dbus).
do_install_append_class-target () {
    if ${@bb.utils.contains('DISTRO_FEATURES', 'dbus-cynara', 'true', 'false', d)}; then
        for i in ${@' '.join([d.getVar('D', True) + x for x in (d.getVar('FILES_dbus', True) or '').split()])}; do
            rm -rf $i
        done

        # Try to remove empty directories, starting with the
        # longest path (= deepest directory) first.
        # Find needs a valid current directory. Somehow the directory
        # we get called in is gone by the time that we get invoked.
        ( cd ${D}
          for i in `find . -type d | sort -r`; do
            rmdir $i || true
          done
        )
    fi
}

# The main package will be empty, but we want to have it created
# anyway because of the dependencies on it. Installing it will pull in
# the replacement dbus-cynara package.
ALLOW_EMPTY_${PN}_class-target = "1"
RDEPENDS_${PN}_append_class-target = "${@bb.utils.contains('DISTRO_FEATURES', 'dbus-cynara', ' dbus-cynara', '', d)}"
