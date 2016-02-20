#!/bin/sh
#
sed -e "/^#.*/d" -e "/^\s*$/d" defconfig >defconfig.new
mv defconfig.new defconfig
