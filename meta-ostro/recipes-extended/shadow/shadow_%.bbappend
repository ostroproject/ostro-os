do_install_append () {
    # The base recipe sets GROUP=100="users" as shared group for all
    # users. In Ostro, each user gets its own group (more secure default
    # because it prevents accidental data sharing when setting something
    # group read/writeable).
    sed -i -e 's/^GROUP=/# GROUP=/' ${D}/${sysconfdir}/default/useradd
}
