.. _architecture-overview:

Ostro |trade| OS Architecture Overview
######################################

This document gives an overview of the Ostro OS architecture and its main
building blocks. Furthermore, the document briefly talks about how
Ostro OS meets different end-user use-cases ranging from hacking to
IoT product creation.

.. _`Yocto Project`: http://yoctoproject.org
.. _`Soletta Project`: http://solettaproject.org
.. _`Node.JS`: https://nodejs.org
.. _`IoTivity`: https://www.iotivity.org/
.. _`Ostro Project download server`: https://download.ostroproject.org
.. _`application sample recipes`: https://github.com/ostroproject/meta-appfw/tree/master/recipes-appfw
.. _`Open Connectivity Foundation`: http://openconnectivity.org/
.. _`systemd.generator`: https://www.freedesktop.org/software/systemd/man/systemd.generator.html

Ostro OS Characteristics
========================

In Ostro OS, there are four key characteristics that
drive the architecture design:

#. **Ostro OS uses standard libraries and services**: The building blocks
   used in Ostro OS are commonly used in many open-source projects and custom
   implementations are avoided to the extent possible. This has a big benefit
   as there is little porting or platform adaptation needed to get
   existing applications or services to run on Ostro OS; often times, all that's
   needed is to create a manifest for your application.

#. **Ostro OS is built with security in mind**: Security is
   critical for IoT and is a focus area in Ostro OS. The security
   design provides scalable options for security configurations
   in Ostro OS-based products. The security architecture is explained in
   more details in :ref:`system-and-security-architecture`.

#. **Ostro OS is easy to customize**: While Ostro OS comes pre-compiled
   (binaries and images), it can be customized
   to meet the diverse product needs of IoT applications. With the help of
   the Yocto Project build system used by Ostro OS, it is easy to customize
   the build and generated images that are finely tuned to meet your exact needs.
   :ref:`about_ostro` and the links provided there are an excellent starting point
   to learn more about the Ostro OS extensive customization possibilities. These
   pre-compiled images are intended to expedite your development work and not intended
   for use in production systems.

#. **Ostro OS is pre-compiled and pre-configured**: Ostro OS leverages the
   `Yocto Project`_ build system tools and is provided as a pre-compiled and pre-configured
   distribution specifically tuned for IoT device development. Generating and compiling your own
   Ostro OS image is very fast since the build system is configured to use the Shared
   State Cache (SSTATE) mechanism offered by the Ostro OS SSTATE server.
   In addition, pre-compiled reference images are available from the
   `Ostro Project download server`_ to get you started in no time.

Ostro OS Architecture Stack
===========================

One way to describe Ostro OS architecture is to build a stack from the
hardware platform up to an IoT Application layer. Such stack is
illustrated here.

.. image:: images/ostro_os_architecture.svg
   :width: 400px

The following sections examine each layer in more details.

IoT Applications
----------------
The IoT applications layer consist of all applications that use the
underlying platform. Ostro OS itself currently does not
implement any specific IoT use-cases via applications, but
`application sample recipes`_ are provided to demonstrate the OS frameworks and services.

Programming Interfaces
-----------------------

Ostro OS provides various application runtimes offering more flexibility and
options to application developers to implement their IoT solution.

* `Soletta Project`_ is an open-source
  framework for making IoT applications. The project provides libraries
  to make it quick and easy to write software for IoT devices. The
  applications can we written using flow-based programming (FBP) or
  more traditionally as C applications linking to Soletta's C-based
  platform APIs.

* `Node.JS`_ is a popular JavaScript runtime to
  run (IoT) web applications. Ostro OS provides the Node.JS runtime
  and selected JavaScript APIs (as Node.JS modules) to build IoT
  applications. The set of APIs includes, for example, a Javascript API for
  the `Open Connectivity Foundation`_ (OCF) specifications. The JavaScript
  API set is kept aligned with the API set provided by Soletta.

