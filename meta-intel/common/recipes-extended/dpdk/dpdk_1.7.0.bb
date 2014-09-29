include dpdk.inc

SRC_URI = "http://dpdk.org/browse/dpdk/snapshot/dpdk-${PV}.tar.gz;name=dpdk \
	   file://dpdk-1.7.0-examples-Add-config-variables-to-enable-disable-dpdk.patch \
	   file://dpdk-1.7.0-examples-pipeline-build-with-all-examples.patch \
	   file://dpdk-1.7.0-ring-remove-extra-devices-creation-with-vdev-option.patch \
	   file://dpdk-1.7.0-ring-simplify-unit-tests.patch \
	   "

SRC_URI[dpdk.md5sum] = "07907d7b1a64888a459a971c45818038"
SRC_URI[dpdk.sha256sum] = "aafc290260b5002d248ab8f8c8ffa76454d4b1382aa3c82ae2700ecce481397a"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"

# dpdk example apps dpdk_qat and vhost have dependancy on fuse and qat.
# fuse is in meta-filesystems and qat is not yet upstreamed.
# So adding mechanism to explicitly disable the use of fuse and qat.
# To enable, uncomment the below line or include in .bbappend.
# PACKAGECONFIG ?= " dpdk_qat vhost "

PACKAGECONFIG[dpdk_qat] = ",,qat"
PACKAGECONFIG[vhost] = ",,fuse"

do_compile_append () {

	cd ${S}/examples/

	# Disable the compilation of example apps dpdk_qat and vhost if they are
	# not included in the PACKAGECONFIG
	export CONFIG_EXAMPLE_DPDK_QAT=${@base_contains('PACKAGECONFIG', 'dpdk_qat', 'y', 'n', d)}
	export CONFIG_EXAMPLE_DPDK_VHOST="${@base_contains('PACKAGECONFIG', 'vhost', 'y', 'n', d)}"

	###############################################################
	# In order to make use of dpdk.inc for example app installation
	# without failure, override the default build directory
	###############################################################
	oe_runmake CROSS="${TARGET_PREFIX}" O="${S}/examples/$@/"
}



