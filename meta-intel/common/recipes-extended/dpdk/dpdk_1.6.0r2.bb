include dpdk.inc


SRC_URI = "http://dpdk.org/browse/dpdk/snapshot/dpdk-${PV}.tar.gz;name=dpdk \
	   file://dpdk-1.6.0r2-examples-qos_sched-fix-makefile.patch \
	   file://dpdk-1.6.0r2-app-test-fix-build-switches-to-enable-cmdline-tests.patch \
	   file://dpdk-1.6.0r2-eal-fix-option-base-virtaddr.patch \
	   "


SRC_URI[dpdk.md5sum] = "f406d027320fc8e724bff20db5397cbb"
SRC_URI[dpdk.sha256sum] = "e72fdebcf8a899fc58e60c9b6493b7457576eece60b08dea6aee96c9087df4b2"

export EXAMPLES_BUILD_DIR = "build"

do_compile_append () {

	###################################################################
	### Compilation for examples
	### Skip dpdk_qat due to it has dependency with qat source code
	### Skip vhost due to it has dependency to fuse libraries
	### Skip vhost_xen due to it has dependency to xen libraries
	###################################################################
	for app in ${S}/examples/*
	do

		[ `basename ${app}` = "dpdk_qat" -o `basename ${app}` =  "vhost"  -o  `basename ${app}` = "vhost_xen" ] && continue;

		cd ${app}

		###############################################################
		# netmap_compat is putting the binary in a directory path
		# which is different from rest of the example apps, so this
		# special case is handled here to avoid installation failure
		# with dpdk-1.6.0
		###############################################################
		if [ `basename ${app}` == "netmap_compat" ]; then
			oe_runmake CROSS="${TARGET_PREFIX}" O="${app}/bridge/${EXAMPLES_BUILD_DIR}/"
		else
			oe_runmake CROSS="${TARGET_PREFIX}"
		fi
	done

}

