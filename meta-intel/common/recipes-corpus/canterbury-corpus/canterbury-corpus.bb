SUMMARY = "Intel Quick Assist Driver - Canterbury Corpus"
DESCRIPTION = "Set of files for testing losless compression algorithms \
		for Intel Crystal Forest BSP Quick Assist Technology Software Package"

HOMEPAGE = "http://corpus.canterbury.ac.nz"
SECTION = "misc"
LICENSE = "GPLv2"

LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"

inherit allarch

# The tarball doesn't extract a directory, so ask bitbake to make one
SRC_URI = "http://corpus.canterbury.ac.nz/resources/cantrbry.tar.gz;subdir=${BP}"
SRC_URI[md5sum] = "442e56cfffdf460d25b0b91650a55908"
SRC_URI[sha256sum] = "f140e8a5b73d3f53198555a63bfb827889394a42f20825df33c810c3d5e3f8fb"

FILES_${PN} = "/lib/firmware/*"

do_install () {
	# do_unpack creates this directory but we don't want to install it, so
	# delete it now.
	rm -rf ${S}/patches

	install -d ${D}${base_libdir}/firmware
	install -m 644 ${S}/* ${D}${base_libdir}/firmware
}

# The corpus contains Sparc binaries with unexpected symbol hash tables, so
# silence the QA tests that will otherwise emit errors.
INSANE_SKIP_${PN} = "arch ldflags"
