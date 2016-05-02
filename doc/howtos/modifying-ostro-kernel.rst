.. _modifying-ostro-kernel:

Modifying the Ostro |trade| Kernel
######################################

Pre-requisites
==============
This document assumes that you have successfully followed the instructions to set up
your development system and are already able to generate Ostro OS images. 
Please refer to Getting Started Guide :ref:`quick_start` if you need help doing so.

This tech note describes one way to modify the Ostro kernel sources to add (or simply modify) 
a new driver. For alternative ways do this this, we recommend  
reading the `Yocto Project Linux Kernel Development Manual`_.

Preparing the Kernel Source Code
================================

Assuming the repository where you have cloned the Ostro source code is called ``ostro-os`` 
generate the initial image using these commands::

   cd ostro-os
   source oe-init-build-env
   bitbake linux-yocto

These steps will ensure you have built the kernel once by retrieving the sources and generating a Yocto Project ``.config`` file.

Modifying the Kernel
====================

The source code is located in the Yocto `${WORKDIR}`_ which 
is: ``tmp-glibc/work/corei7-64-intel-common-iotos-linux/linux-yocto/<kernel-version>/linux-corei7-64-intel-common-standard-build/source``. 
Make all the changes that you need, source code modifications including ``Kconfig`` and ``Makefile`` files if relevant.

* If needed, modify the kernel configuration to enable your changes::

    bitbake linux-yocto -c menuconfig

* Recompile the (modified) kernel:: 

    bitbake -f linux-yocto -c compile

  * Using ``-c compile`` ensures that :command:`bitbake` will **not** re-fetch the sources and wipe all changes you've just made.
  * Using the ``-f`` option forces the rebuild because :command:`bitbake` will not detect 
    changes you made in the Yocto `${WORKDIR}`_ and will think it has already successfully built the kernel.

* Compile all drivers (modules):: 
  
    bitbake -f linux-yocto -c compile_kernelmodules

Generating an Image with all the Changes
========================================

* To build a full image with this new kernel::
  
    bitbake ostro-image

This will generate a complete image and reuse the kernel that you've just modified and successfully compiled.

Integrating the Changes in your Source Tree
===========================================

Once you're happy with your new driver, the next step is to generate a patch and config fragment to be 
included in your source code so that your changes are always automatically applied.

.. _Yocto Project Linux Kernel Development Manual: http://www.yoctoproject.org/docs/2.0/kernel-dev/kernel-dev.html
.. _${WORKDIR}: http://www.yoctoproject.org/docs/2.0/ref-manual/ref-manual.html#var-WORKDIR