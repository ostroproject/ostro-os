# This class is meant for pre-creating users for IoT applications.
#
# Inheriting this class will create the home directory of the
# specified user with the correct ownership.
#
# iot-user class has the following variables for parametrization:
#
# IOT_USER_NAME: user to create
#
#     A new user with this name will be created.
#

#
# We have a license here to allow the one inheriting us be as minimal
# as possible, even omitting licensing information.
LICENSE = "MIT"
LIC_FILES_CHKSUM = " \
   file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690 \
   file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420 \
"

# Set the defaults
IOT_USER_DIR ??= "/home"
IOT_USER_SHELL ??= "/sbin/nologin"

# Force the creation of the package responsible for creating the user.
#PACKAGES =+ "${PN}"

# Tell useradd where the post-install script should go.
USERADD_PACKAGES = "${PN}"

# Create the user with disallowed login and no extra groups.
USERADD_PARAM_${PN} = "-s ${IOT_USER_SHELL} ${IOT_USER_NAME}"
GROUPADD_PARAM_${PN} = ""
GROUPMEMS_PARAM_${PN} = ""

inherit useradd

export IOT_USER_HOME = "${IOT_USER_DIR}/${IOT_USER_NAME}"

# Create the directory here, and change its ownership for the user.
# This will also have the nice side-effect that bitbake will actually
# create ${PN}, so there will be a package for useradd to put its
# postinstall script into. Otherwise, if the package inheriting
# us is empty, bitbake does not create the main package (there are no
# files in it)... it just creates two empty subpackages instead:
# ${PN}-dev and ${PN}-dbg.
FILES_${PN} =+ "${IOT_USER_HOME}"
#FILES_${PN} =+ "${@check_home(d, "${IOT_USER_NAME}")}"

def check_home(d, user):
    import os

    D = d.getVar('D', expand=True)
    if D == None:
       return ''

    home = D + d.getVar('IOT_USER_DIR', expand=True) + '/' + user
    flag = 'IOT_USER_CREATED_' + user
    done = d.getVar(flag)

    if done == 'TRUE':
       return ''

    d.setVar(flag, 'TRUE')
    return home

do_install_append () {
    mkdir -p ${D}${IOT_USER_DIR}/${IOT_USER_NAME}
    chown ${IOT_USER_NAME} ${D}/${IOT_USER_DIR}/${IOT_USER_NAME}
    chgrp ${IOT_USER_NAME} ${D}/${IOT_USER_DIR}/${IOT_USER_NAME}
}
