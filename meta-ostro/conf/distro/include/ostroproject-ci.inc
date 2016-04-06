#
# https://ostroproject.org/jenkins CI configuration:
# This file applied via conf/auto.conf for every build
# happening in Ostro Project CI
#

#
# Static section
# Items that are always present in any CI build:
#

# Generate summary statistics
INHERIT += "buildstats-summary"

# Enable CVE and other secutiry checks
INHERIT += "isafw"

# Enable extended buildhistory:
INHERIT += "buildhistory"
BUILDHISTORY_COMMIT = "1"
INHERIT += "buildhistory-extra"

# Test data generation:
INHERIT += "test-iot"
TEST_EXPORT_DIR = "iottest"
TEST_TARGET = "simpleremote"

# SDK defaults:
SDKMACHINE ?= "x86_64"

# Generate source mirror tarballs:
BB_GENERATE_MIRROR_TARBALLS = "1"

# Include the devel settings
require conf/distro/include/ostro-os-development.inc

# XXX Drop the VM hack after taking care also of the non UEFI devices
# (those using U-Boot: edison and beaglebone)
OSTRO_VM_IMAGE_TYPES = "dsk.xz dsk.zip dsk.vdi.zip"

#
# Automated build targets
# Those targets should be space separated list of items,
# which must contain only alphanumeric symbols,'-' and '_'.
# Any other symbols would be skipped in parser.
#
# Following targets would be used to perform default build task:
OSTROPROJECT_CI_BUILD_TARGETS="${DISTRO}-image ${DISTRO}-image-dev"
# Following targets would be executed with do_populate_sdk task
OSTROPROJECT_CI_SDK_TARGETS=""
# Following targets would be executed with do_populate_sdk_ext task
OSTROPROJECT_CI_ESDK_TARGETS="${DISTRO}-image"
# Following targets would be executed with do_test_iot_export task
OSTROPROJECT_CI_TEST_EXPORT_TARGETS="${DISTRO}-image"
# Execute automatic tests for following images with corresponding
# test suite and test files.
# Space separated list of tuples, each should in format:
# <image_name>,<testsuite_name>,<testfiles_name>,$MACHINE
OSTROPROJECT_CI_TEST_RUNS="${DISTRO}-image,iot-testsuite.tar.gz,iot-testfiles.${MACHINE}.tar.gz,${MACHINE}"

#
# Dymamic section.
# Values are applied dynamically based on runtime config or builder host
# parameters.
# Present here as reference only.
#

# Explicit machine declaration by build job:
# MACHINE = "$TARGET_MACHINE"

# Shared download directory between builders:
# DL_DIR = "/srv/bb-cache/ostro-os/sources"

# Limit CPU utilization, based on amount of slots/CPU cores
# on builder hosts:
# BB_NUMBER_PARSE_THREADS = "X"
# BB_NUMBER_THREADS = "X"
# PARALLEL_MAKE = "-j X"

# Local optimizations on SSTATE directories, shared between builder hosts:
# SSTATE_MIRRORS ?= "file://.* http://$IP/bb-cache/ostro-os/sstate/PATH"
# SSTATE_DIR ?= "/var/tmp/sstate-$slot"

# Local directory, where builder puts local copy of buildhistory
# BUILDHISTORY_DIR ?="$WORKSPACE/buildhistory"

# PRserv host dynamically allocated by master:
# PRSERV_HOST = "$IP:$PORT"

# Enabled for master release builds:
# INHERIT += "archiver"
# ARCHIVER_MODE[src] = "original"
# ARCHIVER_MODE[diff] = "1"
# ARCHIVER_MODE[recipe] = "1"
