.. _disk-layout:

Disk Layout in an Ostro |trade| OS .dsk image
#############################################

Introduction
============
Ostro OS images use a .dsk extension to differentiate them
from the .img files normally produced through Yocto Project
tools, because of the different approach chosen.

Scripts that work with .img files will most likely require
some (minor) tweaks, to support .dsk files.

Description
===========
The disk image has a GPT partition, with (unused) MBR guard.
The minimum number of partitions is 3:

- Active EFI partition (with proper type 0xEF00)
- Inactive EFI partition, used during swupd for implementing
  atomic update of the EFI application (with type 0x2700)
- Main root filesystem, by default ext4 (type 0x8300)

The first two EFI partitions are necessary to ensure the
device will still retain its capability to boot, even in the
presence of otherwise catastrophical events, such as power loss
during sw update or errors during the deployment of a new EFI
combo application.

Implementation and Customization
================================
The disk layout is described through a JSON string, which
defines:

- number of partitions
- for each partition:

  - partition type
  - filesystem
  - source (for populating the filesystem)
  - size

The JSON string is contained in the bitbake variable DSK_IMAGE_LAYOUT.
The variable is defined in meta-ostro/classes/image-dsk.bbclass and can
be re-defined either in local.conf or in a bbappend file for the main
ostro-image.bb recipe.

The simpler case is to adjust the size of the partitions, to better
match the space effectively available on a specific media.

The system designer might want to add other partitions, for special
purposes, for example to preserve configuration or logging data.

In this case, simply copy and modify one of the existing
sections, using a different name.
