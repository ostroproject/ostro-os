# Include security flags pulled in via openembedded-core.
require conf/distro/include/security_flags.inc

SECURITY_PIC_CFLAGS ?= "-fpic"

# Add Ostro OS specific flags to fix build issues with
# recipes that are being used in Ostro OS.
SECURITY_CFLAGS_pn-zeromq = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"
SECURITY_CFLAGS_pn-mraa = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"
SECURITY_CFLAGS_pn-upm = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"
SECURITY_CFLAGS_pn-iot-app-fw = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"
SECURITY_CFLAGS_pn-iotivity = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"
SECURITY_CFLAGS_pn-krb5 = "${SECURITY_NO_PIE_CFLAGS} ${SECURITY_PIC_CFLAGS}"

# c-ares has a custom m4 macro that too agressively (and
# unconditionally) checks CFLAGS and fails with all -D*.
# Drop the flag(s) that c-ares is not happy with.
SECURITY_CFLAGS_remove_pn-c-ares = "-D_FORTIFY_SOURCE=2"
