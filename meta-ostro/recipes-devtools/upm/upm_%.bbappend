# if DISTRO_FEATURES do not have Java enabled, remove java from the bindings list
BINDINGS_remove = "${@bb.utils.contains('DISTRO_FEATURES', 'java', '', 'java', d)}"
