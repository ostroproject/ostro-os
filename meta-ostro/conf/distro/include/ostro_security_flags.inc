# Include security flags pulled in via openembedded-core.
require conf/distro/include/security_flags.inc

# Add Ostro OS specific flags to fix build issues with
# recipes that are being used in Ostro OS.
SECURITY_CFLAGS_pn-mraa = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-upm = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-iot-app-fw = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-iotivity = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-krb5 = "${SECURITY_NO_PIE_CFLAGS}"
