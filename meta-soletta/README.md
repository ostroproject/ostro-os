#meta-soletta

This is the soletta yocto meta-layer. Soletta Project is a framework for making
IoT devices. With Soletta Project's libraries developers can easily write
software for devices that control actuators/sensors and communicate using
standard technologies. It enables adding smartness even on the smallest edge
devices.

If you have any question or want to propose any a change contact the soletta
project on github: https://github.com/solettaproject/.

##SmallOS

SmallOS is a distribution based on poky adding what seems to be required for
soletta framework + IoT (i.e systemd, udev, and all needed to produce a minimal
linux system).

##Dependencies

The dependencies to build the images are:
  - Yocto poky or later
  - meta-intel (If building for intel based-hardware is required)

##Build image for Intel Edison
Go to [Soletta wiki - Edison Instructions](https://github.com/solettaproject/soletta/wiki/Edison-Instructions#yocto)

##Build image for Minnowboard Max
Go to [Soletta wiki - MinnowBoard-MAX-Instructions](https://github.com/solettaproject/soletta/wiki/MinnowBoard-MAX-Instructions)
