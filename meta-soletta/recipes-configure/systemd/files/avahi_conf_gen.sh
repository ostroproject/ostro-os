#! /bin/sh
CONF_FILE="/etc/avahi/avahi-daemon.conf"
INTERFACE="enp2s0"
MAC_ADDRESS=`ifconfig $INTERFACE | grep "HWaddr" | awk '{print $NF}'`
if [ -z "$MAC_ADDRESS" ] ; then
	echo "ERROR avahi_conf_gen: Failed to get MAC Address"
else
	echo "# This file was auto generated" > "$CONF_FILE"
	echo "[server]" >> "$CONF_FILE"
	echo "host-name=$MAC_ADDRESS" >> "$CONF_FILE"
	echo "use-ipv4=yes" >> "$CONF_FILE"
	echo "use-ipv6=yes" >> "$CONF_FILE"
	echo "" >> "$CONF_FILE"
	echo "[wide-area]" >> "$CONF_FILE"
	echo "enable-wide-area=yes" >> "$CONF_FILE"
	echo "" >> "$CONF_FILE"
	echo "[publish]" >> "$CONF_FILE"
	echo "publish-addresses=yes" >> "$CONF_FILE"
	echo "publish-workstation=yes" >> "$CONF_FILE"
	echo "publish-domain=yes" >> "$CONF_FILE"
	echo "publish-hinfo=yes" >> "$CONF_FILE"
	echo "" >> "$CONF_FILE"
	echo "[rlimits]" >> "$CONF_FILE"
	echo "rlimit-core=0" >> "$CONF_FILE"
	echo "rlimit-data=4194304" >> "$CONF_FILE"
	echo "rlimit-fsize=0" >> "$CONF_FILE"
	echo "rlimit-nofile=768" >> "$CONF_FILE"
	echo "rlimit-stack=4194304" >> "$CONF_FILE"
	echo "rlimit-nproc=3" >> "$CONF_FILE"
fi

systemctl enable avahi-daemon.socket
systemctl start avahi-daemon.socket
