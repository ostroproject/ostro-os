#!/bin/sh
#
# Author:       Patrick Ohly <patrick.ohly@intel.com>
# Copyright:    Copyright (C) 2015 Intel Corporation
#
# This file is licensed under the MIT license, see COPYING.MIT in
# this source distribution for the terms.

# Copies new files in $HOME/sstate-cache to the S3 bucket, if configured
# via environment variables.
#
# Embedding these commands into .travis.yml itself turned out to be
# close to impossible. See https://github.com/travis-ci/travis-ci/issues/497

set -e

if [ "$AWS_ACCESS_KEY" ] && [ "$AWS_SECRET_KEY" ] && [ "$AWS_BUCKET" ]; then
    # State of sstate before cleaning. "tree" would give nicer output, but is
    # not available.
    if [ "$DEBUG_OUTPUT" ]; then echo "current sstate-cache:"; find $HOME/sstate-cache \! -type d; FIND_DEBUG_PRINT=-print; echo "removing from sstate-cache:"; fi
    # When we have successfully retrieved sstate from our HTTP server,
    # we end up with files in the top level directory and symlinks to
    # that in the real sstate location. We need to avoid deploying both
    # of these.
    find $HOME/sstate-cache -type l -delete $FIND_DEBUG_PRINT
    find $HOME/sstate-cache -maxdepth 1 -type f -delete $FIND_DEBUG_PRINT
    # In addition, we also get .done files next to the symlinks (or real
    # files?).
    find $HOME/sstate-cache -name *.done | while read file; do base=$(echo $file | sed -e 's/.done$//'); rm -f $base $file; if [ "$DEBUG_OUTPUT" ]; then echo $base; echo $file; fi; done
    # Finally, do_rm_work[_all.tgz.siginfo get created, but never downloaded via HTTP,
    # so there is no need to upload them.
    find $HOME/sstate-cache \( -name *_rm_work.tgz.siginfo -o -name *_rm_work_all.tgz.siginfo \) -delete $FIND_DEBUG_PRINT
    # Result of cleaning.
    if [ "$DEBUG_OUTPUT" ]; then echo "cleaned sstate-cache:"; find $HOME/sstate-cache  \! -type d ; fi
    # Now sync. s3cmd is more flexible than the TravisCI "deploy" or "artifacts" add-ons:
    # - we know that files are immutable, so we can simply skip existing ones
    #   (when running builds in parallel, more than one might end up creating the same file).
    # - we can specify the storage class (reduced redundancy is fine and cheaper).
    # - we can choose when to run it and whether it overlaps with testing.
    # - we can throw away the .rvm directory and thus get more free space.
    # On the other hand, "deploy" could also be configured to copy to other storages.
    cat >$HOME/.s3cfg <<EOF
[default]
access_key = $AWS_ACCESS_KEY
secret_key = $AWS_SECRET_KEY
use_https = False
EOF
    # Not supported by all versions of s3cmd, need to check.
    if s3cmd --help | grep -q -e --storage-class; then
        S3_STORAGE_CLASS=--storage-class=REDUCED_REDUNDANCY
    fi
    # Careful with progress: it can make the log too large, causing
    # TravisCI to abort the job ("The log length has exceeded the
    # limit of 4 Megabytes (this usually means that test suite is
    # raising the same exception over and over).").
    s3cmd --no-progress --skip-existing $S3_STORAGE_CLASS sync $HOME/sstate-cache/ s3://travis-meta-intel-iot-security/
else
    echo "Not updating sstate in S3 bucket (no credentials or bucket)."
fi
