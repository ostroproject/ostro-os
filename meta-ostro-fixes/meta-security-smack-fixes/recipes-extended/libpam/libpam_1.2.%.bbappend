# libpam-1.2.% (upstream commit 7fbf54d6f4b67ed7bac04d801174ecfaa538c1a0)
# pulled via openembedded-core renamed configure.in to configure.ac

# pam-smack-so.patch needed by meta-security-smack layer tries to patch
# non-existent configure.in and the build fails.

# This .bbappend modifies do_patch() so that the patch can be applied
# without touching the patch itself. Better fix to be added after it's
# been decided what's the best way to do it.

# Upstream-Status: Inappropriate [proper fix needed]

do_patch_prepend() {
    import subprocess
    subprocess.call("cd ${S} && ln -sf configure.ac configure.in && cd -", shell=True)
}

do_patch_append() {
    import subprocess

    # XXX: configure.in symlink is gone since patching copies the file from
    # a temporary directory where the patching happened. In this case, we can
    # just move configure.in back to configure.ac to get the desired result.
    subprocess.call("cd ${S} && mv configure.in configure.ac && cd -", shell=True)
}
