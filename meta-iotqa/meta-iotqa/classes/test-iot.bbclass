# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)


# testimage.bbclass enables testing of qemu images using python unittests.
# Most of the tests are commands run on target image over ssh.
# To use it add testimage to global inherit and call your target image with -c testimage
# You can try it out like this:
# - first build a qemu core-image-sato
# - add INHERIT += "test-iot" in local.conf
# - then bitbake core-image-sato -c test_iot. That will run a standard suite of tests.

# You can set (or append to) TEST_SUITES in local.conf to select the tests
# which you want to run for your target.
# The test names are the module names in meta/lib/oeqa/runtime.
# Each name in TEST_SUITES represents a required test for the image. (no skipping allowed)
# Appending "auto" means that it will try to run all tests that are suitable for the image (each test decides that on it's own).
# Note that order in TEST_SUITES is important (it's the order tests run) and it influences tests dependencies.
# A layer can add its own tests in lib/oeqa/runtime, provided it extends BBPATH as normal in its layer.conf.

# TEST_LOG_DIR contains a command ssh log and may contain infromation about what command is running, output and return codes and for qemu a boot log till login.
# Booting is handled by this class, and it's not a test in itself.
# TEST_QEMUBOOT_TIMEOUT can be used to set the maximum time in seconds the launch code will wait for the login prompt.

inherit testimage

#get layer dir
def get_layer_dir(d, layer):
    bbpath = d.getVar("BBPATH", True).split(':')
    for p in bbpath:
        if os.path.basename(p.rstrip('/')) == layer:
            break
    else:
        return ""
    return p

#get QA layer dir
def get_qa_layer(d):
    return get_layer_dir(d, "meta-iotqa")

#override the function in testimage.bbclass
def get_tests_list(d, type="runtime"):
    manif_name = d.getVar("TEST_SUITES_MANIFEST", True)
    if not manif_name:
        manif_name = "iottest.manifest" 
    testsuites = get_tclist(d, manif_name)
    bbpath = d.getVar("BBPATH", True).split(':')

    testslist = []
    for testname in testsuites:
        found = False
        for p in bbpath:
            testslist.append(testname)
            found = True
            break
        if not found:
            bb.fatal('Test %s specified in TEST_SUITES could not be found in lib/oeqa/runtime under BBPATH' % testname)
    return testslist
    
#get testcase list from specified layer
def get_tclist(d, fname):
    p = get_qa_layer(d)
    manif_path = os.path.join(p, 'conf', 'test', fname)
    if not os.path.exists(manif_path):
        return ""
    tcs = open(manif_path).readlines()
    return [ item.strip() for item in tcs ]

#bitbake task - run iot test suite
python do_test_iot() {

    testimage_main(d)
}

addtask test_iot
do_test_iot[depends] += "${TESTIMAGEDEPENDS}"
do_test_iot[lockfiles] += "${TESTIMAGELOCK}"

#overwrite copy src dir to dest
def recursive_overwrite(src, dest, ignore=['__init__.py']):
    import shutil
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        for f in files:
            fsrc = os.path.join(src, f)
            fdest = os.path.join(dest, f)
            if f in ignore and os.path.exists(fdest):
                continue
            recursive_overwrite(fsrc, fdest)
    else:
        shutil.copyfile(src, dest)
   
#export test asset
def export_testsuite(d, exportdir):
    import pkgutil
    import shutil

    oeqadir = pkgutil.get_loader("oeqa").filename
    shutil.copytree(oeqadir, os.path.join(exportdir, "oeqa"))
    
    qalayer = get_qa_layer(d)
    recursive_overwrite(src=os.path.join(qalayer, "lib"),
                        dest=os.path.join(exportdir))
    
    bb.plain("Exported tests to: %s" % exportdir)

#dump build data to external file
def dump_builddata(d, tdir):
    import json

    savedata = {}
    savedata["d"] = {"DEPLOY_DIR" : d.getVar("DEPLOY_DIR", True)}
    savedata["imagefeatures"] = d.getVar("IMAGE_FEATURES", True).split()
    savedata["distrofeatures"] = d.getVar("DISTRO_FEATURES", True).split()
    manifest = os.path.join(d.getVar("DEPLOY_DIR_IMAGE", True),
                              d.getVar("IMAGE_LINK_NAME", True) + ".manifest")
    try:
        with open(manifest) as f:
            pkgs = f.readlines()
            savedata["pkgmanifest"] = [ pkg.strip() for pkg in pkgs ]
    except IOError as e:
        bb.fatal("No package manifest file found: %s" % e)

    bdpath = os.path.join(tdir, "builddata.json")
    with open(bdpath, "w+") as f:
        json.dump(savedata, f, skipkeys=True, indent=4, sort_keys=True)

#copy test description file
def copy_testdesc(d, tdir):
    import shutil
    
    descfile = "testdesc.json"
    layerdir = get_qa_layer(d)
    srcpath = os.path.join(layerdir, "conf", "test", descfile)
    bb.plain("%s -- %s" % (layerdir, srcpath))
    shutil.copy2(srcpath, tdir)
    bb.plain("copy %s to: %s" % (descfile, tdir))

#package test suite as tarball
def pack_testsuite(d, tdir):
    import tarfile
    tar = tarfile.open("/tmp/iot-testsuite.tar.gz", "w:gz")
    tar.add(tdir, arcname=os.path.basename(tdir))
    tar.close()

#bitbake task - export iot test suite
python do_test_iot_export() {
    exportdir = d.getVar("TEST_EXPORT_DIR", True)
    if not exportdir:
        exportdir = "iottest"
        d.setVar("TEST_EXPORT_DIR", exportdir)
    bb.utils.remove(exportdir, recurse=True)
    bb.utils.mkdirhier(exportdir)
    export_testsuite(d, exportdir)
    dump_builddata(d, exportdir)
    copy_testdesc(d, exportdir)
    pack_testsuite(d, exportdir)
}

addtask test_iot_export
do_test_iot_export[depends] += "${TESTIMAGEDEPENDS}"
do_test_io_export[lockfiles] += "${TESTIMAGELOCK}"
