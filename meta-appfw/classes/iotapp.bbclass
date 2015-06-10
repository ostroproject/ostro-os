# This class is for setting variables for application packages.
#
# iotapp class supports the following variables:
#
# IOTAPP_PROVIDER: string to match the app to the service provider user
#
#     A new user will be created for the provider if the user is not
#     already present in the system.
#
# IOTAPP_DIR: directory where applications are installed
#
#     All applications are installed under the same directory structure
#     in their own directories and are therefore expected to be
#     relocatable.  The default value is "/home".
#
# IOTAPP_SERVICE_FILE_PATH
#
#     If a session package wants its service file to contain the
#     automatically generated seat ID, it needs to give the path to the
#     service file to be changed on the root filesystem. The service
#     file has to contain string "seat_placeholder" which is then
#     substituted with the seat id.
#
# IOTAPP_TLM_SESSION_FILE_PATH
#
#     If a session package wants to set the TLM session file to
#     automatically launch applications during the user login, it has to
#     specify a session file that is executed by TLM. This variable
#     should have the full root filesystem path of that file.

# depending on tlm so that tlm-seatconf would work
DEPENDS += "tlm-native tlm-config"

IOTAPP_DIR ??= "/home"

export IOTAPP_INSTALLATION_PATH = "${IOTAPP_DIR}/${IOTAPP_PROVIDER}/${PN}"

# FIXME: if the files go to a package of a different name, this won't probably
# work right.
USERADD_PACKAGES = "${PN}"

# do not allow login for the user
USERADD_PARAM_${PN} = "-s /sbin/nologin ${IOTAPP_PROVIDER}"
GROUPADD_PARAM_${PN} = ""
GROUPMEMS_PARAM_${PN} = ""

# It turns out that if useradd is inherited for multiple times with
# orders to create the same user, it doesn't create an error. Apparently
# the second time the user is just not created. This means that there is
# no need to call 'id -u ${IOTAPP_PROVIDER}' or similar and check for
# the user before inhering the useradd class.
#
# One question that is unsolved is that is there a concept of user/group
# removal when the package is removed? It might mean that if the package
# that actually initialzed the user is removed, the other packages
# requiring the same user would fail to work.
inherit useradd

do_install_prepend() {
    # TODO: if this is a Node.js recipe, check that npm shrinkwrap file is
    # present and warn if it isn't. Also do not create the path if we
    # are installing a session package.

    # create the installation directory
    mkdir -p ${D}/${IOTAPP_INSTALLATION_PATH}
}

do_install_append() {
    if [ -d ${D}${IOTAPP_INSTALLATION_PATH} ]; then
        chown -R ${IOTAPP_PROVIDER} ${D}${IOTAPP_INSTALLATION_PATH}
        chmod -R og-rwx ${D}${IOTAPP_INSTALLATION_PATH}
    fi

    # TODO: seed package database, if present.
}

update_config() {
    # the following commands make sense only in the context of session
    # packages, so guard them with checking the environment variables

    if [ -n ${IOTAPP_TLM_SESSION_FILE_PATH} ]; then
        # use tlm-seatconf to add a new configuration into the tlm.conf file
        SEAT=$(${STAGING_DIR_HOST}/usr/bin/tlm-seatconf add -c ${IMAGE_ROOTFS}/etc/tlm.conf "tlm-laucher -f ${IOTAPP_TLM_SESSION_FILE_PATH} -s %s")

        if [ -n ${IOTAPP_SERVICE_FILE_PATH} ] && [ -n ${SEAT} ]; then
            sed s/seat_placeholder/${SEAT}/ ${IMAGE_ROOTFS}${IOTAPP_SERVICE_FILE_PATH}
        fi
    fi
}

ROOTFS_POSTPROCESS_COMMAND += "update_config; "
