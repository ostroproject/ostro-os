# Do not start the systemd-dev-app services by default. To enable them, log in
# to the system and enable soletta-dev-app-server.service and
# soletta-dev-app-avahi-discover.service.

SYSTEMD_AUTO_ENABLE_${PN} = "disable"
