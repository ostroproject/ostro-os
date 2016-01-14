Ostro Application Framework
===========================

1. Background
-------------
The application framework tries to be bare minimalistic, mostly built
around systemd services and containers.  It should be possible to lift
over existing code or applications to Ostro with minimal effort. No
mandatory changes should be necessary to code. Ideally it should be
enough to slam a small piece of additional Ostro-specific metadata
(the so-called application manifest) to an application and be done
with it.


2. Framework
------------
The 'Application Framework' consists of two actual components: an
installer and a systemd generator. The details of the installer are
still open, since it is undecided in which format 3rd-party
applications will be delivered. At least `ClearLinux
<https://clearlinux.org/>`_ bundles and XDG-APPs are being considered
as alternatives. In either case, the current understanding is that the
installer will be a simple wrapper script with minimal additional
functionality around a utility that takes care of installing an
application in the eventually chosen format.

The systemd generator component produces systemd service files for the
applications using the application manifests as its primary source of
information.


3. Usage of Containers
----------------------
Containers are used for filesystem 'virtualization' and for isolating
applications from each other. Applications can be packed together with
libraries they depend on. Application specific libraries are visible
only to the applications they are bundled with, not to the rest of the
system. While applications are installed in non-standard locations
``(/apps/*)``, the runtime view of the filesystem provided to an
application looks like a standard one (configuration files in
``/etc``, libraries in ``/usr/lib[64]``, binaries in ``/usr/[s]bin,
etc``), application- specific and system-wide bits blended together
using a combination of bind- and overlay-mounts.


4. Container Types
------------------
Ostro supports systemd-nspawned containers and (we're looking into
supporting) XDG-APPs inside containers. If configured so in the
manifest, applications can be started without containers, simply
augmenting ``$LD_LIBRARY_PATH``, ``$PATH``, and overriding ``$HOME``
appropriately.  We were also asked to consider supporting the addition
of new container types by simple plugins in the generator. The plugin
would get fed the container-specific fragments of the manifests and
generate the necessary bits (mostly the ``ExecStart*`` parts) in the
systemd service as it sees fit. This is how the nspawn-specific code
actually already works in Ostro, the only difference being that it is
not loaded as a DSO, rather it is compiled statically into the
generator.


5. Manifests
------------
Sometimes it might be necessary or desirable to be able to limit the
available functionality and configurability exposed to
applications. In other words, it might be necessary or desirable to
present a simplified manifest to the applications with less
configurability (or possibility for errors). For instance, it might be
good idea to have a limited set of predefined application classes from
which an application provider must choose one that best fits its
application. In this case, most of the configuration for the
application comes implicitly by selecting the application class,
instead of being explicitly stated in the manifest. The idea of having
such a possibility is good. However, at the moment nobody can say for
sure how many and what such classes would be.

Therefore we want to support both the limited and simplified and full
configurability and let end-users choose which one they go with.
To be able to do this, we'll allow the user-visible manifest to be fed
to a 'preprocessor' (again a simple plugin/DSO) before it is passed on
to the core of the systemd service generator. The preprocessor can do
arbitrary translations (JSON-in-JSON-out) of the manifest. Ostro contains
a sample preprocessor which can currently interpret the following
manifest format::

  /*
  * Application manifest keys:
  *
  *   - application: string
  *         Application identifier, mostly used for generating a few
  *         filesystem paths and file names.
  *
  *   - description: string
  *         A verbose description of the application.
  *
  *   - provider: string
  *         Unix user the application is executed as.
  *
  *   - groups: string
  *         If given, the Unix group the application is executed as.
  *
  *   - environment: dictionary (strings keys with string values)
  *         Extra environment variables to set for the application.
  *
  *   - command: array (of strings)
  *         The command line to start the application.
  *
  *   - autostart: boolean
  *         Whether to automatically attempt to start the application
  *         upon system boot.
  *
  *   - container: dictionary
  *         If the application is to be run inside a container, specifies
  *         the configuration for the container. Note that currently only
  *         systemd-nspawned containers are supported.
  *
  *         o type: string
  *             Container type to use, currently must be 'nspawn'.
  *         o network: string
  *             Container network configuration. Currently 'VirtualEthernet'.
  *         o sharedsystem: boolean
  *             Whether to run the container in a shared PID, UTS, and IPC
  *             namespaces.
  *
  */

  {
    "application": "sample-app",
    "description": "An application for frobnicating foobar and xyzzy.",
    "provider": "provider-1",
    "groups": "provider-1-group",
    "environment": {
        "FROB": "nicate",
        "FOOBAR": "xyzzy",
    },
    "command": [ "/usr/bin/test-1.sh" ],
    "autostart": "true",
     "container": {
        "type": "nspawn",
        "network": "VirtualEthernet",
        "sharedsystem": false,
    },
  }


6. Building an application using Ostro application framework
------------------------------------------------------------
Ostro application framework includes a set of very simple sample
applications, which show you how to bind your application to the
framework. There's a "hello world" application in native C with
autotools and similar server application in NodeJS.

Porting your application for Ostro application framework couple of
simple steps:

1. Write yocto recipe for your application
2. Inherit from iot-app class in your recipe
3. Define IOT_USER_NAME and IOT_APP_NAME in your recipe
4. Write a manifest for your application and include it to your recipe

We have a simple helper yocto class called "iot-app" which you can
inherit to your application to make things little bit easier::
  
  inherit useradd

  # Tell useradd where the post-install script should go.
  USERADD_PACKAGES = "${PN}"
  
  # Set the defaults
  IOT_USER_SHELL ??= "/sbin/nologin"
  IOT_USER_APP_NAME ??= "${IOT_USER_NAME}-${IOT_APP_NAME}"
  
  # Create the user with disallowed login and no extra groups.
  USERADD_PARAM_${PN} = "-s ${IOT_USER_SHELL} ${IOT_USER_APP_NAME}"
  GROUPADD_PARAM_${PN} = ""
  GROUPMEMS_PARAM_${PN} = ""
  
  IOT_APP_DIR ??= "/apps"
  IOT_APP_HOME ??= "${IOT_APP_DIR}/${IOT_USER_NAME}/${IOT_APP_NAME}"
  
  export IOT_APP_HOME
  RDEPENDS_${PN} = "iot-app-fw"
  
  do_install_append () {
    if [ -d "${D}${IOT_APP_HOME}" ] ; then
       chown -R ${IOT_USER_APP_NAME}.${IOT_USER_APP_NAME} ${D}${IOT_APP_HOME}
    fi
  }

Basically this class is inheriting from yocto oe-core useradd class
which helps to create users on the first boot of the device. User name
is a catenation from the IOT_USER_NAME and IOT_APP_NAME you give in
your application recipe. Also a home directory will be created for the
user. What this means in practive is that we have a dedicated user for
each app running in the system. The class will also create the
dedicated "apps" directory for the user/app combination and export
IOT_APP_HOME variable for you to use in your recipe to install
applications to correct place.

Here is the simplified recipe for the sample "hello-world" C program::
  
  IOT_USER_NAME = "yoyodine"
  IOT_APP_NAME = "nativetest"
  
  SRC_URI = "file://hello-world.c"
  
  inherit iot-app
  
  FILES_${PN} = "${IOT_APP_HOME}/bin"
  FILES_${PN} =+ "${IOT_APP_HOME}/manifest"
  
  PACKAGES = "${PN}"

And here is the manifest for the hello-world C program::
  
  {
    "application": "nativetest",
    "description": "test native application to see if the infra worked",
    "provider": "yoyodine",
    "groups": "yoyodine-nativetest",
    "environment": {
        "FROB": "nicate",
	"FOOBAR": "xyzzy",
    },
    "command": [ "/bin/hello-world" ],
    "autostart": "false",
    "container": {
        "type": "nspawn",
        "network": "VirtualEthernet",
        "sharedsystem": false,
    },
  }

When this application is added to the image user
``yoyodine-nativetest`` is created in the first boot or when
installing the application. Also application framework systemd service
file generator is running at boot and generating a service file for
the application.  You should see the application under
``/apps/yoyodine/nativetest`` and you can see the user
``yoyodine-nativetest`` for example in ``/etc/passwd``. The generated
systemd service file should be in
``/run/systemd/generator/yoyodine-nativetest.service``.

You can now start and stop your application with ``systemctl`` (like
``systemctl start yoyodine-nativetest.service``). From the service
file you can see what happens: systemd-nspawn container is created
with defined user, your application directory is overlay mounted and
the applications is started in the container.
