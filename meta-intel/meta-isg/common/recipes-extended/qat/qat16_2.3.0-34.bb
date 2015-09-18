include qat16.inc

SRC_URI += "file://qat16_2.3.0-34-qat-add-install-target-to-makefiles.patch \
            file://qat16_2.3.0-34-qat-replace-strict_strtoull-with-kstrtoull.patch \
            "

SRC_URI[qat.md5sum] = "9614bf598bc8e7eedc8adb6d29109033"
SRC_URI[qat.sha256sum] = "1f9708de3c132258eaa488c82760f374b6b6838c85cafef2e8c61034fe0f7031"
