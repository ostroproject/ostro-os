DESCRIPTION = "Application framework daemon and client"
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "BSD-3-Clause"

LIC_FILES_CHKSUM = "file://LICENSE-BSD;md5=f9f435c1bd3a753365e799edf375fc42"

DEPENDS = "json-c systemd"

SRC_URI = " \
    git://git@github.com/ostroproject/iot-app-fw.git;protocol=ssh \
  "

SRCREV = "a324424c9173cc4b54a2bf1f496405a20013445e"

inherit autotools pkgconfig systemd python-dir pythonnative

AUTO_LIBNAME_PKGS = ""

S = "${WORKDIR}/git"

# possible package configurations
PACKAGECONFIG ??= "python"
PACKAGECONFIG[qt]         = "--enable-qt,--disable-qt,qt4-x11-free"
PACKAGECONFIG[pulse]      = "--enable-pulse,--disable-pulse,pulseaudio"
PACKAGECONFIG[glib-2.0]   = "--enable-glib,--disable-glib,glib-2.0"
PACKAGECONFIG[node]       = "--enable-nodejs,--disable-nodejs,nodejs"
PACKAGECONFIG[shave]      = "--enable-shave,--disable-shave"
PACKAGECONFIG[python]     = "--enable-python,--disable-python,python python-json glib-2.0 python-pygobject"

do_configure[prefuncs] += "set_python_env"

do_package[prefuncs] += "set_python_files"

PACKAGES =+ "${PN}-launcher"
FILES_${PN}-launcher = "${bindir}/iot-launch-daemon"
FILES_${PN}-launcher += "${bindir}/iot-launch"
FILES_${PN}-launcher += "${libdir}/iot-app-fw"
FILES_${PN}-launcher += "${systemd_unitdir}/system"

PACKAGES =+ "${PN}-test"
FILES_${PN}-test = "${bindir}/iot-event-test"

python set_python_env () {
    # Provide the build environment to distutils during Python
    # extension build and installation only when 'python' is enabled.
    # The arguments are close to what distutils.bbclas would add but
    # added manually to avoid its problems with our specific setup.
    if not "python" in d.getVar("PACKAGECONFIG", True):
        return

    d.appendVar("EXTRA_OECONF", " --with-python-PYTHONPATH=" + d.getVar("STAGING_DIR_HOST", True) + d.getVar("PYTHON_SITEPACKAGES_DIR", True))
    d.appendVar("EXTRA_OECONF", " --with-python-BUILD_SYS=" + d.getVar("BUILD_SYS", True))
    d.appendVar("EXTRA_OECONF", " --with-python-HOST_SYS=" + d.getVar("HOST_SYS", True))
    d.appendVar("EXTRA_OECONF", " --with-python-STAGING_INCDIR=" + d.getVar("STAGING_INCDIR", True))
    d.appendVar("EXTRA_OECONF", " --with-python-STAGING_LIBDIR=" + d.getVar("STAGING_LIBDIR", True))
    d.appendVar("EXTRA_OECONF", " --with-python-PYTHON_EXECUTABLE=" + d.getVar("PYTHON_EXECUTABLE", True))
    d.appendVar("EXTRA_OECONF", " --with-python-INSTALL_LIB=" + d.getVar("PYTHON_SITEPACKAGES_DIR", True))
    d.appendVar("EXTRA_OECONF", " --with-python-INSTALL_DATA=" + d.getVar("datadir", True))
    # Python bindings support only glib-2.0 mainloops.
    d.appendVar("EXTRA_OECONF", " --enable-glib")
}

python set_python_files () {
    # Include Python bindings to the image only when python is enabled.
    if not "python" in d.getVar("PACKAGECONFIG", True):
        return

    packageName = d.getVar("PN", True)

    d.appendVar("FILES_" + packageName, " " + d.getVar("PYTHON_SITEPACKAGES_DIR", True))
    d.appendVar("FILES_" + packageName + "-dbg", " " + d.getVar("PYTHON_SITEPACKAGES_DIR", True) + "/.debug")
}
