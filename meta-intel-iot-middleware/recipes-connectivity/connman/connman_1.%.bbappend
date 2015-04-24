PACKAGECONFIG[bluetooth] = "--enable-bluetooth, --disable-bluetooth, bluez5"
RDEPENDS_${PN}_remove = "bluez4"
RDEPENDS_${PN}_append = "bluez5"

