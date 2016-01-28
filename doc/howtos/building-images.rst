Building Images
###############

Initial Steps
=============

1. Check out the ``ostro-os`` repository.
2. In the repository, run ``. oe-init-build-env``.
3. Update the ``conf/local.conf`` (see next section)
4. ``bitbake ostro-image``
5. Install and boot as described in `booting-and-installation`_

.. _`booting-and-installation`: booting-and-installation.md


Image Configuration
===================

Building images depends on choosing the private keys that are needed
during the build process. One either has to generate and configure
these keys or disable the features which depend on them.

In addition, images are locked down by default: for example, none of
the existing user accounts (including root) has a password set, so
logging into the running system is impossible. Some way of interacting
with the system after booting it has to be chosen before building
images.


Base Images
-----------

``ostro-image.bb`` is the image recipe used by the Ostro
project. It uses image features (configured via ``IMAGE_FEATURES``) to
control the content and the image configuration.

Internally, several virtual image variants are created from that base
recipe. They differ in the set of image features added or removed
from the base recipe:

ostro-image:
    The default image. Contains all programming runtimes.

ostro-image-dev:
    The same as ostro-image, plus build and debugging tools.

ostro-image-minimal:
    A smaller image which still has the core OS, but none of the
    optional runtimes.

Additional image variants can be defined in the ``local.conf``. For
example, the following adds ``ostro-image-noima`` and
``ostro-os-dev-noima`` as build targets where IMA is disabled and thus
no IMA keys are needed::

    OSTRO_EXTRA_IMAGE_VARIANTS = "imagevariant:noima imagevariant:dev,noima"


Development Images
------------------

All images provided by the Ostro Project are targetting
developers. Because the project wants to avoid having developers
accidentally build images for real products that have development
features enabled, explicit changes in ``local.conf`` are needed to
enable them.

Developers building their own images for personal use can follow these
instructions to replicate the published Ostro images. All necessary
private keys are provided in the ``ostro-os`` repository.

To do that, in step 3. above, edit ``conf/local.conf``, find the line
with ``# require conf/distro/include/ostro-os-development.inc`` and
uncomment it.


Production Images
-----------------

When building production images, first follow the instructions
provided in meta-integrity/doc/README.md for creating your own
keys. Then set ``IMA_EVM_KEY_DIR`` to the directory containing
these keys or set the individual variables for each required
key (see ``ima-evm-rootfs.bbclass``).

Then add your custom applications and services by listing them as in
the following example, which adds ``strace`` to the ``ostro-image``::

    CORE_IMAGE_EXTRA_INSTALL_append_pn-ostro-image = " strace"

This example assumes that ``bitbake ostro-image`` is used to build
an image. By making the append conditional on the name of the image,
different images can be built with different content inside the same
build configuration.

