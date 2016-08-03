require mraa.inc

SRC_URI = "git://github.com/intel-iot-devkit/mraa.git;protocol=git;tag=v${PV} \
           file://0001-intel_galileo_rev_d.c-Move-code-for-gen1-from-pwm.c-.patch \
           file://0001-firmata_mraa.c-Fixed-aio-bug.patch"
