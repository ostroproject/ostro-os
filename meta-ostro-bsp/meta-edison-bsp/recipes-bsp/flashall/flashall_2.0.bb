DESCRIPTION = "flashall scripts and supporting files"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=ea398a763463b76b18da15f013c0c531"

inherit deploy

PR = "r5"

SRC_URI = " \
	   file://LICENSE \
	   file://filter-dfu-out.js \
	   file://flashall.bat \
	   file://flashall.sh \
	   file://pft-config-edison.xml \
	   file://FlashEdison.json \
	   file://helper/helper.html \
	   file://helper/images/Edison-arduino.png \
	   file://helper/images/Edison-arduino-blink-led.png \
	   file://helper/images/Edison-breakout-board.png \
	  "

S="${WORKDIR}"

PACKAGE_ARCH = "${MACHINE_ARCH}"

do_deploy () {

	# remove any prior deployments
	rm -rf ${DEPLOYDIR}/flashall

	install -d 			${DEPLOYDIR}/flashall
	install ${S}/filter-dfu-out.js	${DEPLOYDIR}/flashall
	install ${S}/flashall.*		${DEPLOYDIR}/flashall
	install ${S}/pft-config-edison.xml ${DEPLOYDIR}/flashall
	install ${S}/FlashEdison.json	${DEPLOYDIR}/flashall

	install -d 			${DEPLOYDIR}/flashall/helper
	install ${S}/helper/helper.html	${DEPLOYDIR}/flashall/helper

	install -d 			${DEPLOYDIR}/flashall/helper/images
	install ${S}/helper/images/*.png  ${DEPLOYDIR}/flashall/helper/images
}

addtask deploy before do_rootfs
