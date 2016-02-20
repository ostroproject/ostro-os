#! /bin/bash
INTERFACE="enp2s0"
MAC_ADDRESS=`ifconfig $INTERFACE | grep "HWaddr" | awk '{print $NF}'`
sed -i "s@MACADDR@$MAC_ADDRESS@" /etc/avahi/services/soletta-dev-app.service
