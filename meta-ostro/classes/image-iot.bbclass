# This class implements image creation for the ostro target.
# The image is GPT based.
# To boot, it uses a combo file, containing kernel, initramfs and
# command line, presented to the BIOS as UEFI application, by prepending
# it with the efi stub obtained from gummiboot.
# The layout of the image is described in a separate, customizable json file.

# A layout files is built accordingly to the following example:
#   {
#       "gpt_initial_offset_mb": 3,          <-  Space allocated for the 1st GPT
#       "gpt_tail_padding_mb": 3,            <-  Space allocated for the 2nd GPT
#       "primary_uefi_boot_partition": {     <-- Name of the entry in the dictionary
#           "name": "primary_uefi",          <-- Name of the partition in the GPT (MAX 16 ch)
#           "uuid": 0,                       <-- UUID of the partition, 0 means random
#           "size_mb": 30,                   <-- Size of the partition in MB
#           "source": "${S}/hdd/boot",       <-- Directory containing the root for the partition
#           "filesystem": "vfat",            <-- Filesystem for the partition
#           "type": "ef00"                   <-- Type of the partition, to be used in the GPT
#           "preserve": "yes"                <-- Keep the artefact yes/no
#       },
#       [...]                                Iterate partitions as needed
#   }
#
#   The main rootfs partition is a special case and must be named "rootfs".
#   This is required to identify it and pass its Partition UUID to the kernel, for booting.


EXTRA_IMAGEDEPENDS += " \
                       parted-native \
                       gptfdisk-native \
                      "

# This expects the presence of an initramfs, defined by setting INITRD_IMAGE.
INITRD ?= "${DEPLOY_DIR_IMAGE}/${INITRD_IMAGE}-${MACHINE}.cpio.gz"
do_image[depends] += " \
                      ${INITRD_IMAGE}:do_rootfs \
                      ${PN}:do_rootfs \
                     "
# XXX If this class is used for non x86 devices, the microcode part needs to
# be made specific to x86 devices.
do_image[depends] += " \
                      gummiboot:do_deploy \
                      virtual/kernel:do_deploy \
                      initramfs-framework:do_populate_sysroot \
                      intel-microcode:do_deploy \
                      gptfdisk-native:do_populate_sysroot \
                      parted-native:do_populate_sysroot \
                      mtools-native:do_populate_sysroot \
                      dosfstools-native:do_populate_sysroot \
                     "
PACKAGES = " "
EXCLUDE_FROM_WORLD = "1"


# XXX This might get dropped later. It depends on the implementation for Edison.
EFI = "1"

# The image does without traditional bootloader.
# In its place, instead, it uses a single UEFI executable binary, which is
# composed by:
#   - an UEFI stub
#     The linux kernel can generate a UEFI stub, however the one from gummiboot can fetch
#     the command line from a separate section of the EFI application, avoiding the need to
#     rebuild the kernel.
#   - the kernel
#   - the initramfs
#   There is a catch: all of these binary components must have the same word size as the BIOS:
#   either 32 or 64 bit.
build_uefi_executable() {
	dest="${S}/hdd/boot"
        EFIDIR="/EFI/BOOT"
	install -d $dest/${EFIDIR}

	# initrd is composed by the concatenation of multiple compressed cpio archives
        # (initramfs, microcode, etc.)
	if [ -n "${INITRD}" ]; then
		rm -f $dest/${EFIDIR}/initrd
		for fs in ${INITRD}
		do
			if [ -s "${fs}" ]; then
				cat ${fs} >> $dest/${EFIDIR}/initrd
			else
				bbfatal "${fs} is invalid. initrd image creation failed."
			fi
		done
	fi
        echo "${IMAGE_NAME}" > "${dest}/${EFIDIR}/os-release.txt"
        echo "${APPEND} root=PARTUUID=${ROOTFS_PARTUUID} rootfstype=${ROOTFS_TYPE}" > "${dest}/${EFIDIR}/cmdline.txt"
        # XXX Can this be done better?
        if (echo "${MACHINE}" |grep -q "64"); then
          EXECUTABLE=bootx64.efi
        else
          EXECUTABLE=bootia32.efi
        fi
        objcopy \
          --add-section .osrel="${dest}/${EFIDIR}/os-release.txt" --change-section-vma .osrel=0x20000 \
          --add-section .cmdline="${dest}/${EFIDIR}/cmdline.txt" --change-section-vma .cmdline=0x30000 \
          --add-section .linux="${DEPLOY_DIR_IMAGE}/bzImage" --change-section-vma .linux=0x40000 \
          --add-section .initrd="${dest}/${EFIDIR}/initrd" --change-section-vma .initrd=0x3000000 \
          "${DEPLOY_DIR_IMAGE}"/linux*.efi.stub $dest/${EFIDIR}/${EXECUTABLE}
        chmod 0644 $dest/${EFIDIR}/${EXECUTABLE}
        # If needed, leave a copy of each binary component into the EFI partition, to help debugging.
        # To do it, uncomment the 2 following lines.
        # However this might also require adjusting the space allocated for the EFI partition(s)
        # cp "${DEPLOY_DIR_IMAGE}/bzImage" "${dest}/${EFIDIR}/bzImage"
        # cp "${DEPLOY_DIR_IMAGE}"/linux*.efi.stub "${dest}/${EFIDIR}"
}

