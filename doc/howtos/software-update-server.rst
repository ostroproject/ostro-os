How to use software updates
###########################

These instructions help to generate a repository needed to make software updates
work with Ostro.

Prerequisites
=============

 - a linux host with docker and util-linux installed (e.g. Fedora 23);
 - signing keys (alternatively testing keys from the `swupd-server` project can
   be used).

Creating a Docker image
=======================

We have already created a Docker image for your convenience, so all you need is
to type in::

  $ docker pull ostroproject/ostro-swupd-server

But you can create your own image with the following instructions:

1. Clone the git repo `git@github.com:ostroproject/ostro-docker.git` to your host::

     $ git clone git@github.com:ostroproject/ostro-docker.git

2. Build a new docker image using the Dockerfile from the repo::

     $ docker build -t ostro-swupd-server ostro-docker/swupd

If your host can't access Internet directly then you need to provide an
additional `--build-arg` argument for your HTTP proxy::

  $ docker build --build-arg http_proxy=http://<you_proxy_host>:<proxy_port> -t ostro-swupd-server ostro-docker/swupd

Creating software update repo
=============================

The main selling point of ClearLinux's software updates is the per-file
granularity and the ability to use binary deltas for updates. But this
comes at a price: previous builds need to be preserved in order to
calculate the diffs. You must have a big enough storage mounted to your
host to keep the history. Let's assume the path to the storage is in
`STORAGE_DIR` and the initial version of your distribution is `NEW_VERSION`.
Then do the following steps:

1. Using the script `doc/howtos/extras/extract_rootfs.sh` of this repository
   extract the content of the latest rootfs to `$STORAGE_DIR/image/10/os-core`::

     $ sudo sh doc/howtos/extras/extract_rootfs.sh \
         ${OSTRO_SDK_DIR}/tmp-glibc/deploy/images/${MACHINE}/ostro-image-${MACHINE}.dsk \
         $STORAGE_DIR $NEW_VERSION $PARTITION_NUM

   Where `PARTITION_NUM` is the number of rootfs partition in the .dsk image,
   e.g. 5. You can find it in the file
   `meta-ostro/recipes-image/images/files/iot-cfg/disk-layout-<MACHINE>.json`.

2. Generate the first repo::

     $ docker run --rm=true --privileged \
                  -v ${STORAGE_DIR}/image:/var/lib/update/image \
                  -v ${STORAGE_DIR}/www:/var/lib/update/www \
                  ostro-swupd-server /home/clrbuilder/projects/process_rootfs.sh ${NEW_VERSION}

3. Check if everything went smoothly and if it did then update the latest version::

     $ echo ${NEW_VERSION} > ${STORAGE_DIR}/image/latest.version
     $ mkdir -p ${STORAGE_DIR}/www/version/format3
     $ echo ${NEW_VERSION} > ${STORAGE_DIR}/www/version/format3/latest

.. warning:: The steps above have been written with the assumption that your
             host system supports xattrs on the file system and doesn't
             interfere with them. For example you might need to disable SELinux.
             Also please keep in mind that future versions of Yocto will
             have these steps integrated.

Now you can expose the new repo with an HTTP server::

     $ cd ${STORAGE_DIR}/www
     $ python -m SimpleHTTPServer 8000

And test with the `swupd` client on a device::

    # swupd verify -V --log=info --url=http://<you_host>:8000

.. note:: swupd client on the device must be aware of its OS' current version:
          the file `/usr/lib/os-release` should contain something like::

              VERSION_ID=10

As such the initial repository is of limited use since devices are initially
flashed with the first version of OS. Hence let's assume there is a new build
that devices need to be upgraded to. In this case just increment `NEW_VERSION`
by 10 and repeat the steps above on the same host.
