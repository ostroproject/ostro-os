# This class is for setting variables for application packages.
#
# iot-app class input variables:
# ------------------------------
#
# IOT_APP_PROVIDER: the application provider which is at the same time the
#     Linux user
#
#     We are going to depend on the package that creates the user,
#     eg. if IOTAPP_PRIVIDER were 'yoyodine' we will depend on 'yoyodine-user'
#     package
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
#     where the files of the applications should go. You could pass this
#     eg. as --prefix option to autoconf
#
# IOT_APP_MANIFEST_PATH
#

DEPENDS += "${IOT_APP_PROVIDER}-user"

IOT_USER_DIR ??= "/home"
IOT_USER_HOME ??= "${IOT_USER_DIR}/${IOT_APP_PROVIDER}"
IOT_APP_ROOT = "apps_rw"

export IOT_APP_INSTALLATION_PATH = "${IOT_USER_HOME}/${IOT_APP_ROOT}/${PN}"
export IOT_APP_MANIFEST_PATH = "/usr/share/iot/users/${IOT_APP_PROVIDER}"
export IOT_USER_HOME
export IOT_APP_TLM_PATH = "${IOT_APP_INSTALLATION_PATH}"


RDEPENDS_${PN} += "${IOT_APP_PROVIDER}-user"


do_install_append () {
    if [ -d "${D}${IOT_USER_HOME}" ] ; then
        chown -R ${IOT_APP_PROVIDER}.${IOT_APP_PROVIDER} ${D}${IOT_USER_HOME}
    fi
    if [ -d "${D}${IOT_APP_MANIFEST_PATH}" ] ; then
        chown ${IOT_APP_PROVIDER}.${IOT_APP_PROVIDER} ${D}${IOT_APP_MANIFEST_PATH}
    fi
}
