# This class is meant for creating a user with a TLM session
#
# Inheriting this class will create the home directory of the
# specified user with the correct ownership.
#
# iot-user class has the following variables for parametrization:
#
# IOT_USER_NAME:
# IOT_USER_DIR:
# 
#
#

IOT_USER_SHELL = "/sbin/nologin"

IOT_APP_SERVICE_DIR = "${systemd_unitdir}/system"
IOT_APP_TLM_SESSION_DIR = "/etc/session.d"

export IOT_APP_SERVICE_FILE_PATH = "${IOT_APP_SERVICE_DIR}/${IOT_USER_NAME}-session.service"
export IOT_APP_TLM_SESSION_FILE_PATH = "${IOT_APP_TLM_SESSION_DIR}/tlm-session.ini"


SYSTEMD_UNIT_NAME = "${IOT_USER_NAME}-session.service"

pkg_postinst_${PN}_append () {
#!/bin/sh -e
if [ "x$D" != "x" ] ; then
   # use tlm-seatconf to add a new configuration into the tlm.conf file
   SEAT=$(tlm-seatconf add -c $D/etc/tlm.conf -h 1 -i /var/lock/iotpm.ready "tlm-launcher -f ${IOT_APP_TLM_SESSION_FILE_PATH} -s %s")
   bbdebug 1 "generated seat $SEAT for tlm session"

   if [ -n "$SEAT" ]; then
      # in-place modify the systemd service file
      bbdebug 1 "adding seat $SEAT to ${IOT_APP_SERVICE_FILE_PATH}"
      sed -i s/seat_placeholder/$SEAT/ $D${IOT_APP_SERVICE_FILE_PATH}
   fi

   # enable the systemd session here
   systemctl --root=$D enable ${SYSTEMD_UNIT_NAME}
fi
}


inherit iot-user

DEPENDS =+ "tlm-native iot-app-fw-tlm"
RDEPENDS_${PN} =+ "iot-app-fw-tlm"


# automatically start the service during boot
SYSTEMD_SERVICE_${PN} = "${SYSTEMD_UNIT_NAME}"
SYSTEMD_AUTO_ENABLE = "status"

inherit systemd

do_install_append() {
    mkdir -p ${D}${IOT_APP_SERVICE_DIR}
    mkdir -p ${D}${IOT_APP_TLM_SESSION_DIR}

    cat > /tmp/${IOT_USER_NAME}-session.service << EOF
[Unit]
Description=TLM session for user ${IOT_USER_NAME}
Requires=tlm.service iot-launch.socket
After=multi-user.target

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/tlm-client -k -l --seat seat_placeholder --username ${IOT_USER_NAME} --password automatic_login
EOF

    install /tmp/${IOT_USER_NAME}-session.service ${D}${IOT_APP_SERVICE_FILE_PATH}
}

FILES_${PN} += "${IOT_APP_SERVICE_FILE_PATH}"

pkg_postinst_${PN}_append () {
#!/bin/sh -e
exit 0
}