* Ostro OS also provides support for the popular IoT-space development
  languages Python and Java\* (OpenJDK8).

.. _`iotivity-node`: https://github.com/otcshare/iotivity-node

Frameworks
----------

Frameworks provide an abstraction to platform services, making
application deployment easier. The Ostro Application
Framework :ref:`application-framework` provides tooling for
application writers to get the applications running in an Ostro OS
based image.

The application framework is simple and focused on how to start each application
in its desired environment. It implements a `systemd.generator`_ that can generate
a systemd service based on the application needs as defined in its manifest.
Currently, the supported manifest keys will provide configuration options that will
open the firewall ports, use the correct user and groups, sandbox in a container
(if desired), and stitch the file system as desired by the application. This
means applications may have their own file system view, with parts of the system
being hidden or write-protected, and they may have a private network or even no
network at all.

Ostro OS also pre-integrates `IoTivity`_ framework. IoTivity is an open-source
project that implements the full OCF specification by `Open Connectivity Foundation`_.
This connectivity framework is also available from `Soletta Project`_ and Node.JS/`iotivity-node`_.

Services
--------

The responsibility of system services is to bring the system up,
manage connectivity and set up process' inter-process communication (IPC).
The components Ostro OS use are commonly found in many open-source OSes: systemd,
ConnMan, BlueZ, D-Bus and others.

In addition to systemd and connectivity, Ostro OS comes with
:ref:`software-update` technology tailored for IoT products. This means
efficient delivery of selected and quality assured software from a
single, vendor controlled, stream. The update technology copes with
the fast paced IoT environment and allows live updates, reducing
downtime by only restarting needed services

Base Libraries
--------------

Standard Linux base libraries are used in Ostro; the same libraries
and utilities that are available in all major distributions.

The `Yocto Project`_ build system tools used in Ostro OS also makes it
possible to easily extend the content of Ostro OS if there's a need to add new libraries.

For example, while Ostro OS 1.0 is focused on headless use-cases and no graphic
and multimedia libraries are enabled, one can use the `Yocto Project`_ build system
tools to incorporate them to your product.

Linux Kernel and Hardware Adaptation
-------------------------------------

The hardware board support packages (BSP) for Ostro OS run the Linux Kernel. The kernel
provides the necessary drivers and hardware adaptation.

Sensors and connectivity are critical for IoT devices. Ostro OS reference Linux
kernel configuration focuses on making as many sensors and connectivity peripherals
available for the end-users and makers. In addition, a dedicated page for :ref:`hardware` that
describes how various peripherals can be run with :ref:`platforms` is maintained.

Ostro OS Composition
====================

The Ostro OS is a composition of multiple Yocto Project build system
metadata layers maintained in individual layer repositories. The layers used
in Ostro OS are combined to form the ``ostro-os`` repo.

The following layer repositories are used in Ostro OS. The Board
Support Package (BSP) layers used bring hardware adaptation and
CPU architecure configuration for :ref:`platforms`.

.. _`openembedded-core`: http://git.openembedded.org/openembedded-core
.. _`meta-intel`: http://git.yoctoproject.org/meta-intel
.. _`meta-ostro`: https://github.com/ostroproject/meta-ostro.git
.. _`meta-ostro-fixes`: https://github.com/ostroproject/meta-ostro-fixes.git
.. _`meta-ostro-bsp`: https://github.com/ostroproject/meta-ostro-bsp.git
.. _`meta-intel-iot-security`: https://github.com/01org/meta-intel-iot-security.git
.. _`meta-appfw`: https://github.com/ostroproject/meta-appfw.git
.. _`meta-openembedded`: http://git.openembedded.org/meta-openembedded
.. _`meta-oic`: http://git.yoctoproject.org/meta-oic
.. _`meta-intel-iot-middleware`: http://git.yoctoproject.org/meta-intel-iot-middleware
.. _`meta-iotqa`: https://github.com/ostroproject/meta-iotqa.git
.. _`meta-iot-web`: https://github.com/ostroproject/meta-iot-web.git
.. _`meta-security-isafw`: https://github.com/01org/meta-security-isafw
.. _`meta-yocto`: http://git.yoctoproject.org/meta-yocto
.. _`meta-java`: https://github.com/intel-iot-devkit/meta-java.git
.. _`meta-soletta`: https://github.com/solettaproject/meta-soletta.git
.. _`meta-swupd`: http://git.yoctoproject.org/meta-swupd

