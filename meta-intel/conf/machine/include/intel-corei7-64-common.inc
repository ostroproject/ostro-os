#
# Common configuration for all MACHINES of the intel-corei7-64 type
#

DEFAULTTUNE ?= "corei7-64"
require intel-common-pkgarch.inc
require conf/machine/include/tune-corei7.inc
require conf/machine/include/x86-base.inc
