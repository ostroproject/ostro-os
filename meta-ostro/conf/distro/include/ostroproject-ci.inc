# XXX Drop the VM hack after taking care also of the non UEFI devices (those using U-Boot: edison and beaglebone)
OSTRO_VM_IMAGE_TYPES = "dsk.zip dsk.vdi.zip"

# Include the devel settings
require conf/distro/include/ostro-os-development.inc
