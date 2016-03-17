#!/bin/sh
ifconfig lowpan0 down
ifconfig wpan0 down
ip link del lowpan0
