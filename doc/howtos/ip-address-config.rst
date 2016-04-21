.. _ip-address-config:

Configuring an IP Address in the Ostro |trade| OS
######################################################

The Ostro Project uses Connection Manager (ConnMan), a Linux daemon and command-line utility, for managing internet connections 
within embedded devices.

ConnMan supports these network technologies:

* Ethernet, using a built-in card, connected via host or client side USB
* WiFi, using wpa_supplicant
* Cellular connectivity using oFono
* Bluetooth connectivity using BlueZ

By default all technologies are disabled at the very first startup
to prevent unwanted wireless or wired communication from happening. ConnMan remembers the state of network
technologies over reboots. 
(You can read more about ConnMan at https://01.org/connman/documentation.)

This tech note explains how to connect your device to a network manually using the ``conmanctl`` command-line client.  For proper integration in 
an application, you should use the D-Bus APIs (and their bindings).  


Enabling Network Technologies 
=============================

Before a network transport (such as WiFi) can be used, it must be enabled in ConnMan. You can check to see what technologies
have already been enabled with the command :: 

   $ connmanctl technologies

The command will indicate if LAN and WiFi technologies are enabled. If not, you can enable either (or both) of them with the commands:: 

   $ connmanctl enable ethernet 
   $ connmanctl enable wifi 


ConnMan will automatically handle wired connections with a DHCP server.

Configuring a Static IP Address
================================

ConnMan refers to network devices as services. To configure a static IP address for a given LAN or WiFi service, 
you first find the name of the service assigned by ConnMan and then provide the IP address information, as 
shown in these steps: 

#. List the services available on your device ::

     $ connmanctl services

     *AO Wired                ethernet_0008a209b525_cable
         AnOpenNetwork        wifi_dc85de828967_4d6568657272696e_managed_none

   The wired service name discovered is ``ethernet_0008a209b525_cable``.

   Note: The symbols in the output above are: '\*' favorite (saved) network, 'A' autoconnectable, 'O' online and 'R' ready. 
   If no letter is shown in the O/R column, the network is not connected. In addition, temporary states include 
   'a' for association, 'c' configuration and 'd' disconnecting. When any of these three letters are showing, 
   the network is in the process of connecting or disconnecting. A network is in state 'ready' once it has 
   obtained an IPv4 or IPv6 address or both, and can indicate that the network might still need a proxy set up to get 
   internet connectivity.

#. Once you know the service name, you can assign a static IP with the command::

     $ connmanctl config <service> –ipv4 manual <ip address> <netmask> <gateway> 

   For example, using the service name discovered above: ::

     $ connmanctl config ethernet_0008a209b525_cable –ipv4 manual 192.168.1.4 255.255.255.0 192.168.1.1

You can assign a static IP to a discovered WiFi adapter service in the same manner.


Connecting to a WiFi Network
============================

You can run connmanctl with all the arguments on the command line (as we did in the previous examples), 
or you can use it as an interactive program.  We'll use this interactive interface
for the following example.  

Here are the steps to connect to a wireless network using DHCP:

#. Open connmanctl in interactive mode, enable WiFi (if you haven't already), and scan for new WiFi services (available SSIDs)::

     $ connmanctl
     $ connmanctl> enable wifi 
     $ connmanctl> scan wifi
     $ connmanctl> services 

#. To connect to a secure
   WiFi network, we need to register the agent to handle user requests. This agent is used by the daemon to 
   call back an application when attention or input is needed. If you're connecting to an (unsecured) open access point you 
   can skip this step ::

     $ connmanctl> agent on

#. Use the wireless network name and the service name displayed by the ``services`` command to connect to that network ::  

     $ connmanctl> connect wifi_<MAC_ADDR>_<SSID_HEX>_managed_psk

   If the wireless network is password protected, ConnMan will prompt you to enter the password before establishing 
   a connection. 

   An open unsecured access point would be displayed by the ``services`` command with an ``_managed_none`` suffix.

   For example ::

     $ connmanctl> scan wifi
     $ connmanctl> services

     G2_5078              wifi_a434d96b4f72_47325f35303738_managed_none
     Guest                wifi_a434d96b4f72_4775657374_managed_none

     $ connmanctl connect wifi_a434d96b4f72_4775657374_managed_none


#. Finally, exit the ConnMan console with the ``quit`` command.
 