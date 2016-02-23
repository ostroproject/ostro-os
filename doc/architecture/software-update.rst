.. _software-update:

Software Update Mechanism for Ostro |trade| OS
##############################################

Introduction
============

Ostro-based software can be deployed to a target device in two ways:

- Full Disk Flashing

  A new software image is built and installed, completely replacing
  what was previously present on the device.
  It can be useful for initializing a device with Ostro.

- Software Update

  This is a component that Ostro borrows from The Clear Linux\* OS
  for Intel |reg| Architecture and consists of both a server and client
  component.


Software Update Server
======================

The software update server runs elsewhere than on the device, for example
on a CI (Continuous Integration) server.
For each build, the server generates information specific to that build
(in software update lingo it's the delta from version 0) and related to
previous builds (deltas from a customizable number of previous versions).

The information produced by the server is then exposed over an HTTP server
and consumed by the software update clients that run on the supported devices.

Such information is secured by generating hashes of each file and then
signing the file containing the references to the hashes.
It doesn't matter that the channel used to distribute the updates is secure.
As long as the signature and integrity checks are satisfied, the software
update client will treat them as trusted.


Software Update Client
======================

The client runs on the device and is responsible of downloading, verifying
(signature verification to be implemented) and applying the updates.
It can also restore to their pristine state files that were present in the
initial sw image and have been modified.


SW Bundles
==========

The software update mechanism supports the concept of bundles_: groups of files
that provide one functionality.
It is similar to the concept of package used in the vast majority of linux distros,
but in general one software update bundle maps to several packages (ex: .rpm or .deb)

There is one main os-core bundle containing everything that is mandatory for having
a bare-bones working system.
Everything else is optional and can be either deployed or removed by using the
software update client program.

Ostro developers can also use bundles following the rule that each application is
contained in its own bundle.

.. _bundles: https://clearlinux.org/documentation/bundles_overview.html

XXX TODO: add here or in the howto some info on how to create bundles, once that part
is working.
