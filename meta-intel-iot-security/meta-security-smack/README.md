This README file contains information on the contents of the
security-smack layer.

Please see the corresponding sections below for details.


Dependencies
============

This layer depends on:

    URI: git://git.openembedded.org/bitbake
    branch: master

    URI: git://git.openembedded.org/openembedded-core
    layers: meta
    branch: master

    URI: git://github.com/01org/meta-intel-iot-security
    layers: security-framework
    branch: master


Patches
=======

Please submit any patches against the security-smack layer via Github
pull requests.

For discussion or patch submission via email, use the
yocto@yoctoproject.org mailing list. When submitting patches that way,
make sure to copy the maintainer and add a "[meta-intel-iot-security]"
prefix to the subject of the mails.

Maintainer: Patrick Ohly <patrick.ohly@intel.com>


Table of Contents
=================

  I. Adding the security-smack layer to your build
 II. Misc


I. Adding the security-smack layer to your build
================================================

In order to use this layer, you need to make the build system aware of
it.

Assuming the security repository exists at the top-level of your
yocto build tree, you can add it to the build system by adding the
location of the security-smack layer to bblayers.conf, along with any
other layers needed. e.g.:

  BBLAYERS ?= " \
    /path/to/yocto/meta \
    /path/to/yocto/meta-yocto \
    /path/to/yocto/meta-yocto-bsp \
    /path/to/yocto/meta-intel-iot-security/meta-security-smack \
    "

It has some dependencies on a suitable BSP; in particular the kernel
must have certain Smack-related patches. For linux-yocto 3.14, the
necessary patches are added by this layer. The necessary kernel
configuration parameters are added to all kernel versions by this
layer.

Just adding the layer does not enable Smack. These changes can be
enabled and disabled separately via configuration variables. To enable
Smack security, add the following entries to local.conf:

    # Enable Smack support. May also be done by a distro config,
    # (using DISTRO_OVERRIDES and directly updating DISTRO_FEATURES,
    # without the _append).
    OVERRIDES .= ":smack"
    DISTRO_FEATURES_append = " smack"

    # Enable systemd.
    DISTRO_FEATURES_append = " pam"
    DISTRO_FEATURES_append += " systemd"
    VIRTUAL-RUNTIME_init_manager = "systemd"
    DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
    VIRTUAL-RUNTIME_initscripts = ""
    # CORE_IMAGE_EXTRA_INSTALL += "systemd-analyze"

    # Need Smack support in file utilities.
    CORE_IMAGE_EXTRA_INSTALL += "coreutils"

    # Having Smack utilities is useful.
    CORE_IMAGE_EXTRA_INSTALL += "smack-userspace"

By default, enabling Smack as described above will also make Smack
the default LSM when compiling the kernel, overriding the choice
that may or may not have been made in the BSP kernel config.

If that is not desired, a distro conf can use:
    # Do not override default LSM configuration.
    SMACK_DEFAULT_SECURITY ?= ""

Using the weaker "?=" assignment allows a user to revert that
choice once more in a local.conf with:
    # Make Smack the default LSM.
    SMACK_DEFAULT_SECURITY = "${SMACK_DEFAULT_SECURITY_CFG}"

II. Misc
========

This layer intentionally limits itself to configuration changes of
existing components, plus the new Smack userspace library and
tools. See the other layer(s) in this repository for higher level
security components meant to work together with Smack.

The layer limits itself to just setting up Smack rules for system
components (the "System" domain in the Tizen three-domain Smack
model). See recipes-core/base-files/base-files_%.bbappend for details.

That is because the "User" part heavily depends on how applications
are managed, which is out-of-scope for this layer. Whoever adds an
application framework which depends on Smack will also have to add the
necessary Smack rules and file attributes.
