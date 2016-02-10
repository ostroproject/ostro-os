.. _software-update-server:

Software Update: Building an Ostro |trade| OS  Repository
#########################################################

This technical note provides instructions to help you build a repository 
used to make software updates work with the Ostro OS.

Prerequisites
=============

 - a Linux host with Docker (>= 1.9.1) and util-linux installed (Fedora 23 and
   OpenSUSE 13.2 are known to work well for this purpose, but the outdated
   Docker packages in Ubuntu 14.04 might have connectivity issues);
 - signing keys (alternatively testing keys from the :file:`swupd-server` project can
   be used).

Creating a Docker Image
=======================

We've already created a :file:`swupd-server` Docker image for your convenience, so all you need is
to type in::

  $ docker pull ostroproject/ostro-swupd-server

If you prefer, you can also create your own :file:`swupd-server` Docker image with these steps:

1. Clone the git repo :file:`git@github.com:ostroproject/ostro-docker.git` to your host::

     $ git clone git@github.com:ostroproject/ostro-docker.git

2. Build a new Docker image using the Dockerfile from the repo::

     $ docker build -t ostro-swupd-server ostro-docker/swupd

If your host requires a proxy to access the internet, you need to provide an
additional `--build-arg` argument for your HTTP proxy::

  $ docker build --build-arg http_proxy=http://<you_proxy_host>:<proxy_port> -t ostro-swupd-server ostro-docker/swupd

Creating a Software Update Repo
===============================

The main selling point of Clear Linux's software updates (which we're using for
Ostro OS software updates), is the per-file update
granularity and the ability to use binary deltas for updates. But this
comes at a price: previous builds need to be preserved in order to
calculate the diffs. You must have a large enough storage device mounted to your
host to keep the history. 

Let's assume the path to the storage is in
`STORAGE_DIR` and the initial version of your distribution is `NEW_VERSION`.

Here is a script that will extract the contents of the latest rootfs:

.. literalinclude:: extras/extract_rootfs.sh
   :language: sh 


(There's a copy of this script saved as :file:`extract_rootfs.sh`.) 

Do the following steps to setup your swupd server repository:

1. Extract the content of the latest rootfs to `$STORAGE_DIR/image/10/os-core`::

     $ sudo sh extract_rootfs.sh \
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

Now you can expose the new repo with an HTTP server (python's
SimpleHTTPServer is enough for verification, but never use it in production
because it silently drops new requests when busy with serving a current one)::

     $ cd ${STORAGE_DIR}/www
     $ python -m SimpleHTTPServer 8000

And test with the :file:`swupd` client on a device::

    # swupd verify -V --log=info --url=http://<your_host>:8000

.. note:: swupd client on the device must be aware of its OS' current version:
          the file `/etc/os-release` should contain something like::

              VERSION_ID=10

As such, the initial repository is of limited use since devices are initially
flashed with the first version of OS. Let's assume there is a new build
that devices need to be upgraded to. In this case just increment `NEW_VERSION`
by 10 and repeat the steps above on the same host.
