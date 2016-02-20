IOTQA_EXTRA_IMAGEDEPENDS += "mraa-test mmap-smack-test tcp-smack-test udp-smack-test read-map shm-util gdb"
IOTQA_EXTRA_IMAGEDEPENDS += "${@bb.utils.contains('IMAGE_FEATURES', 'app-privileges', 'app-runas', '', d)}"

EXTRA_IMAGEDEPENDS += "${@bb.utils.contains('IMAGE_FEATURES', 'qatests', '${IOTQA_EXTRA_IMAGEDEPENDS}', '', d)}"

