# This class is for setting variables for application packages.
#
# iot-app class input variables:
# ------------------------------
#
# IOT_APP_PROVIDER: the application provider which is at the same time the Linux user
#
#     We are going to depend on the package that creates the user,
#     eg. if IOTAPP_PRIVIDER were 'yoyodine' we will depend on 'yoyodine-user' package
#
# IOT_USER_DIR: directory where applications are installed
#
#     All applications are installed under the same directory structure
#     in their own directories and are therefore expected to be
#     relocatable.  The default value is "/home".
#
#
# iot-app class exported variables:
# ---------------------------------
#
# IOT_APP_INSTALLATION_PATH
#     where the files of the applications should go. You could pass this eg. as --prefix
#     option to autoconf
#
# IOT_APP_MANIFEST_PATH
#

# depending on tlm so that tlm-seatconf would work
DEPENDS += "${IOT_APP_PROVIDER}-user"
IOT_USER_DIR ??= "/home"
IOT_USER_HOME ??= "${IOT_USER_DIR}/${IOT_APP_PROVIDER}"
IOT_APP_ROOT = "apps_rw"

export IOT_APP_INSTALLATION_PATH = "${IOT_USER_HOME}/${IOT_APP_ROOT}/${PN}"
export IOT_APP_MANIFEST_PATH = "/usr/share/iot/users/${IOT_APP_PROVIDER}"
export IOT_USER_HOME

# FIXME: if the files go to a package of a different name, this won't probably
# work right.
USERADD_PACKAGES = "${PN}"

def get_tlm_rdepends(d):
    return ""

    if d.getVar('IOT_APP_SERVICE_FILE_PATH') != None:
        if d.getVar('IOTAPP_TLM_SESSION_FILE_PATH') != None:
            # this is a TLM-based session
            return "iot-app-fw-launcher tlm"
    else:
        return ""

RDEPENDS_${PN} += "${IOT_APP_PROVIDER}-user ${@get_tlm_rdepends(d)}"
