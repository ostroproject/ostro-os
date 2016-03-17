#!/bin/sh

if [ -z "$HWADDR" ]; then
    HWADDR=`ip link show wpan0 | grep -e link/ieee802.15.4 | sed -e 's#^.*link/ieee802.15.4 \([0-9a-fA-F:]\+\) .*$#\1#g'`
    if [ -z "$HWADDR" ]; then
        HWADDR=`sed /etc/machine-id -e 's#\([0-9a-fA-F]\{2\}\)#\1:#g' | cut -d: -f1-8`
    fi
fi

if [ -z "$PAN" ]; then
    PAN=777
fi

if [ -z "$ADDR" ]; then
    ADDR=`echo $HWADDR  | cut -d: -f7-8 | tr -d :`
fi

if [ -z "$CHANNEL" ]; then
    CHANNEL=`iz listphy | grep -e "channels on page 0:" | sed -e 's#^.*channels on page 0: \([0-9a-fA-F:]\+\) .*$#\1#g'`
fi

if [ -z "$CHANNEL" ]; then
    CHANNEL=11
fi

ip link set wpan0 address ${HWADDR}
iz set wpan0 ${PAN} ${ADDR} ${CHANNEL}
ifconfig wpan0 up
ip link add link wpan0 name lowpan0 type lowpan
ifconfig lowpan0 up

