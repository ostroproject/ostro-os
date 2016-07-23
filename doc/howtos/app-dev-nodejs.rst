.. _app-dev-nodejs:

Ostro |trade| OS Application Development Using Node.js
#######################################################

Node.js\* is a JavaScript runtime built on the Google\* V8 JavaScript
engine. Node.js uses an event-driven, non-blocking I/O model that makes
it lightweight and efficient. The Node.js package ecosystem, *npm*, is
the largest ecosystem of open source libraries in the world.

Ostro |trade| OS includes Node.js application runtime integrated in all image
configurations. With Node.js you can develop IoT applications using
JavaScript on Ostro OS. During the development phase you can use npm to
install additional Node.js modules to speed up your development process.
When using Node.js you don’t need to use Yocto build tools and the Ostro
OS SDK for your development. Node.js and npm are enough (until you’re
ready to deploy your application).

Making Your First Node.js application
=====================================

You can start your Node.js application development on any host machine
which supports Node.js. The supported Node.js operating systems includes
Windows, Linux, and OS X. For the Node.js installation on you host
machine, consult the https://nodejs.org web pages.

To start your first Node.js application, create a file, e.g., ``index.js``,
using a text editor (like vi), as shown::

   var os = require("os");
   function printMem() {
      console.log("Free mem on " + os.hostname() +
         ": " + os.freemem());
   }
   setInterval(printMem, 1000);

This Node.js application is using two Node.js APIs, ``os`` and ``timers``, to
get and print the hostname and amount of free memory once a second on
the console.

You can run the application by using the following command::

   $ node index.js

Stop the program by pressing CTRL-C. You can run the same application on
your Ostro OS device or on your host machine.

Pre-installed NPM packages
==========================

Ostro OS images contains the following npm packages pre-installed and
validated:

`Iotivity-node <https://www.npmjs.com/package/iotivity-node>`__
  JavaScript APIs for Open Connectivity Forum (OCF) specification using
  the open source IoTivity project implementation. With this package, you
  can easily develop OCF compliant applications with JavaScript on Ostro
  OS.

`iot-rest-api-server <https://www.npmjs.com/package/iotivity-node>`__
  Provides RESTful APIs for Ostro OS. Built with JavaScript using
  Node.js and iotivity-node frameworks, the iot-rest-api-server provides
  OCF REST API (explained in the next section) and system information. The
  Ostro OS RESTful services can easily be extended by using the
  iot-rest-api-server.

`Mraa <https://www.npmjs.com/package/mraa>`__ 
  IO library with
  JavaScript APIs that helps you use I2c, SPI, gpio, uart, pwm, analog
  inputs (aio), and more on a number of platforms such as the Intel®
  Galileo board, the Intel® Edison board, and others

All the npm packages are located in ``/usr/lib/node_modules`` directory on
the Ostro OS device.

Services based on Node.js Applications
======================================

The following RESTful services are not enabled by default. In order to
use the services they need to be enabled first with the following
command::

   root@edison:~# systemctl enable iot-rest-api-server.socket

The iot-rest-api-server provides the following RESTful services on Ostro
OS::

   /api/system
   /api/oic

These services are REST API endpoints. The full documentation of the
RESTful services can be found
`here <https://github.com/01org/iot-rest-api-server/tree/master/doc>`__.

To use the services, your mobile, cloud, or web application needs to
construct the full URL in the following way::

   <proto><port><api-endpoint><params>

The following examples assumes the iot-rest-api-server runs on IP
address: 192.168.0.1, port 8000.  Visit these urls in your web browser:

#. Get the system status using  ``http://192.168.0.1:8000/api/system``
#. Discover all the OCF enabled devices on the local network using:
   ``http://192.168.0.1:8000/api/oic/res``

Using NPM
=========

On Ostro OS -dev and -all images, the Node.js package manager (npm) is
pre-installed so you can use npm to manage Node.js packages.

For example, you can install the johnny-five sensor framework on Ostro
OS with the following command on the device::

   root@edison:~# npm install johnny-five

Creating and Installing Node.js Application
===========================================

In this section, we create a small Node.js application for Intel |reg| Edison
board, which uses the ``johnny-five`` IoT and Robotics framework. First,
create the ``package.json`` file with the the following content::

   {
   "name": "my-app",
   "version": "1.0.0",
   "description": "J5 Ostro Led Blinking",
   "main": "index.js",
   "license": "Apache-2.0",
   "dependencies": {
      "johnny-five": "^0.9",
      "edison-io": "^0.9"
      }
   }

This ``package.json`` file is the manifest of the application and contains
important information, including the application’s name and
dependencies. Full configuration documentation can be found
`here <https://docs.npmjs.com/files/package.json>`__.

Next, create the application code and place it in an ``index.js`` file::

   var five = require("johnny-five");
   var Edison = require("edison-io");
   var board = new five.Board({
      io: new Edison()
   });

   board.on("ready", function() {
      // Create a standard \`led\` component instance
      var led = new five.Led(13);

      // "blink" the led in half-second (500ms) on-off phase periods
     led.blink(500);
   });

The application above is very simple: it blinks the Intel Edison
on-board LED every half-second (500ms).

Once you are done with the development phase, or want to test your
application on the Ostro OS device, you must build the Node.js
application on the Ostro OS device.

To build your application, copy the two files (``package.json`` and
``index.js``) to your Ostro OS device, for example to ``my-app`` directory.

Then install the dependencies by using the following command::

   root@edison:~/my-app# npm install

This command requires an internet connection in order to fetch and install
all the dependent packages.

Running Node.js Application
===========================

To run your Node.js application, type the following command::

   root@edison:~/my-app# node index.js

If you want your Node.js application to be started every time the Ostro
OS device boots, you need to add a systemd service file for it. Below is
an example of the systemd service file for a Node.js application::

   [Unit]
   Description=Node.js application startup service
   After=network.target
     
   [Service]
   ExecStart=/usr/bin/node /home/root/my-app/index.js
   Environment='NODE_PATH=/usr/lib/node_modules/'
   Restart=on-failure

Name the file for example ``my-app.service`` and place it in the
``/lib/systemd/system`` directory.

Deploying Node.js Application
=============================

Once the Node.js application is ready to deploy it can be included in
Ostro OS based distribution image. This is done by using Yocto project
layers and recipes. An example of doing this can be found
in https://github.com/ostroproject/meta-iot-web. 
