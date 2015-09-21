FILESEXTRAPATHS_prepend := "${THISDIR}/linux-yocto:"

### Config "fix" fragments

### Hardware support fragments

# I2C sensors
SRC_URI_append_intel-quark = " file://sensors.cfg"
SRC_URI_append_edison = " file://sensors.cfg"
SRC_URI_append_beaglebone = " file://sensors.cfg"
#  Minnow Max has I2C
SRC_URI_append_intel-corei7-64 = " file://sensors.cfg"
SRC_URI_append_intel-core2-32 = " file://sensors.cfg"
# backport BH1750 light sensor support on Minnow Max and NUC
SRC_URI_append_intel-corei7-64 = " file://0001-iio-light-add-support-for-ROHM-BH1710-BH1715-BH1721-.patch"
SRC_URI_append_intel-core2-32 = " file://0001-iio-light-add-support-for-ROHM-BH1710-BH1715-BH1721-.patch"
SRC_URI_append_intel-corei7-64 = " file://bh1750.cfg"
SRC_URI_append_intel-core2-32 = " file://bh1750.cfg"

#  BeagleBone Black enable all I2Cs
SRC_URI_append_beaglebone = " file://0001-v3.15.0-ARM-dts-am335x-boneblack-configure-i2c1-and-2.patch"

# IIO support
SRC_URI_append_beaglebone = " file://iio.cfg"

# NFC support and drivers
SRC_URI_append = " file://nfc.cfg"
SRC_URI_append_intel-quark = " file://nfc-spi.cfg"
SRC_URI_append_edison = " file://nfc-spi.cfg"
SRC_URI_append_beaglebone = " file://nfc-spi.cfg"
#  Minnow Max has SPI
SRC_URI_append_intel-corei7-64 = " file://nfc-spi.cfg"
SRC_URI_append_intel-quark = " file://nfc-i2c.cfg"
SRC_URI_append_edison = " file://nfc-i2c.cfg"
SRC_URI_append_beaglebone = " file://nfc-i2c.cfg"
#  Minnow Max has I2C
SRC_URI_append_intel-corei7-64 = " file://nfc-i2c.cfg"

# USB-serial interface support and drivers
SRC_URI_append = " file://usb-serial.cfg"

# CAN-bus support and drivers
SRC_URI_append = " file://can.cfg"
SRC_URI_append_intel-quark = " file://can-spi.cfg"
SRC_URI_append_edison = " file://can-spi.cfg"
SRC_URI_append_beaglebone = " file://can-spi.cfg"
#  MinnowMax has SPI
SRC_URI_append_intel-corei7-64 = " file://can-spi.cfg"
SRC_URI_append_intel-core2-32 = " file://can-x86.cfg"
SRC_URI_append_intel-corei7-64 = " file://can-x86.cfg"

# RealTek WiFi chip used on Gigabyte GB-BXBT-3825
SRC_URI_append_intel-core2-32 = " file://wireless.cfg"
SRC_URI_append_intel-corei7-64 = " file://wireless.cfg"

# 6lowpan support
SRC_URI_append = " file://6lowpan.cfg"

# 6lowpan over 802154 support and drivers
SRC_URI_append = " file://6lowpan-802154.cfg"

# 6lowpan over Bluetooth LE support
SRC_URI_append = " file://6lowpan-btle.cfg"
SRC_URI_append_intel-quark = " file://debug-fs.cfg"

# Bluetooth and Bluetooth LE support on Galileo Gen 2
SRC_URI_append_intel-quark = " file://bluetooth.cfg"
