#! /bin/sh
INTERFACE="enp2s0"
MAC_ADDRESS=`ifconfig $INTERFACE | grep "HWaddr" | awk '{print $NF}'`
/usr/bin/hostnamectl set-hostname $MAC_ADDRESS
