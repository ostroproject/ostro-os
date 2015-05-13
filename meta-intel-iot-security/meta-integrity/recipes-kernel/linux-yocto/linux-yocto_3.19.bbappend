FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# These patches come from rebasing
# a6aacbde406eeb6f8fc218b2c6172825f5e73fcf..b19a6214369cf1b9c23c1130ae3243c457112d5b
# from
# http://git.kernel.org/cgit/linux/kernel/git/kasatkin/linux-digsig.git/?h=ima-control-experimental
# (the upstream development branch for ima) onto v3.19.
#
# a6aacbde406eeb6f8fc218b2c6172825f5e73fcf was the
# most recent common commit in upstream Linux and
# ima-control-experimental, merged shortly before v3.19.
#
# Some patches had to be applied manually because
# of changes made between a6aac..v3.19 and some
# could be skipped because they were already
# included in v3.19 final.

SRC_URI_append = " \
file://0001-ima-limit-file-hash-setting-by-user-to-fix-and-log-m.patch \
file://0002-ima-reset-EVM-status-when-resetting-appraisal-status.patch \
file://0003-ima-re-introduce-own-integrity-cache-lock.patch \
file://0004-ima-reset-EVM-status-along-with-appraisal-status.patch \
file://0005-integrity-define-.evm-as-a-builtin-trusted-keyring.patch \
file://0006-evm-load-x509-certificate-from-the-kernel.patch \
file://0007-evm-provide-a-function-to-set-EVM-key-from-the-kerne.patch \
file://0008-ima-separate-security.ima-reading-functionality-from.patch \
file://0009-integrity-forbid-write-access-when-reading-data-to-t.patch \
file://0010-ima-load-policy-using-path.patch \
file://0011-ima-provide-ima_policy_check-hook.patch \
file://0012-evm-remove-helper-hmac-and-hash-calculation-function.patch \
file://0013-evm-provide-immutable-EVM-signature.patch \
file://0014-ima-provide-appraise_type-evmsig.patch \
file://0015-evm-require-EVM-signature-based-appraisal.patch \
file://0016-evm-load-EVM-key-from-the-kernel.patch \
file://0017-ima-limit-capabilities-for-unsigned-executables.patch \
file://0018-evm-fix-potential-race-when-removing-xattrs.patch \
file://0019-ima-do-not-remove-sysfs-policy-entry.patch \
file://0020-ima-pass-dentry-argument-to-the-policy-function.patch \
file://0021-ima-assume-that-ima_get_action-might-return-error.patch \
file://0022-ima-path-support-for-policy-definition.patch \
file://0023-ima-provide-buffer-hash-calculation-function.patch \
file://0024-ima-load-policy-from-the-kernel.patch \
file://0025-ima-provide-appraise_action-log-policy-parameter.patch \
file://0026-ima-rename-_sig-and-_digest-printing-functions-to-_h.patch \
file://0027-ima-add-new-template-field-for-inode-appraisal-statu.patch \
file://0028-ima-use-MAY_NOT_BLOCK-flag-to-select-memory-allocati.patch \
file://0029-ima-pass-dentry-instead-of-file.patch \
file://0030-ima-export-ima_fix_xattr.patch \
file://0031-ima-export-ima_alloc_tfm-and-ima_free_tfm.patch \
file://0032-ima-provide-inode-type-information-in-audit.patch \
file://0033-ima-hooks-for-directory-integrity-protection.patch \
file://0034-ima-directory-integrity-protection-implementation.patch \
file://0035-ima_dir-honor-appraise-permit-action.patch \
file://0036-ima-special-files-integrity-verification-implementat.patch \
file://0037-ima-hook-for-integrity-protection-of-symbolic-links.patch \
file://0038-evm-do-not-use-inode-generation-for-special-files.patch \
file://0039-ima-return-dentry-name-if-mnt-is-NULL.patch \
file://0040-ima-use-d_path-for-fifos-as-it-uses-d_op-d_name.patch \
file://0041-ima-add-read-method-to-policy-interface.patch \
file://0042-ima-add-infringements-counter-to-ima_fs.patch \
file://0043-ima-add-ima_state-interface.patch \
file://0044-ima-make-IMA-policy-replaceable-at-runtime.patch \
file://0045-evm-add-interface-to-read-and-write-EVM-state-ENABLE.patch \
"

# IMA_LOAD_POLICY is unusable in 3.19 (and other versions of the kernel) without this patch.
SRC_URI_append = " file://0001-ima-fix-configuration-of-policy-loading.patch"
