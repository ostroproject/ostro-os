#!/bin/sh
#author: JiuJin Hong (jiujinx.hong@intel.com)
if [ ! -d "/sys/devices/platform/intel_mcu" ];then
	exit
fi

if [ ! -f "/lib/firmware/intel_mcu.bin" ];then
	exit
fi

echo "load mcu app" > /sys/devices/platform/intel_mcu/control

