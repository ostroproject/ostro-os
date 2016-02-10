.. _quick_start:


Ostro |trade| OS Quick Start Guide
##################################

This quick start guide explains how to install the Ostro OS development environment on your
development system and to install and run applications on :ref:`platforms`.

Refer to the Ostro OS Release Notes in the Image Release area for specific details about capabilities and status
of features for the current release. 

This guide describes two ways to get started with your investigation and use of the Ostro OS: 

   * Download one of the pre-built Ostro OS images, ready to run on a supported hardware platform, or 
     emulated using a Virtual Machine.

   * Download the source code, examine and customize the OS and packages, and use the `Yocto Project`_ tools 
     to generate a new image that is tailored to your specific application needs.

.. _`Yocto Project`: http://yoctoproject.org


Access and Support
==================

Here’s a quick summary of resources to find Ostro OS images, source code,
documentation, and support systems:

* Ostro Project Website
   The website https://ostroproject.org is the central source of  
   information about the Ostro Project.  On this site you'll find current information
   about the project as well as all the relevent links to project material 
   (including these technical documents).

* Image Releases
   Pre-built Ostro OS images for all the :ref:`platforms` are available at
   https://download.ostroproject.org

   In there you’ll find an images folder with separate folders for each of
   the supported hardware platforms. In the platform folder, you’ll find an
   :file:`.dsk` file that can be written directly onto a hard disk or
   USB thumb drive and booted.  There’s also a :file:`.vdi` file for use with VirtualBox.

* Software Updates
   The Ostro OS uses a rolling updates development and release process using "bundle"  
   technology developed by the Clear Linux\* OS for Intel |reg| Architecture team.  You 
   can read more about bundles at `Clear Linux Project Software Update`_

.. _`Clear Linux Project Software Update`: https://clearlinux.org/features/software-update
   
* Source Code on GitHub
   Ostro OS source code is maintained on a public GitHub repository at
   https://github.com/ostroproject. Check out the README there for more information
   about the repository and its organization.

* Documentation
   Project techical documentation is under development and the document sources are
   stored along with the Ostro OS code on GitHub.  The document sources are processed 
   to generate the website documentation your currently reading.

* Issue Tracking with JIRA
   Requirements and Issue tracking is done with our public JIRA system at 
   https://ostroproject.org/jira/.  You can browse through the issues freely,
   but you'll need to create an account before submitting an issue of your own.

* Mailing List
   Mailing lists are a convenient way to communicate with Ostro project members as
   well as other developers interested in the Ostro OS.  These lists are perhaps
   the most convenient way to track developer discussions and to ask your own
   support questions to the Ostro OS community.  You can find a list of
   the available mailing lists, how to subscribe, and what each list is used for
   from https://lists.ostroproject.org
   You can also read through
   the mailing list archives to follow past posts and discussions.

* IRC Chatting
   You can chat online with the Ostro OS developer community and other users in
   our IRC channel **#<need a name here>** on the **<need a name here>** IRC server.
   Instructions for connecting are available at
   <server name goes here> and you'll need a client-side application
   such as :command:`pidgin`.  Communication on IRC is immediate but transient,
   making it good for meetings or a quick discussion.  (IRC discussions are
   not recorded so it's better to use the mailing list for open discussions
   with the community of developers.)


Prerequisites
=============

You can do Ostro OS development using a reasonable current Linux-based host
system capable of running Yocto Project tools used to configure and build 
Ostro OS images. You should be familiar
with the Yocto Project terminology and processes and how to use these tools as
documented at the `Yocto Project`_ web site.  A good place to start is with 
the `Yocto Project Quick Start Guide`_.

.. _`Yocto Project Quick Start Guide`: http://www.yoctoproject.org/docs/current/yocto-project-qs/yocto-project-qs.html

Downloading a Pre-Built Ostro OS Image
=======================================

A fast way to investigate the Ostro OS is to download one of the pre-built
Ostro OS images, ready to run on :ref:`platforms` (or emulated using a Virtual
Machine). Ostro OS images are available from  https://download.ostroproject.org

Within each of the hardware-specific release folders you’ll find an :file:`images` folder,
and in that folder, you'll find a :file:`.dsk` file that can be directly written to a hard disk 
or booted on a USB thumb drive (written there with :command:`dd`). This
:file:`.dsk` file contains a raw full-disk image with boot partition and rootfs
with sizes fixed at compile time.

Note that the bit-support of the UEFI firmware on your hardware platform (such as a MinnowBoard
MAX) and for the Ostro OS distro must match; i.e., you need a 64-bit Ostro OS
image for a board with 64-bit firmware. Check the firmware version on your
board to verify which bit-support is configured.

Once you’ve downloaded the image for your supported hardware, you're ready to load
and run that image on your :ref:`platforms` or emulation environment.


Setting up and Building an Ostro OS Image
=========================================

If you don’t want to use one of the pre-built images, you can get the Ostro OS sources and make your 
own image. We've written a :ref:`Building Images` tech note that explains this procedure. 

You should be familiar with the `Yocto Project`_ build tools as 
explained in the `Yocto Project Quick Start Guide`_.  This guide has step-by-step instructions 
and system requirements for setting up your host computer’s development environment and 
tools needed to build an Ostro OS image.

Briefly (and as fully explained in the `Yocto Project Quick Start Guide`_), you’ll need:

   *  A host system with a minimum of 50 Gbytes of free disk space that is running a supported 
      Linux distribution (i.e. recent releases of Fedora, openSUSE, CentOS, Debian, or Ubuntu). 
      If your host system supports multiple cores and threads, you can configure the Yocto Project
      build system to take advantage of this and significantly decrease the time needed to build images.

   *  Appropriate developer packages (gawk, make, python, perl, patch, and others) 
      installed on the system you are using for builds

   *  A release of the Yocto Project (included when you clone the ostroproject repo from GitHub).

Once you’ve followed the Yocto Project instructions to get your computer ready to host a project, 
you may also need to set up proxy information if your sitting behind a firewall.

You’ll also need to create an SSH public key (if you don’t already have one) and add that key to your GitHub 
profile as explained in these GitHub `Generating SSH Keys`_ instructions. (These instructions also show 
how to confirm that your proxy and SSH key are set correctly.)

.. _`Generating SSH Keys`: https://help.github.com/articles/generating-ssh-keys/

The `Yocto Project Quick Start Guide`_ offers detailed instructions and explanations about the build 
environment and processes. 

Briefly, you start by setting up the environment for building the Ostro OS by cloning the 
ostroproject GitHub repo, editing configuration files, and then starting the build.  Refer to 
the :ref:`Building Images` tech note for more information.  

If you made no changes, you should end up with a binary :file:`.dsk` file 
that is functionally equivalent to an image in the Ostro Project binary release folder.

Running an Ostro OS image
==========================

Once you have an Ostro OS image (by downloading a pre-built image or by building your own), 
you’ll want to install and run it on your target hardware or VM environment.  We've written
a :ref:`booting-and-installation` tech note that explains this procedure.
