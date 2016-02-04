.. _booting-and-installation:

Booting and Installing an Ostro |trade| OS Image
#################################################

This technical note explains the basic procedures for taking an Ostro OS image that was downloaded
or built from source (using instructions in :ref:`Building Images`), and installing and 
running that image one of the :ref:`platforms`.

There are two images of interest for this process (depending if you're using real hardware or a VM):

:file:`.dsk`
    A raw disk image in GPT format and contains at least one UEFI bootable partition
    and at least one ext4 partition (rootfs).  For details on disk layout
    see the associated :file:`.json` file in the same directory as the image file.

:file:`.vdi`
    A :file:`.dsk` image converted to VirtualBox\* format (with no other differences).


Using dd to Create Bootable Media
---------------------------------

Once you have the :file:`.dsk` Ostro OS image you need to get it
onto your hardware platform, typically by using removable media such as a 
USB thumb drive or SD card.  The typical way to do this is with the :command:`dd` command.

   #. Connect your USB thumb drive or SD card to your Linux-based development system
      (minimum 2 GB card required). 
   #. If you're not sure about your media device name, use the :command:`dmesg` command to view the system log 
      and see which device the USB thumb drive or SD card was assigned (e.g. :file:`/dev/sdb`)::

        $ dmesg 

   #. The :command:`dd` command will overwrite all content on the device so be careful specifying 
      the correct media device. In the example below, :file:`/dev/sdb` is the 
      destination USB device on our development machine::

         $ sudo umount /dev/sdb*
         $ sudo dd if=<ostro-os-image.dsk> of=/dev/sdb bs=512k
         $ sync

      Unplug the removable media from your development system and plug 
      it into your target system.


MinnowBoard MAX
================

The `MinnowBoard MAX`_ is a small formfactor board with an Intel |reg| Atom |trade| E3825 dual-core processor (supporting both 32-bit and 64-bit images).  
Once you have the Ostro OS image on a USB thumb drive (or SD card), you can use this to boot your MinnowBoard MAX-compatible board. It's important
to use a current version of firmware on your board, so we recommend checking this first and updating the firmware if needed using the instructions 
at http://wiki.minnowboard.org/MinnowBoard_MAX_HW_Setup 

Here are the steps for booting the Ostro OS:

    #. Connect an HDMI monitor, USB keyboard, and network cable. Alternatively you can connect the serial 
       FTDI cable from the MinnowBoard to a USB port on your host computer and use a terminal emulator 
       to communicate with the MinnowBoard.)
    #. Plug in the USB thumb drive with your Ostro OS image to your MinnowBoard
    #. Power the board on.
    #. Wait for the system to enter the EFI shell where you can set the system date and time with the :command:`date` and :command:`time`
       (Because the MinnowBoard MAX does not have a battery for the RTC, the system date and time revert to the date and time
       when the firmware was created.)
    #. Enter :command:`exit` to return to the boot option screen
    #. Use the arrow keys to select Boot Manager, press return, then select EFI USB Device, and press return
    #. The Ostro OS will begin booting
    #. Debug information about the boot will display, then an Ostro OS identification line, followed by a login prompt.  Login as ``root``, with the password ``ostro``.


.. _MinnowBoard MAX: http://wiki.minnowboard.org


Gigabyte
========


Galileo
=======


Intel Edison
============