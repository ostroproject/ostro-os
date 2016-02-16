.. _efi-boot:


EFI support in Ostro |trade| OS
###############################

On x86 devices, Ostro OS supports EFI mode through the creation
of a single-binary EFI application.


Background
==========
On typical distros (Fedora, Ubuntu, etc.) there are distinct
components that implement:

- boot loader
- kernel command line (usually part of the bootloader configuration)
- kernel
- initramfs (if present)

This typical model provides more choices to the user, but it introduces
additional points of failure in the security chain, because the EFI BIOS
only verifies the authenticity of the bootloader.
The bootloader has the burden of verifying the kernel, the initramfs
and its own configuration data, which must be signed individually.

The first part (BIOS verification of the bootloader) cannot be avoided,
because it's the first ring ofthe chain of trust.
The following (BIOS verification of kernel and initramfs) can only
introduce an additional risk, due to different implementation of what
is basically the same set of functionality already present in the BIOS.


EFI support in Ostro OS
=======================
Ostro OS relies on a single-binary approach, where the bootloader
(but only a small part of it), the kernel command line, the kernel and
the initramfs are all pacakged in a single file, which then gets signed.

Each component is placed in a separate section, inside the combo-binary.

Only the EFI stub is used from the bootloader.
The stub accomplishes these main functions:

- make the entire combo binary look like an EFI application, to the EFI BIOS
- extract the kernel command line from its section inside the binary
- handover the execution to the kernel section.

Advantages
----------

- only one file to handle, where most of the handling is performed by the
  BIOS, so that only one implementation exists for each functionality.
- no risk of components going out of sync: there is only one file to update
- less vulnerability to corruption of the EFI partition, during update.
  The EFI partition is of type FAT, as required by the EFI specifications,
  which means that it is significantly more exposed to corruptions than other
  more modern and saner file systems.

Disadvantages
-------------

- in case one wants to have multiple boot options, this needs to be supported
  through the EFI BIOS (more on this in the following point) and not all the
  BIOS implementations shine for supporting very well parts of the EFI
  specifications that are not indispensible for booting.
- the implementation of multi-boot selection will require either the creation
  of an additional EFI binary or the implementation of an EFI shell script.
  This sort of expertise might not be very common among Ostro developers.
- changing the content of the command line requires rebuilding the EFI combo,
  unless there is a mechanism in place to support an alternative (to be developed).
