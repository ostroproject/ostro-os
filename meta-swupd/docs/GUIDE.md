What is swupd?
==============

The [SoftWare UPDater](https://clearlinux.org/features/software-update) — swupd — from [Clear Linux](https://clearlinux.org/) provides a new way of adding functionality to and updating a Linux-based OS.

swupd uses binary-delta technology to efficiently update only the files that have changed between OS updates. This means that updates are small, resulting in fast downloads, and fast to apply.

Bundles allow a system adminstrator to easily add or remove a complete set of functionality to the OS image, rather than worrying about individual packages.

What is this meta-swupd?
===================

[meta-swupd](http://git.yoctoproject.org/cgit/cgit.cgi/meta-swupd) provides a metadata layer to aide Open Embedded and Yocto Project users in developing Linux-based operating systems built around swupd.

meta-swupd can be used to implement both of the key features of swupd; efficient binary-delta based updates and bundle-based feature management.

meta-swupd can easily be used to only deploy efficient update streams *or* to deploy a bundle-based OS with efficient updates.

Swupd Concepts
==============

Single, OS-wide, version number
-------------------------------

swupd based operating systems atomically upgrade the entire OS from one version to the next, rather than upgrading at a more granular, package-based, level.
This means that the entire contents of the OS can be determined from a single version number.

How do I use it?
================

The following steps are required to develop an OS that uses a swupd update stream:
* add the meta-swupd layer to bblayers.conf
* designate an image recipe as the base OS image (os-core, in swupd parlance) and `inherit swupd-image` in that recipe
* ensure the `OS_VERSION` variable is assigned an integer value which matches the `VERSION_ID` value in the *os-release* recipe and that this number is increased before each build which should generate swupd update artefacts

In addition, to make use of swupd's bundle functionality, you will need to:
* assign a list of bundle names to `SWUPD_BUNDLES` i.e:

    ```SWUPD_BUNDLES = "feature_one feature_two"```

* for each named bundle, assign a list of packages for which their content should be included in the bundle to a varflag of `BUNDLE_CONTENTS` which matches the bundle name i.e:

    ```BUNDLE_CONTENTS[feature_one] = "package_one package_three package_six"```


What might go wrong? (a.k.a. known issues)
==========================================

* refuses to overwrite generated data — because the act of generating swupd updates is time-consuming meta-swupd, by design, refuses to overwrite an existing update stream warning that the `OS_VERSION` number should be incremented.
* hardlinks and extended attributes — there's a bug in [pseudo](https://www.yoctoproject.org/tools-resources/projects/pseudo) which results in the extended attributes for a hardlink being incorrectly associated with the directory entry, rather than the inode. See [bug #9317](https://bugzilla.yoctoproject.org/show_bug.cgi?id=9317)
* alternatives — when a bundle adds a package which pulls in an alternative with a higher priority than the one in the base image (i.e. coreutils takes precedence over busybox) we end up with a situation where the base image contains the symlink to the higher priority binary, but not the binaries themselves. See [bug #9320](https://bugzilla.yoctoproject.org/show_bug.cgi?id=9320)
* potentially copies a lot of duplicate files — when copying bundle contents around it's very likely that the same file will exist in the swupd working directory multiple times. We may be able to make this less disk space intensive by using a utility like hardlink to deduplicate identical files. See [bug #9189](https://bugzilla.yoctoproject.org/show_bug.cgi?id=9189)
* copies then deletes, rather than just copying — the current/initial implementation copies the entire mega-image rootfs for each bundle chroot-like directory and then prunes away unwanted files. It will be much more efficient to only copy the files which are required in the first instance. See [bug #9325](https://bugzilla.yoctoproject.org/show_bug.cgi?id=9325)

Control Variables
=================

Several variables can be set to tune the way swupd-image works:
* `SWUPD_GENERATE` — if set to *0* i.e. `SWUPD_GENERATE = "0"` swupd update artefact processing will be skipped but all tasks of the `swupd-image` class will be executed. This is useful both for debugging the `swupd-image` class and in a scenario where it might be desirable to generate the chroot-like bundle directories without performing an processing with swupd.
* `SWUPD_DELTAPACKS` — if set to *0* i.e. `SWUPD_DELTAPACKS="0"` swupd delta-packs will not be generated.
* `SWUPD_N_DELTAPACKS` — the number of previous releases against which to generate delta-packs, defaults to 2.
* `SWUPD_VERSION_STEP` — Amount the OS_VERSION should be increased by for each release. Used by the delta pack looping to generate delta packs going back up to SWUPD_N_DELTAPACK releases. This could be replaced by a more elegant algorithm, see [bug #9322](https://bugzilla.yoctoproject.org/show_bug.cgi?id=9322).

Implementation Overview
=======================
An image that inherits this class will automatically have bundle 'chroots' created which contain the filesystem contents of the specified bundles.
The mechanism to achieve this is that several virtual image recipes are created, one for each defined bundle plus a 'mega' image recipe.
The 'mega' image contains the base image plus all of the bundles (and their contents), whilst bundle images contain only the base image plus the contents of a single bundle.

We build the mega image first, then the base image (the one which inherits the `swupd-image` class) and finally all of the bundle images  . Each non-mega image has a manifest generated that lists all of the file contents of the image.

Each bundle 'chroot'-like directory and the rootfs of the base image are all populated from the contents of the mega image's rootfs. The reason for this is to ensure that all files which are modified during some kind of post-processing step, i.e. passwd and groups updated during postinsts, are fully populated.
This may not be an ideal compromise and requires further thought (i.e. see the known issue about alternatives above).

Once the images and their manifests have been created each bundle image manifest is compared to the base image manifest in order to generate a delta list of files in the bundle image which don't exist in the base image.
Files in this list are then preserved in the bundle directory for processing by swupd-server in order to generate update artefacts.
