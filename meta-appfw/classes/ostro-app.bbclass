# This class is for setting variables for application packages.
#
# ostro-app class input variables:
# ------------------------------
#
# OSTRO_USER_NAME:
#       user to create for your app
#
# OSTRO_APP_NAME:
#       name of the application
#
# ostro-app class exported variables:
# ------------------------------
#
# OSTRO_APP_ROOT:
#       path where to install your app
#

inherit useradd

# Tell useradd where the post-install script should go.
USERADD_PACKAGES = "${PN}"

# Set the defaults
OSTRO_USER_SHELL ??= "/sbin/nologin"
OSTRO_USER_APP_NAME ??= "${OSTRO_USER_NAME}-${OSTRO_APP_NAME}"

# Create the user with disallowed login and no extra groups.
USERADD_PARAM_${PN} = "-s ${OSTRO_USER_SHELL} ${OSTRO_USER_APP_NAME}"
GROUPADD_PARAM_${PN} = ""
GROUPMEMS_PARAM_${PN} = ""

OSTRO_APP_DIR ??= "/apps"
OSTRO_APP_ROOT ??= "${OSTRO_APP_DIR}/${OSTRO_USER_NAME}/${OSTRO_APP_NAME}"

export OSTRO_APP_ROOT
RDEPENDS_${PN} += "iot-app-fw"

do_install_append () {
    chmod -R 755 ${D}${OSTRO_APP_ROOT}/
}
