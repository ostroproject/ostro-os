SUMMARY = "Intel Processor Microcode Datafile for Linux"
HOMEPAGE = "http://www.intel.com/"
DESCRIPTION = "The microcode data file contains the latest microcode\
 definitions for all Intel processors. Intel releases microcode updates\
 to correct processor behavior as documented in the respective processor\
 specification updates. While the regular approach to getting this microcode\
 update is via a BIOS upgrade, Intel realizes that this can be an\
 administrative hassle. The Linux operating system and VMware ESX\
 products have a mechanism to update the microcode after booting.\
 For example, this file will be used by the operating system mechanism\
 if the file is placed in the /etc/firmware directory of the Linux system."

LICENSE = "Intel-Microcode-License"
LIC_FILES_CHKSUM = "file://microcode.dat;md5=dfedc580c52db32c762669b7652178b7"

SRC_URI = "http://downloadmirror.intel.com/24661/eng/microcode-${PV}.tgz"
SRC_URI[md5sum] = "639b7f2af0a822fe006a4fa2ddf8052f"
SRC_URI[sha256sum] = "23353b93bb421971496cea5e9f9d390ce0ed22580a8cc45ae7b3b322dcd8f6b3"

DEPENDS = "iucode-tool-native"
S = "${WORKDIR}"

COMPATIBLE_HOST = "(i.86|x86_64).*-linux"
PACKAGE_ARCH = "${MACHINE_ARCH}"

inherit deploy

# Use any of the iucode_tool parameters to filter specific microcodes from the data file
# For further information, check the iucode-tool's manpage : http://manned.org/iucode-tool
UCODE_FILTER_PARAMETERS ?= ""

do_compile() {
	mkdir -p ${WORKDIR}/ucode/kernel/x86/microcode
	${STAGING_DIR_NATIVE}${sbindir_native}/iucode_tool \
		${UCODE_FILTER_PARAMETERS} \
		--overwrite \
		--write-to=${WORKDIR}/microcode_${PV}.bin \
		${WORKDIR}/microcode.dat

	${STAGING_DIR_NATIVE}${sbindir_native}/iucode_tool \
		${UCODE_FILTER_PARAMETERS} \
		--overwrite \
		--write-earlyfw=${WORKDIR}/microcode_${PV}.cpio \
		${WORKDIR}/microcode.dat
}

do_install() {
	install -d ${D}${base_libdir}/firmware/intel-ucode/
	install ${WORKDIR}/microcode_${PV}.bin ${D}${base_libdir}/firmware/intel-ucode/
	cd ${D}${base_libdir}/firmware/intel-ucode/
	ln -sf microcode_${PV}.bin microcode.bin
}

do_deploy() {
	install -d ${DEPLOYDIR}
	install ${S}/microcode_${PV}.cpio ${DEPLOYDIR}/
	cd ${DEPLOYDIR}
	rm -f microcode.cpio
	ln -sf microcode_${PV}.cpio microcode.cpio
}

addtask deploy before do_build after do_compile

PACKAGES = "${PN}"

FILES_${PN} = "${base_libdir}"
