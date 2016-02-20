.. _certificate-handling:

Certificate Handling in the Ostro |trade| OS
############################################

This document explains how certificates and secret keys are managed in
the Ostro |trade| OS.


SSL certificates
================

SSL certificates are used by libraries like openssl or gnutls and thus
by higher-level libraries and tools like libsoup, libcurl, curl, and wget
to verify the authenticity of their peer when connecting to a remote
server. node.js uses openssl and thus also uses the system
certificates.

Ostro OS uses ca-certificates from OpenEmbedded without
modifications. ca-certificates itself is taken by OE from Debian,
which in turn contains certificates as maintained by the Mozilla
foundation for the Firefox browser. All of these certificates are
enabled in Ostro OS.

These certificates are installed in ``/usr/share/ca-certificates``
by the ca-certificates package's 
``update-ca-certificates`` tool. That tool maintains
``/etc/ssl/certs`` containing both individual certificates in ``.pem``
format and a single ``certificates.crt``. Some of the consumers of
these certificates need the ``.pem`` files, while others need
``certificates.crt``.


Managing custom SSL certificates
--------------------------------

You should package new ``.crt`` files so they get installed under
``/usr/local/share/ca-certificates``, depend on ca-certificates, and
call ``update-ca-certificates`` in postinst and postrm scripts. Adding
or removing that package then will update the system SSL certificates
accordingly. Because the Ostro OS does not support individual packages in
installed images, this must be done when preparing the next revision
of an image.

Alternatively, certificates can also be modified directly without
packaging them, if the process manipulating
``/usr/local/share/ca-certificates`` and calling
``update-ca-certificates`` has write access to that directory and
``/etc/ssl/certs``. However, in the recommended security configuration
of Ostro OS that directory is not writable, so in practice updating
certificates on a device has to be done via an OS update.

Removing system SSL certificates
--------------------------------

In a ``ca-certificates_%.bbappend`` configuration file, you can extend
``do_install()`` to make further modifications to
``${D}${sysconfdir}/ca-certificates.conf`` before the ca-certificate
package gets created.


IMA/EVM and image signing
=========================

Linux IMA (Integrity Measurement Architecture) and EVM (Extended Verification Module) 
are technologies which ensure integrity by signing hashes of
file content and file meta data, respectively. There are several keys
involved:

* A root certificate authority: the public part is compiled
  into the Linux kernel itself and is installed on the device
  as part of the kernel.

* A signing key signed by the CA: the public part gets
  installed into ``/etc/keys/x509_evm.der`` of the initramfs at
  initramfs creation time.

The private keys need to be available only when building the Linux
kernel and images.


Creating IMA/EVM keys
---------------------

meta-integrity/README.md contains instructions for creating new
keys. As a default, that layer also provides keys which are known to
anyone and thus should not be used in production.

Updating IMA/EVM keys
---------------------

Updating keys is only possible as part of a complete image update because the
keys are not packaged. Updating the public keys
requires re-signing files with private keys, which are not available
on the device.

Updating keys in a running system is problematic: if IMA is active,
replacing core system components (like libc) with files that the
currently running kernel does not trust is going to make the
replacement libc unusable.
