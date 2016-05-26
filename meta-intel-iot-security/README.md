# meta-intel-iot-security

A collection of loosely related OpenEmbedded layers providing several
security technologies.

In general, the additional features must be explicitly enabled.
Merely adding the layers has little influence on the resulting
packages and images, therefore it is possible to build a distro where
security is an optional feature.

meta-security-framework is a general-purpose utility layer. Both
meta-security-smack and meta-integrity depend on
it. meta-security-smack and meta-integrity do not depend on each
other.

See the individual layer README's for further instructions.


# Testing

Build and unit testing under [TravisCI][] is configured against
different OpenEmbedded core branches in .travis.yml. Currently master,
jethro, and fido are covered.

Two different [TravisCI environments][] are used:

* The traditional containers support test jobs of up to 2 hours, but
  do not offer root rights, therefore testing under qemu (which needs a
  configured TAP device and thus root access) is not possible. Using that
  environment is configured in a special "travis-compilation" branch.
* The fully virtualized Trusty environment grants root rights and thus can
  run tests, but only allows jobs of up to 50 minutes, which is not
  enough to compile from scratch. This configuration is the default used
  by most branches.

Both environments have fairly limited disk space, therefore the
"rm_work.bbclass" is used to reduce disk usage during building. Even
that is often not good enough to compile in one go without running out
of disk space.

To overcome these limitations, sstate is stored persistently, shared
between all jobs and always updated after compilation, even for jobs
which had to be terminate prematurely. That way, restarting a job that
failed due to a timeout or full disk will make some progress and
eventually succeed. Restarting the "travis-compilation" jobs is useful
for this because those jobs make more progress per run.

Bitbake itself gets started under the travis-cmd-wrapper.py helper
script which logs system state (disk usage, CPU utilization, running
processes) at regular time intervals, which is useful for monitoring a
run and also avoids getting killed by TravisCI when there is no normal
output for more than 10 minutes (as it can happen when bitbake is
working on a single complex task, like compiling the Linux kernel).

In addition, the script ensures that bitbake generates output for
non-interactive usage terminates early enough to leave time for sstate
uploading.

An [Amazon S3][] bucket is used to store the sstate. Pull requests get
access to existing sstate, but are not allowed to modify it. TravisCI
testing is free for open source projects like this one, but S3 is
not. The free [TravisCI caching][] was evaluated, but turned out to be
not flexible enough. Uploading is done with s3cmd because that offers
more control than the TravisCI deploy addon. It also only has Python
as dependency, which allows freeing up some disk space by deleting the
Ruby runtime environment from the home directory.

To re-create a similar setup:

* in the [Amazon IAM console][] create a new user 'travisci' that will
  get access to the bucket, remember its access key and secret
* log into the [Amazon S3 console][]
* create a new bucket; the default for the TravisCI deploy addon seems
  to be us-east-1, so perhaps that works best
* edit the bucket policy such that the travisci user can upload content and everyone else gets read access:

        {
        	"Version": "2012-10-17",
        	"Id": "Policy1234",
        	"Statement": [
        		{
        			"Sid": "AllowUpload",
        			"Effect": "Allow",
        			"Principal": {
        				"AWS": "arn:aws:iam::youraccount:user/travisci"
        			},
        			"Action": "s3:*",
        			"Resource": "arn:aws:s3:::yourbucket/*"
        		},
        		{
        			"Sid": "AllowPublicRead",
        			"Effect": "Allow",
        			"Principal": "*",
        			"Action": "s3:GetObject",
        			"Resource": "arn:aws:s3:::youraccount/*"
        		}
        	]
          }
* enable static web hosting with default index.html and error.html
* configure your TravisCI project with the following environment variables:
  * ``AWS_ACCESS_KEY``: access key for the travisci user, not displayed
  * ``AWS_SECRET_KEY``: access secret for the travisci user, not displayed
  * ``AWS_BUCKET``: your bucket name, displayed
  * ``AWS_BUCKET_REGION``: the region where the bucket was created

``AWS_ACCESS_KEY`` and ``AWS_SECRET_KEY`` are not exported to pull requests,
so there is no risk that they get leaked to malicious commands in a
modified .travis.yml and when testing a pull request, uploading is
disabled in the current .travis.yml.

The static web hosting is used to configure a HTTP sstate cache server
based on the ``AWS_BUCKET`` and ``AWS_BUCKET_REGION``, if
available. This works because access permissions are set such that
Bitbake and wget do not need credentials to access the sstate.

[TravisCI]: https://travis-ci.org/
[TravisCI environments]: https://docs.travis-ci.com/user/ci-environment/
[TravisCI caching]: https://docs.travis-ci.com/user/caching
[Amazon S3]: https://aws.amazon.com/s3/
[Amazon IAM console]: https://console.aws.amazon.com/iam
[Amazon S3 console]: https://console.aws.amazon.com/s3


# Copying

Unless noted otherwise, files are provided under the MIT license (see
COPYING.MIT).