============================ =======================================
Layer Repository Name        Description
============================ =======================================
`openembedded-core`_         Core metadata and component recipes
`meta-intel`_                BSP layer for common IA platforms
`meta-ostro`_                Ostro OS distro metadata, configuration,
                             and documentation
`meta-ostro-fixes`_          Ostro OS layer that is used to carry
                             fixes to upstream layers
`meta-ostro-bsp`_            Ostro OS BSP configuration metadata
meta-edison-bsp              BSP layer for Intel Edison (integrated
                             via the `meta-ostro-bsp`_ layer)
`meta-intel-iot-security`_   Security building blocks: IMA, SMACK.
`meta-appfw`_                Ostro OS application framework recipes
                             and sample applications
`meta-openembedded`_         Collection of OpenEmbedded layers
`meta-oic`_                  `IoTivity`_
`meta-intel-iot-middleware`_ Middleware components used in Intel IoT
                             DevKit
`meta-iotqa`_                Ostro OS test tools
`meta-iot-web`_              Node.JS and OIC JavaScript APIs
`meta-security-isafw`_       Image Security Analysis framework gives
                             offline tooling to analyze images
`meta-yocto`_                BSP layer for BeagleBone Black
`meta-java`_                 Java support (openjdk8)
`meta-soletta`_              `Soletta Project`_
`meta-swupd`_                Software update tooling
============================ =======================================

The Ostro OS distro configuration file (:file:`meta-ostro/conf/distro/ostro.conf`) defines
the global configuration of the OS. For example, it determines which components are being
enabled/built by default (via ``DISTRO_FEATURES``, ``PNBLACKLIST``, and ``PNWHITELIST`` settings).

Ostro OS Development Workflows
==============================

.. _`Yocto Project extensible SDK`: http://www.yoctoproject.org/docs/2.1/sdk-manual/sdk-manual.html#sdk-extensible

Ostro OS enables many options how to do hacking and/or IoT product development.

#. **Quick Prototyping**: Using the pre-built development images found in 
   `Ostro Project download server`_ it's easy to get started with any of the :ref:`platforms`. 
   Some of the image configurations also provide an environment to do quick prototyping with 
   programming tools discussed in 'Programming Interfaces' above.
#. **Image Customization**: Likely, the pre-built development images do not provide the desired 
   content or configuration for products. However, the images can easily be customized to suit 
   the needs as discussed on :ref:`Building Images`.
#. **Adding 3rd party content**: For device makers it's often necessary to bring in additional 
   3rd party libraries and product IoT applications while still keeping the base OS unchanged. 
   `Yocto Project extensible SDK`_ (discussed below) built for Ostro OS tries to make that process easy.

Extensible SDK
--------------

Using the `Yocto Project extensible SDK`_ built for Ostro OS makes it easy to add new applications 
and libraries to an image, modify the source for an existing component, test changes on the 
target hardware. Each Ostro OS build found in `Ostro Project download server`_ has an 
extensible SDK installer that is quick to download and install on user's development PC.

The ``devtool`` is the main tool when using extensible SDK. With ``devtool`` user can 
add new recipes/content, e.g., from Node.JS NPM registry and have them installed in the 
image or modify kernel configuration options. To build the new components and new images, 
the Ostro OS pre-compiled SSTATE cache (including the cross-development toolchain) is 
used (as long as it's valid).
