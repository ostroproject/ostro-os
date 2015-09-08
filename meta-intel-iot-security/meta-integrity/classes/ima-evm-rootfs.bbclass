# Use keys included in layer by default.
IMA_EVM_KEY_DIR ?= "${IMA_EVM_BASE}/data/debug-keys"
IMA_EVM_PRIVKEY ?= "${IMA_EVM_KEY_DIR}/privkey_ima.pem"

# Public part of certificates.
IMA_EVM_X509 ?= "${IMA_EVM_KEY_DIR}/x509_ima.der"
IMA_EVM_ROOT_CA ?= "${IMA_EVM_KEY_DIR}/ima-local-ca.x509"

# Sign all regular files by default.
IMA_EVM_ROOTFS_SIGNED ?= ". -type f"
# Hash nothing by default.
IMA_EVM_ROOTFS_HASHED ?= ". -depth 0 -false"

ima_evm_sign_rootfs () {
    cd ${IMAGE_ROOTFS}

    # Copy file(s) which must be on the device. Use the name as expected
    # by evmctl to make "evmctl ima_verify" work out-of-the-box, even
    # though the tool is probably using the wrong name (should be x509_ima.der
    # as in the kernel default).
    install -d ./${sysconfdir}/keys
    install "${IMA_EVM_X509}" ./${sysconfdir}/keys/x509_evm.der

    # Sign file with private IMA key. EVM not supported at the moment.
    bbnote "IMA/EVM: signing files 'find ${IMA_EVM_ROOTFS_SIGNED}' with private key '${IMA_EVM_PRIVKEY}'"
    find ${IMA_EVM_ROOTFS_SIGNED} | xargs -d "\n" --max-args=1 --no-run-if-empty --verbose evmctl ima_sign --key ${IMA_EVM_PRIVKEY}
    bbnote "IMA/EVM: hashing files 'find ${IMA_EVM_ROOTFS_HASHED}'"
    find ${IMA_EVM_ROOTFS_HASHED} | xargs -d "\n" --max-args=1 --no-run-if-empty --verbose evmctl ima_hash

    # Optionally install custom policy for loading by systemd.
    if [ "${IMA_EVM_POLICY_SYSTEMD}" ]; then
        install -d ./${sysconfdir}/ima
        install "${IMA_EVM_POLICY_SYSTEMD}" ./${sysconfdir}/ima/ima-policy
    fi
}

# Signing must run as late as possible in the do_rootfs task.
# IMAGE_PREPROCESS_COMMAND runs after ROOTFS_POSTPROCESS_COMMAND, so
# append (not prepend!) to IMAGE_PREPROCESS_COMMAND, and do it with
# _append instead of += because _append gets evaluated later. In
# particular, we must run after prelink_image in
# IMAGE_PREPROCESS_COMMAND, because prelinking changes executables.

IMAGE_PREPROCESS_COMMAND_append = " ima_evm_sign_rootfs ; "

# evmctl must have been installed first.
do_rootfs[depends] += "ima-evm-utils-native:do_populate_sysroot"
