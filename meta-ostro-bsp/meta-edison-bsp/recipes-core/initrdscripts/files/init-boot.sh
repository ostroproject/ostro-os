#!/bin/sh

PATH=/sbin:/bin:/usr/sbin:/usr/bin

# create required directories
mkdir -p /proc
mkdir -p /sys
mkdir -p /run
mkdir -p /update
mkdir -p /var/lock
mkdir -p /var/log
mkdir -p /var/run

# set up /proc /sys and /dev
mount -t proc proc /proc
mount -t sysfs sysfs /sys
mount -t devtmpfs none /dev

# set up logging
syslogd

# launch udev
udevd --daemon
udevadm trigger --action=add

# start watchdog daemon to avoid reboot while recovering
watchdog

# mount update partition and do recovery
if losetup -o 1048576 /dev/loop0 /dev/mmcblk0p9; then
	mount -t vfat /dev/loop0 /update
	if [ -d /update/recovery ] && \
	   [ -e /update/recovery/u-boot.bin ] && \
	   [ -e /update/recovery/u-boot.env ] && \
	   [ -e /update/recovery/boot.hddimg ] && \
	   [ -e /update/recovery/rootfs.tar.bz2 ] && \
	   [ -e /update/recovery/image-name.txt ]; then
		echo -n " Recovering installation of "
		cat /update/recovery/image-name.txt
		echo "Writing u-boot binary ..."
		dd if=/update/recovery/u-boot.bin of=/dev/mmcblk0p1
		echo "Writing u-boot environment ..."
		dd if=/update/recovery/u-boot.env of=/dev/mmcblk0p2
		echo "Writing u-boot backup environment ..."
		dd if=/update/recovery/u-boot.env of=/dev/mmcblk0p4
		echo "Writing boot partition ..."
		dd if=/update/recovery/boot.hddimg of=/dev/mmcblk0p7
		echo "Preparing rootfs ..."
		mkfs.ext4 -i 4096 /dev/mmcblk0p8
		echo "Writing rootfs ..."
		mkdir /rootfs
		mount -t ext4 /dev/mmcblk0p8 /rootfs
		tar xf /update/recovery/rootfs.tar.bz2 -C /rootfs
		sync
		losetup -d /dev/loop0
		reboot -f
	fi
fi
echo "Missing recovery files, launching debug shell"
exec sh
