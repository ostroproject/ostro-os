DEPLOY_FILES_DIR = "${WORKDIR}/deploy-files-${PN}"
SSTATETASKS += "do_deploy_files"
do_deploy_files[sstate-inputdirs] = "${DEPLOY_FILES_DIR}"
do_deploy_files[sstate-outputdirs] = "${DEPLOY_DIR}/files/"

python do_deploy_files_setscene () {
    sstate_setscene(d)
}
addtask do_deploy_files_setscene
do_deploy_files[dirs] = "${DEPLOY_FILES_DIR} ${B}"

# Use like this:
# DEPLOY_FILES = "abc xyz"
# DEPLOY_FILES_FROM[abc] = "file-ab dir-c"
# DEPLOY_FILES_TO[abc] = "directory-for-abc"
# DEPLOY_FILES_FROM[xyz] = "file-xyz"
# DEPLOY_FILES_TO[xyz] = "directory-for-xyz"
#
# The destination directory will be created inside
# ${DEPLOYDIR}. The source files and directories
# will be copied such that their name and (for
# directories) the directory tree below it will
# be preserved. Shell wildcards are supported.
#
# The default DEPLOY_FILES copies files for the native host
# and the target into two different directories. Use that as follows:
# DEPLOY_FILES_FROM_native = "native-file"
# DEPLOY_FILES_FROM_target = "target-file"

DEPLOY_FILES ?= "native target"
DEPLOY_FILES_FROM[native] ?= ""
DEPLOY_FILES_TO[native] = "native/${BUILD_ARCH}"
DEPLOY_FILES_FROM[target] ?= ""
DEPLOY_FILES_TO[target] = "target/${MACHINE}"

# We have to use a Python function to access variable flags. Because
# bitbake then does not know about the dependency on these variables,
# we need to explicitly declare that. DEPLOYDIR may change without
# invalidating the sstate, therefore it is not listed.
do_deploy_files[vardeps] = "DEPLOY_FILES DEPLOY_FILES_FROM DEPLOY_FILES_TO"
python do_deploy_files () {
    import glob
    import os
    import shutil

    for file in (d.getVar('DEPLOY_FILES', True) or '').split():
        bb.note('file: %s' % file)
        from_pattern = d.getVarFlag('DEPLOY_FILES_FROM', file, True)
        bb.note('from: %s' % from_pattern)
        if from_pattern:
            to = os.path.join(d.getVar('DEPLOY_FILES_DIR', True), d.getVarFlag('DEPLOY_FILES_TO', file, True))
            bb.note('to: %s' % to)
            if not os.path.isdir(to):
                os.makedirs(to)
            for from_path in from_pattern.split():
                for src in (glob.glob(from_path) or [from_path]):
                    bb.note('Deploying %s to %s' % (src, to))
                    if os.path.isdir(src):
                        src_dirname = shutil._basename(src)
                        to = os.path.join(to, src_dirname)
                        if os.path.exists(to):
                            bb.utils.remove(to, True)
                        shutil.copytree(src, to)
                    else:
                        shutil.copy(src, to)
}

addtask deploy_files before do_build after do_compile
