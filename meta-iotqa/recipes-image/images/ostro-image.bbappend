EXTRA_IMAGEDEPENDS += "mraa-test sensor-test"

TESTIMAGEDEPENDS += " \
	mraa-test:do_install \
	sensor-test:do_install \
	systemd:do_install \
	"
