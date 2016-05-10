#meta-soletta

The meta-soletta project is a meta-layer for [Yocto](https://www.yoctoproject.org/) that contains the needed recipes to cross-compile Soletta and generate images for a target board.

The meta-soletta is being supported by [Ostro OS](https://ostroproject.org/), an open source Yocto-based operating system for IoT devices, and it is the recommended method of using the meta-layer.
 
The generated images are snapshots of the operating system ready to be booted. Being Ostro-based they contain all the needed software for an easier IoT development.

In this page we include two ways of generating system images: one covers [how to build them with Ostro](#generating-the-images-with-ostro-os) (highly recommended) and the other one covers [how to build them with pure Yocto](#generating-the-images-with-yocto).

# Generating the images with Ostro OS

Ostro supports the following boards:
  - Intel Edison
  - MinnowBoard MAX
  - Intel Galileo Gen2
  - BeagleBone Black
  - GigaByte GB-BXBT-3825

To generate the image follow this Ostro documentation: [Ostro Project - Building Images] (https://ostroproject.org/documentation/howtos/building-images.html)

## Installing the images

To install the generated image follow this tutorial from Ostro: [Ostro Project - Booting and Installation] (https://ostroproject.org/documentation/howtos/booting-and-installation.html)

# Generating the images with Yocto

Only use this option if you are an advanced user of Yocto and you're sure of what you're looking for. Otherwise the [Ostro method](#generating-the-images-with-ostro-os) is highly recommended.

With pure Yocto we support the following boards:
  - Intel Edison
  - MinnowBoard MAX

To generate image with Yocto for MinnowBoard MAX: [Building for MinnowBoard MAX](https://github.com/solettaproject/soletta/wiki/MinnowBoard-MAX-Instructions)

To generate image with Yocto for Intel Edison: [Building for Intel Edison] (https://github.com/solettaproject/soletta/wiki/Creating-an-Edison-Image-with-Yocto)
