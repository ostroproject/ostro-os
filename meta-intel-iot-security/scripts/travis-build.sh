#! /bin/bash
#
# Combines setup, build and sstate-cache upload in a single script.
# Invoke with env variables as needed by the individual components
# and the build directory as parameter.
#
# sstate-cache can be reused between invocations, but should not
# be shared with unrelated builds, because it will get uploaded
# completely to S3.
#
# Example:
# rm -rf /work/build-dir;
# SSTATE_CACHE=/work/sstate-cache-meta-intel-iot-security \
# DOWNLOADS=/work/downloads \
# ... \
# /work/meta-intel-iot-security/scripts/travis-build.sh /work/build-dir

set -ex

SRC_DIR=${1-$(pwd)}
LAYERDIR=$(dirname $0)/..

$LAYERDIR/scripts/travis-setup.sh $SRC_DIR
. $SRC_DIR/init-travis-build-env
bitbake core-image-minimal
$LAYERDIR/scripts/sstate2s3.sh
