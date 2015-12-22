EXTRA_IMAGEDEPENDS += "mraa-test mmap-smack-test tcp-smack-test udp-smack-test"
EXTRA_IMAGEDEPENDS += "${@bb.utils.contains('IMAGE_FEATURES', 'app-privileges', 'app-runas', '', d)}"
