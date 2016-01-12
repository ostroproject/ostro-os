# Overview of the current situation, post M2:

| MACHINE  | Hardware | Image Format | Booting | Installation |
|---|---|---|---|---|
| intel-corei7 | MinnowBoardMAX, GigaByte | .dsk | dd the image to the preferred media and select it from the UEFI BIOS | Same as booting |
| intel-quark | Galileo | .dsk | dd the image to the preferred media and select it from the UEFI BIOS |  Same as booting |
| intel-corei7, intel-quark | VirtualBox | .vdi | Select the image from the VirtualBox menu |  Create a machine with UEFI support and select the emulated SATA controller |
| edison | Intel Edison | same as M2 | same as M2 | same as M2 |
| beaglebone | BeagleBone Black  | same as M2 | same as M2 | same as M2 |

# .dsk

Raw image, in GPT format, contains at least one UEFI bootable partition and at least one ext4 partition (rootfs) - for details on disk layout see associated .json file in the same download directory.

# .vdi

.dsk converted to VirtualBox format. No other differences from the originating image.

---
---
---
# Overview of the situation in M2:

| MACHINE  | Hardware | Image Format | Booting | Installation |
|---|---|---|---|---|
| intel-corei7-64, intel-core2-32 | MinnowBoardMAX (choose 32 or 64-bit image such that it [matches the BIOS](http://www.elinux.org/Minnowboard:MaxBios#32-bit_vs._64-bit_UEFI)) | hdddirect | dd hdddirect to SD card or USB stick, boot from that | same as booting (no internal storage) |
|   | NUC | hdddirect  | same as MinnowBoardMAX | boot into some kind of OS (could be Ostro OS), dd hdddirect to /dev/mmcblk0 (untested) |
|   | VirtualBox | vdi | set up virtual machine with one disk based on the vdi file; if booting fails with a [kernel panic regarding snbep_uncore_msr_init_box](https://bugzilla.yoctoproject.org/show_bug.cgi?id=8271) then the host hardware is too recent and needs a VirtualBox >= 5.0 with paravirtualization mode set to "Default" instead of "Legacy" (as used in machines created by older VirtualBox) | n.a. |
|   | VMWare | vmdk | set up virtual machine with one disk based on the vmdk file (untested) | n.a. |
|   | kvm, qemu | qcow2 | set up virtual machine with one disk based on the qcow2 file (untested) | n.a. |
| intel-quark | Intel Galileo Gen 2 | hdddirect | same as MinnowBoardMAX | n.a. |
| edison | Intel Edison | ??? | ??? |
| beaglebone | BeagleBone Black | ostro-image-beaglebone.tar.bz2 | see [Creating bootable SD card for BeagleBone](Creating bootable SD card for BeagleBone) | same as booting |
| qemux86[-64] | qemu | kernel + .rootfs.ext4 | `runqemu qemux86[-64] ostro-image ext4 'qemuparams=-initrd tmp-glibc/deploy/images/qemux86/ostro-initramfs-qemux86[-64].cpio.gz' 'bootparams=rootflags=i_version rootfstype=ext4'` | n.a. |
|  |   | hdddirect | `runqemu qemux86[-64] ostro-image hdddirect` | n.a. |

See local.conf[.sample] for the current set of supported values for MACHINE and the corresponding hardware.

# hdddirect

Raw full-disk image of a MS-DOS (aka MBR) partition table with one VFAT boot partition and one ext4 rootfs. Size is fixed at compile time. Boot partition contains kernel, initramfs (optional, might also get compiled into kernel), syslinux (for traditional booting) and gummiboot (for UEFI booting).

Currently this image gets created by the boot-direct.bbclass in OE-core, using hard-coded calls to parted and dd. The plan is to switch to a more flexible way of creating these images with wic. This should not impact the way how the image gets used.

# vdi/vmdk/qcow2

Content is exactly the same as in hdddirect because these images get created by image-vm.bbclass by converting the hdddirect image with `qemu-img convert`.

# ostro-image-beaglebone.tar.bz2

tar archive of the rootfs. Care must be taken to preserve xattrs when creating and extracting it.

# .rootfs.ext4

Raw partition image containing the rootfs. Copied verbatim into .hdddirect partition or used directly by qemu.

# initramfs + kernel

In the past (pre-M2), the initramfs was optional and only used for booting live images (either setting up a loop-mounted rootfs or offering an install option). Now the initramfs contains code which sets up IMA. Therefore it should always be preserved when installing Ostro OS.

The initramfs is based on the OE-core initramfs-framework, so it is possible to extend it by installing additional packages into the core-image-minimal-initramfs. See the meta-intel-iot-security/meta-integrity for an example.

The "install" option itself is no longer supported (was not an official feature and only happened to work when using the existing live image initramfs).

# Architecture comparison

Building for each MACHINE in a local.conf (first column in the table above) creates packages suitable for the architecture. Sometimes, builds for different machines result in packages that are the same as for a different machine (for example, same CPU, or content of the package just plain text that is the same everywhere). This table summarizes the architecture names as found in the Ostro OS package feeds.

*TODO*