# Method for faking the creation of a partition, by reusing an existing one.
# No real use at the moment.
populate_rawcopy() {
    cp ${PARTITION_SOURCE} ${FULL_PARTITION_FILE_NAME}
}


# Method for creating and populating a FAT partition out of a root
# directory. Useful mostly for UEFI partitions.
populate_vfat() {
    # vfat doesn't care about ownership/attributes, so no need to
    # care about pseudo.
    mkdosfs ${FULL_PARTITION_FILE_NAME}
    mcopy -i ${FULL_PARTITION_FILE_NAME} -s  ${PARTITION_SOURCE}/* ::/
}

# Method for creating and populating an ext4 partition out of a root
# directory. Useful for typical partitions.
# Preservation of user ownership and file attributes is provided through pseudo.
# As long as the rootfs was created using it.
populate_ext4() {
    # To preserve correct ownership and attributes, the copying of files
    # must happen through pseudo.

    # Prepare the environment for running "pseudo".
    tmp1=`echo ${FAKEROOTENV} |sed 's/ /; export /g' |sed 's/^/export /' |sed 's/$/;/'`

    # Populate the filesystem preserving attributes and ownership of files.
    tmp2="pseudo mkfs.ext4 -F ${FULL_PARTITION_FILE_NAME} "
    if [ -z "${PARTITION_SOURCE}" ]; then
        tmp3=""
    else
        tmp3=" -d ${PARTITION_SOURCE}"
    fi
    eval $tmp1$tmp2$tmp3
}

# Generic part of the partition-creation fare.
build_partition() {
    if [ -f  "${FULL_PARTITION_FILE_NAME}" ]; then
        rm -f ${FULL_PARTITION_FILE_NAME}
    fi
    truncate -s ${PARTITION_SIZE_MB}M ${FULL_PARTITION_FILE_NAME}
    populate_${PARTITION_FILESYSTEM}
    chmod 644 ${FULL_PARTITION_FILE_NAME}
    # Create a symlink to the partition only if it's meant to be kept.
    if [ "${PARTITION_PRESERVE}" == "1" ]; then
        if [ -h "${FULL_PARTITION_FILE_NAME_LINK}" ]; then
            rm -f ${FULL_PARTITION_FILE_NAME_LINK}
        fi
        ln -s ${PARTITION_FILE_NAME} ${FULL_PARTITION_FILE_NAME_LINK}
    fi
}

# First step in creating the full disk image.
# Loop file + GPT partition.
build_empty_image_file() {
    truncate -s ${FULL_IMAGE_SIZE_MB}M ${FULL_IMAGE_FILE_NAME}
    sgdisk -o ${FULL_IMAGE_FILE_NAME}
    if [ -h  "${FULL_IMAGE_FILE_NAME_LINK}" ]; then
        rm -f ${FULL_IMAGE_FILE_NAME_LINK}
    fi
    ln -s ${IMAGE_FILE_NAME} ${FULL_IMAGE_FILE_NAME_LINK}
}

# Method for poplating the GPT with entries, one for each partition desired.
# This first writes the entry into to the GPT, then injects the partition loop file
# at the appropriate address.
process_partition() {
    sgdisk -c=0:${PARTITION_NAME} -n=0:${PARTITION_START_MB}M:+${PARTITION_SIZE_MB}M -t=0:${PARTITION_TYPE} -u=0:${PARTITION_UUID} ${FULL_IMAGE_FILE_NAME}
    dd if=${FULL_PARTITION_FILE_NAME} of=${FULL_IMAGE_FILE_NAME} bs=1M conv=notrunc seek=${PARTITION_START_MB}
    # Delete the partition loop file, if so requested.
    if [ "${PARTITION_PRESERVE}" == "0" ]; then
        rm -f "${FULL_PARTITION_FILE_NAME}"
    fi
}

# The json file describing the disk layout is created by the main python code
# however its name contains the build-id, making it less than friendly
# to handle for post-processing tools.
# So let's create a symlink with a more stable name.
create_symlink_to_disk_layout() {
    if [ -h  "${FULL_DISK_LAYOUT_FILE_NAME_LINK}" ]; then
        rm -f "${FULL_DISK_LAYOUT_FILE_NAME_LINK}"
    fi
    ln -s "${DISK_LAYOUT_FILE_NAME}" "${FULL_DISK_LAYOUT_FILE_NAME_LINK}"
}


# This should not be necessary, but it seems that the rootfs creation
# doesn't generate a symlink to the manifest, unless some type of image
# is created out of the rootfs.
# Worse, there is a confusion between the manifest of the root partition and
# the manifest of the whole image, which might have more partitions and certainly
# has also an initrd.
# But, for now, let's just replicate what the previous recipe does.
manifest_hack() {
    if [ -h  "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}.rootfs.manifest" ]; then
        rm -f "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}.rootfs.manifest"
    fi
    ln -s "${IMAGE_NAME}.rootfs.manifest" "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}.rootfs.manifest"
    FULL_IMAGE_MANIFEST_FILE_NAME_LINK="${DEPLOY_DIR_IMAGE}/"`echo "${IMAGE_NAME_LINK}.manifest"`
    if [ -h  "${FULL_IMAGE_MANIFEST_FILE_NAME_LINK}" ]; then
        rm -f "${FULL_IMAGE_MANIFEST_FILE_NAME_LINK}"
    fi
    ln -s "${IMAGE_NAME}.rootfs.manifest" "${FULL_IMAGE_MANIFEST_FILE_NAME_LINK}"
}


# Build .vdi images for use with VirtualBox
# Because of the .vdi format, the output file can be smaller than the original,
# since it compresses unused portions of the image.
vdi_from_raw() {
    qemu-img convert -O vdi ${FULL_IMAGE_FILE_NAME} ${FULL_VDI_IMAGE_FILE_NAME}
    if [ -h "${FULL_VDI_IMAGE_FILE_NAME_LINK}" ]; then
      rm -f ${FULL_VDI_IMAGE_FILE_NAME_LINK}
    fi
    ln -s ${VDI_IMAGE_FILE_NAME} ${FULL_VDI_IMAGE_FILE_NAME_LINK}
}


# Entry point for generating the disk image.
python do_image() {
    import random, string, json, uuid
    # Helper function for converting the json data to utf8.
    # Bitbake is allergic to the strings as loaded by json.
    def to_utf8(data):
        if isinstance(data, dict):
            return {to_utf8(dict_key): to_utf8(dict_value) for dict_key,dict_value in data.iteritems()}
        elif isinstance(data, list):
            return [to_utf8(list_entry) for list_entry in data]
        elif isinstance(data, unicode):
            return data.encode('utf-8')
        else:
            return data

    d.setVar("IMAGE_NAME_LINK", "${BPN}-${MACHINE}")
    with open('${IOT_DISK_LAYOUT_DIR}/disk-layout-${MACHINE}.json') as disk_layout:
        partition_table = to_utf8(json.load(disk_layout))

    full_image_size_mb = partition_table["gpt_initial_offset_mb"] + \
                         partition_table["gpt_tail_padding_mb"]

    for key in sorted(partition_table.iterkeys()):
        if not isinstance(partition_table[key], dict):
            continue
        full_image_size_mb += partition_table[key]["size_mb"]
        # Generate randomized uuids only if required uuid == 0
        # Otherwise leave whatever was set in the configuration file.
        if int(partition_table[key]['uuid']) == 0:
            partition_table[key]['uuid'] = str(uuid.uuid4())
        # Store these for the creation of the UEFI binary
        if partition_table[key]['name'] == 'rootfs':
            d.setVar("ROOTFS_PARTUUID", partition_table[key]['uuid'])
            d.setVar("ROOTFS_TYPE", partition_table[key]['filesystem'])
    # Now that the rootfs uuid is known, generate the UEFI binary, with commadnline
    bb.build.exec_func('build_uefi_executable', d)

    with open('${DEPLOY_DIR_IMAGE}/${IMAGE_NAME}-disk-layout.json', 'w') as disk_layout:
        json.dump(obj=partition_table, fp=disk_layout, indent=4, separators=(',', ': '))
    d.setVar("DISK_LAYOUT_FILE_NAME", "${IMAGE_NAME}-disk-layout.json")
    d.setVar("FULL_DISK_LAYOUT_FILE_NAME_LINK", "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}-disk-layout.json")
    bb.build.exec_func('create_symlink_to_disk_layout', d)

    d.setVar("IMAGE_FILE_NAME", "${IMAGE_NAME}.dsk")
    d.setVar("FULL_IMAGE_FILE_NAME", "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME}.dsk")
    d.setVar("FULL_IMAGE_FILE_NAME_LINK", "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}.dsk")
    d.setVar("FULL_IMAGE_SIZE_MB", str(full_image_size_mb))
    bb.build.exec_func('build_empty_image_file', d)

    partition_start_mb = partition_table["gpt_initial_offset_mb"]
    for key in sorted(partition_table.iterkeys()):
        if not isinstance(partition_table[key], dict):
            continue
        d.setVar("PARTITION_NAME", str(partition_table[key]["name"]))
        d.setVar("PARTITION_START_MB", str(partition_start_mb))
        d.setVar("PARTITION_SIZE_MB", str(partition_table[key]["size_mb"]))
        d.setVar("PARTITION_TYPE", str(partition_table[key]["type"]))
        d.setVar("PARTITION_UUID", str(partition_table[key]["uuid"]))
        d.setVar("PARTITION_FILESYSTEM", partition_table[key]["filesystem"])
        partition_file_name = "${IMAGE_NAME}." + partition_table[key]["name"] + ".part"
        full_partition_file_name = "${DEPLOY_DIR_IMAGE}/" + partition_file_name
        full_partition_file_name_symlink = "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}." + partition_table[key]["name"] + ".part"
        d.setVar("PARTITION_FILE_NAME", partition_file_name)
        d.setVar("FULL_PARTITION_FILE_NAME", full_partition_file_name)
        d.setVar("FULL_PARTITION_FILE_NAME_LINK", full_partition_file_name_symlink)
        d.setVar("PARTITION_SOURCE", partition_table[key]["source"])
        d.setVar("PARTITION_PRESERVE", '1' if partition_table[key]["preserve"].strip().lower() == 'yes' else '0')
        bb.build.exec_func("build_partition", d)
        bb.build.exec_func("process_partition", d)
        partition_start_mb += partition_table[key]["size_mb"]
    bb.build.exec_func("manifest_hack", d)
    d.setVar("VDI_IMAGE_FILE_NAME", "${IMAGE_NAME}.vdi")
    d.setVar("FULL_VDI_IMAGE_FILE_NAME", "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME}.vdi")
    d.setVar("FULL_VDI_IMAGE_FILE_NAME_LINK", "${DEPLOY_DIR_IMAGE}/${IMAGE_NAME_LINK}.vdi")
    bb.build.exec_func("vdi_from_raw", d)
}

IMAGE_TYPEDEP_ostro = "ext4"

# For IoT, the partitions and image are not created with the oe-core
# image_types.bbclass, so mask out the ext4 type and prevent the creation
# of a spurious .hdddirect image.
IMAGE_TYPES_MASKED += "ext4"
IMAGE_TYPES_MASKED += "ostro"

addtask do_rootfs before do_build
addtask do_image after do_rootfs
addtask do_image before do_build
