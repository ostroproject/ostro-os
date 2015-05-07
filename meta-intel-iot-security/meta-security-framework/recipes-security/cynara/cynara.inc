DESCRIPTION = "Cynara service with client libraries"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=86d3f3a95c324c9479bd8986968f4327;beginline=3"

DEPENDS = " \
dbus \
systemd \
zip \
"

# For testing:
# DEPENDS += "gmock"

inherit cmake

CXXFLAGS_append = " \
-DCYNARA_STATE_PATH=\\\\\"${localstatedir}/cynara/\\\\\" \
-DCYNARA_LIB_PATH=\\\\\"${prefix}/lib/cynara/\\\\\" \
-DCYNARA_TESTS_DIR=\\\\\"${prefix}/share/cynara/tests/\\\\\" \
-DCYNARA_CONFIGURATION_DIR=\\\\\"${sysconfdir}/cynara/\\\\\" \
-DCYNARA_VERSION=\\\\\"${PV}\\\\\" \
"

EXTRA_OECMAKE += " \
-DCMAKE_VERBOSE_MAKEFILE=ON \
-DBUILD_TESTS:BOOL=OFF \
-DCMAKE_BUILD_TYPE=RELEASE \
-DSYSTEMD_SYSTEM_UNITDIR=${systemd_unitdir}/system \
"

inherit useradd
USERADD_PACKAGES = "${PN}"
GROUPADD_PARAM_${PN} = "-r cynara"
USERADD_PARAM_${PN} = "\
--system --home ${localstatedir}/lib/empty \
--no-create-home --shell /bin/false \
--gid cynara cynara \
"

# Causes deadlock during booting, see workaround in postinst below.
#inherit systemd
#SYSTEMD_SERVICE_${PN} = "cynara.service"

do_install_append () {
   chmod a+rx ${D}/${sbindir}/cynara-db-migration

   install -d ${D}${sysconfdir}/cynara/
   install ${S}/conf/creds.conf ${D}/${sysconfdir}/cynara/creds.conf

   # No need to create empty directories...
   # install -d ${D}${localstatedir}/cynara/
   # install -d ${D}${prefix}/share/cynara/tests/empty_db
   # install -d ${D}${prefix}/lib/cynara/plugin/client
   # install -d ${D}${prefix}/lib/cynara/plugin/service

   # install db* ${D}${prefix}/share/cynara/tests/

   install -d ${D}${systemd_unitdir}/system/sockets.target.wants
   ln -s ../cynara.socket ${D}${systemd_unitdir}/system/sockets.target.wants/cynara.socket
   ln -s ../cynara-admin.socket ${D}${systemd_unitdir}/system/sockets.target.wants/cynara-admin.socket
   ln -s ../cynara-agent.socket ${D}${systemd_unitdir}/system/sockets.target.wants/cynara-agent.socket
}

FILES_${PN} += "${systemd_unitdir}/system"

# Cynara itself has no dependency on Smack. Only its installation
# is Smack-aware in the sense that it sets Smack labels. Do not
# depend on smack userspace unless we really need Smack labels.
#
# The Tizen .spec file calls cynara-db-migration in a %pre section.
# That only works when cynara-db-migration is packaged separately
# (overly complex) and does not seem necessary: perhaps there is a
# time window where cynara might already get activated before
# the postinst completes, but that is a general problem. It gets
# avoided entirely when calling this script while building the
# rootfs.
RDEPENDS_${PN}_append_smack = " smack-userspace"
DEPENDS_append_smack = " smack-userspace-native"
CHSMACK_smack = "chsmack"
CHSMACK = "true"
pkg_postinst_${PN} () {
   # Fail on error.
   set -e

   # It would be nice to run the code below while building an image,
   # but currently the calls to cynara-db-chsgen (a binary) in
   # cynara-db-migration (a script) prevent that. Rely instead
   # on OE's support for running failed postinst scripts at first boot.
   if [ x"$D" != "x" ]; then
      exit 1
   fi

   mkdir -p $D${sysconfdir}/cynara
   ${CHSMACK} -a System $D${sysconfdir}/cynara

   if [ -d $D${localstatedir}/cynara ] ; then
      # upgrade
      $D${sbindir}/cynara-db-migration upgrade -f 0.0.0 -t ${PV}
   else
      # install
      mkdir -p $D${localstatedir}/cynara
      ${CHSMACK} -a System $D${localstatedir}/cynara
      $D${sbindir}/cynara-db-migration install -t ${PV}
   fi

   # Workaround for systemd.bbclass issue: it would call
   # "systemctl start" without "--no-block", but because
   # the service is not ready to run at the time when
   # this scripts gets executed by run-postinsts.service,
   # booting deadlocks.
   systemctl enable cynara
   systemctl start --no-block cynara
}
