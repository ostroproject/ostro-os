# Include security flags pulled in via openembedded-core.
require conf/distro/include/security_flags.inc

# Add Ostro OS specific flags to fix build issues with
# recipes that are being used in Ostro OS.
SECURITY_CFLAGS_pn-mraa = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-upm = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-iot-app-fw = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-iotivity = "${SECURITY_NO_PIE_CFLAGS}"
SECURITY_CFLAGS_pn-krb5 = "${SECURITY_NO_PIE_CFLAGS}"




# Workaround for issue, where a) openjdk uses system gcc, and b)
# system gcc is 4.8 or older and -fstack-protector-strong is not supported

SECURITY_LDFLAGS_remove_pn-openjdk-8-jre = "-fstack-protector-strong"
SECURITY_LDFLAGS_append_pn-openjdk-8-jre = " -fstack-protector-all"


SECURITY_CFLAGS_remove_pn-openjdk-8-jre = "-fstack-protector-strong"
SECURITY_CFLAGS_append_pn-openjdk-8-jre = " -fstack-protector-all"
