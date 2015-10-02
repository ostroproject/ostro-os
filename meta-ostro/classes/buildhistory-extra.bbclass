# Provides some extra logging into buildhistory of some of the inputs
# (buildhistory itself mostly concentrates on build output)
#
# Copyright (C) 2015 Intel Corporation
# Licensed under the MIT license

inherit buildhistory

BUILDHISTORY_EXTRA_PKGVARS ?= "PACKAGECONFIG EXTRA_OEMAKE EXTRA_OECONF EXTRA_OECMAKE EXTRA_OESCONS EXTRA_QMAKEVARS_PRE EXTRA_QMAKEVARS_POST OE_FEATURES SUMMARY DESCRIPTION HOMEPAGE LICENSE"

python buildhistory_emit_pkghistory_append() {
    import codecs

    relpath = os.path.dirname(d.getVar('TOPDIR', True))

    # List sources
    pkghistdir = d.getVar('BUILDHISTORY_DIR_PACKAGE', True)
    srcsfile = os.path.join(pkghistdir, "sources")
    with codecs.open(srcsfile, "w", encoding='utf8') as f:
        urls = (d.getVar('SRC_URI', True) or '').split()
        for url in urls:
            localpath = bb.fetch2.localpath(url, d)
            if os.path.isfile(localpath):
                sha256sum = bb.utils.sha256_file(localpath)
            else:
                sha256sum = 'N/A'
            if localpath.startswith(relpath):
                localpath = os.path.relpath(localpath, relpath)
            f.write('%s %s %s\n' % (url, localpath, sha256sum))

    # List metadata
    includes = d.getVar('BBINCLUDED', True).split()
    metafile = os.path.join(pkghistdir, "metadata")
    with codecs.open(metafile, "w", encoding='utf8') as f:
        for path in includes:
            if os.path.exists(path):
                sha256sum = bb.utils.sha256_file(path)
                if path.startswith(relpath):
                    path = os.path.relpath(path, relpath)
                f.write('%s %s\n' % (path, sha256sum))

    # List some extra var values
    latestfile = os.path.join(pkghistdir, "latest")
    vars = (d.getVar('BUILDHISTORY_EXTRA_PKGVARS', True) or '').split()
    if vars:
        with codecs.open(latestfile, "a", encoding='utf8') as f:
            for var in vars:
                value = oe.utils.squashspaces(d.getVar(var, True) or '')
                if value:
                    f.write('%s = %s\n' % (var, value))
}

python() {
    if bb.data.inherits_class('kernel', d):
        d.appendVarFlag('do_compile', 'prefuncs', ' buildhistory_extra_emit_kernelconfig')
        d.appendVarFlag('do_compile', 'vardepsexclude', ' buildhistory_extra_emit_kernelconfig')
}

python buildhistory_extra_emit_kernelconfig() {
    # Copy the final kernel config
    # Unlike the rest of buildhistory this will only get run when the kernel is actually built
    # (as opposed to being restored from the sstate cache); this is because do_shared_workdir
    # operates outside of sstate and that running is the only way you get the config other than
    # during the actual kernel build.
    import shutil
    pkghistdir = d.getVar('BUILDHISTORY_DIR_PACKAGE', True)
    shutil.copyfile(d.expand('${B}/.config'), os.path.join(pkghistdir, 'kconfig'))
}

buildhistory_get_image_installed_append() {
	# Create a file mapping installed packages to recipes
	printf "" > ${BUILDHISTORY_DIR_IMAGE}/installed-package-recipes.txt
	cat ${IMAGE_MANIFEST} | while read pkg pkgarch version
	do
		if [ -n "$pkg" ] ; then
			recipe=`oe-pkgdata-util -p ${PKGDATA_DIR} lookup-recipe $pkg`
			pkge=`oe-pkgdata-util -p ${PKGDATA_DIR} read-value PKGE $pkg`
			if [ "$pkge" != "" ] ; then
				pkge="$pkge-"
			fi
			pkgr=`oe-pkgdata-util -p ${PKGDATA_DIR} read-value PKGR $pkg`
			if [ "$pkgr" != "" ] ; then
				pkgr="-$pkgr"
			fi
			echo "$pkg $version $pkge$version$pkgr $recipe" >> ${BUILDHISTORY_DIR_IMAGE}/installed-package-recipes.txt
		fi
	done
}
