#!/bin/sh
### BEGIN INIT INFO
# Provides:
# Required-Start:
# Required-Stop:
# Default-Start:     S
# Default-Stop:
# Short-Description: Configure ALSA audio output to the connected HDMI port
### END INIT INFO

#
# If both HDMI ports are connected then use HDMI0 for default ALSA audio out..

ALSA_CONF_FILE="/etc/asound.conf"

HDMI0_STATUS_FILE="/sys/class/drm/card0-HDMI-A-1/status"
HDMI1_STATUS_FILE="/sys/class/drm/card0-HDMI-A-2/status"

HDMI0_ALSA_CONF="hw:0,3"
HDMI1_ALSA_CONF="hw:0,7"

if [ -f "${HDMI0_STATUS_FILE}" ] && [ "`cat ${HDMI0_STATUS_FILE}`" == "connected" ]
then
	sed -i "s/pcm *\"hw:[0-9]*,[0-9]*\"/pcm \"${HDMI0_ALSA_CONF}\"/" ${ALSA_CONF_FILE}
elif [ -f "${HDMI1_STATUS_FILE}" ] && [ "`cat ${HDMI1_STATUS_FILE}`" == "connected" ]
then
	sed -i "s/pcm \"hw:[0-9]*,[0-9]*\"/pcm \"${HDMI1_ALSA_CONF}\"/" ${ALSA_CONF_FILE}
fi
