.. _firewall-configuration:

Configuring Ostro |trade| OS Firewall
#####################################

Initial firewall ruleset
========================

Ostro OS loads its default firewall rule set from two files:
``/usr/share/iptables-settings/iptables.rules`` for the IPv4 firewall
and ``/usr/share/iptables-settings/ip6tables.rules`` for the IPv6
firewall. These two files contain security-restricting defaults for
Ostro OS with no services running. A default rule set is provided by
``iptables-settings-default`` recipe.

The default Ostro OS firewall configuration is a restrictive one.
Briefly, all incoming packets are dropped, except for those belonging to
already established connections or those that are coming from the
loopback interface. Forwarding packets is not allowed. All outgoing
packets are accepted. The IPv6 firewall is configured to accept
incoming ICMPv6 packets.

You can change the default rule set by creating a new rule set recipe
file. Here's an example file we'll call
``iptables-settings-custom_0.1.bb``:

::

    DESCRIPTION = "Custom iptables and ip6tables settings."
    LICENSE = "MIT"
    LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

    SRC_URI = " \
        file://custom-iptables.rules \
        file://custom-ip6tables.rules \
    "

    inherit update-alternatives

    # If you have a system without IPv6 support, just drop out the
    # configuration files for ip6tables.

    ALTERNATIVE_${PN} += "iptables.rules ip6tables.rules"
    ALTERNATIVE_LINK_NAME[iptables.rules] = "${datadir}/iptables-settings/iptables.rules"
    ALTERNATIVE_LINK_NAME[ip6tables.rules] = "${datadir}/iptables-settings/ip6tables.rules"
    ALTERNATIVE_TARGET[iptables.rules] = "${datadir}/iptables-settings/custom-iptables.rules"
    ALTERNATIVE_TARGET[ip6tables.rules] = "${datadir}/iptables-settings/custom-ip6tables.rules"

    FILES_${PN} += "${datadir}/iptables-settings/"

    do_install() {
        install -d ${D}${datadir}/iptables-settings
        install -m 0644 ${WORKDIR}/custom-iptables.rules ${D}${datadir}/iptables-settings/custom-iptables.rules
        install -m 0644 ${WORKDIR}/custom-ip6tables.rules ${D}${datadir}/iptables-settings/custom-ip6tables.rules
    }

The files ``custom-iptables.rules`` and ``custom-ip6tables.rules``
referenced in this recipe contain your firewall rules in a format that
is readable by ``iptables-restore`` and ``ip6tables-restore`` commands.
Make sure that the recipe can find the files when it's being built: put
the rule files for example in a ``files/`` subdirectory in the recipe
directory.

Finally, you tell the image build tools to use your
``iptables-settings-custom`` package (overriding the default
``iptables-settings-default`` package) by setting this variable in your
local.conf or image configuration:

::

    VIRTUAL-RUNTIME_iptables-settings = "iptables-settings-custom"

Now, when you build a new image, it has the ``iptables-settings-custom``
package installed instead of ``iptables-settings-default`` package.


Opening firewall holes for services
===================================

System services dynamically configure firewall settings so they function
properly when they are started (or when the systemd socket activation is
initiated) and undo those changes when the service is stopped (or when
the systemd socket activation is disabled).

The firewall setting changes made by services must not change the
fundamental way the firewall is set up. That's done from the initial
ruleset. The firewall settings the services do must not compromise the
firewall security or interfere with the operation of other services or
applications. Ostro OS does not have a centralized firewall control, so
the service writers must be careful about this.

There is no abstraction layer for making changes to the firewall; the
services call ``iptables`` and ``ip6tables`` directly. All services in
Ostro OS are started by systemd, so the firewall setup is often done
from systemd service files.

For example, sshd is a service started by systemd via socket activation when it
receives an incoming connection to port 22. To open the IPv6 port in the
firewall, openssh recipe writes the following configuration to
``/lib/systemd/system/sshd.socket.d/opensshd-ipv6.conf``:

::

    [Unit]
    After=ip6tables.service

    [Socket]
    ExecStartPre=/usr/sbin/ip6tables -w -A INPUT -p tcp --dport ssh -j ACCEPT
    ExecStopPost=/usr/sbin/ip6tables -w -D INPUT -p tcp --dport ssh -j ACCEPT

The ``ExecStartPre`` and ``ExecStopPost`` values tell systemd to run the
``ip6tables`` commands when ``sshd.socket`` file is loaded and unloaded. Note
the ``-w`` parameter: it tells ``ip6tables`` to wait for the firewall lock even
if the command didn't get it at first, meaning that the firewall operations are
run in a sequence. The ``-w`` parameter must be present for all ``iptables`` and
``ip6tables`` commands to prevent concurrency problems.

Opening holes to firewall using this method is not absolutely mandatory.
If you are building a device without dynamic services or applications,
you can simply add the necessary rules to the custom ruleset that is
loaded upon device startup.

Note that if you are starting your service as non-root user (as you
probably should be) using systemd's ``User=`` option, you'll need to
make sure that the firewall manipulation commands are run with original
permissions. An easy way to do that is to use
``PermissionsStartOnly=true`` option in the service file. This works if
you don't need to run any other ``ExecStartPre=`` or similar commands
with the reduced non-root privileges.

Opening firewall holes for applications
=======================================

All this work for opening necessary firewall holes is abstracted away
for applications. It's enough for applications to declare the ports that
they are using in the application manifest. The :ref:`application-framework`
will take care of generating and applying suitable firewall rules.
