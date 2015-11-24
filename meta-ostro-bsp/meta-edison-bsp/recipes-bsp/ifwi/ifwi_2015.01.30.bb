DESCRIPTION = "ifwi binary blobs"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=ea398a763463b76b18da15f013c0c531"

inherit deploy

PR = "r1"

SRC_URI = "file://${PN}-${PV}.tar.bz2"

S="${WORKDIR}/ifwi"

PACKAGE_ARCH = "${MACHINE_ARCH}"

do_deploy () {

	# remove any prior deployments
	rm -rf ${DEPLOYDIR}/ifwi

	install -d ${DEPLOYDIR}/ifwi
	install ${S}/*.bin ${DEPLOYDIR}/ifwi

	# build ifwi file for using in DFU mode
	# Remove FUP footer (144 bytes) as it's not needed when we directly write to boot partitions
	for ifwi in ${DEPLOYDIR}/ifwi/*ifwi*.bin ;
	do
		dfu_ifwi_name="`basename $ifwi .bin`-dfu.bin"
		dd if=$ifwi of=${DEPLOYDIR}/ifwi/$dfu_ifwi_name bs=4194304 count=1
	done
}

addtask deploy before do_rootfs
