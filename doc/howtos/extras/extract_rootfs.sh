#!/bin/sh

TMP_MOUNT_POINT=/tmp/img_mount_point

IMG_FILE=$1
STORAGE_DIR=$2
VER=$3
PARTITION_LAYOUT=$4

function usage {
    echo "Usage: $0 <path_to_image_file> <storage_directory> <version> <path_to_partition_layout>"
}

if [ -z "${IMG_FILE}" ]; then
    echo "ERROR: No image file specified."
    usage
    exit 1
fi

if [ -z "${STORAGE_DIR}" ]; then
    echo "ERROR: No storage directory specified"
    usage
    exit 1
fi

if [ -z "${VER}" ]; then
    echo "ERROR: No version specified"
    usage
    exit 1
fi

if [ -z "${PARTITION_LAYOUT}" ]; then
    echo "ERROR: No partition layout file specified. You can find it next to *.dsk image"
    echo "       file inside you build directory, e.g."
    echo "       build/tmp-glibc/deploy/images/<MACHINE>/ostro-image-<MACHINE>-disk-layout.json"
    usage
    exit 1
fi

PARTITION_NUM=`cat $PARTITION_LAYOUT | python -c "import json, sys; print int([key for key in json.load(sys.stdin).keys() if key.endswith('_rootfs')][0].split('_')[1])"`

if [ -z "${PARTITION_NUM}" ]; then
    echo "ERROR: Can't fetch rootfs's partition number from the given layout file"
    exit 1
fi

OS_CORE_DIR=${STORAGE_DIR}/image/${VER}/os-core
IMG_FILE=`realpath $IMG_FILE`

losetup -f $IMG_FILE
LOOPDEV=`losetup -a | grep $IMG_FILE | awk -F ":" '{print $1}' -`

if [ -z "${LOOPDEV}" ]; then
    echo "ERROR: Can't associate $IMG_FILE with a loop device"
    exit 1
fi

mkdir -p $TMP_MOUNT_POINT
partprobe $LOOPDEV
mount ${LOOPDEV}p${PARTITION_NUM} $TMP_MOUNT_POINT
mkdir -p $OS_CORE_DIR
rsync -aX $TMP_MOUNT_POINT/ $OS_CORE_DIR
umount $TMP_MOUNT_POINT
losetup -d $LOOPDEV
rm -r ${OS_CORE_DIR}/lost+found
