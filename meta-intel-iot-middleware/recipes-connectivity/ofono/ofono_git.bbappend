# Remove the python3 runtime requirements for ofono, this is only for test
# scripts and these test scripts use dbus and python3 dbus module is broken.
RDEPENDS_${PN} = ""
