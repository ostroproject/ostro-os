# Check that the user has explicitly chosen how to build images.
OSTRO_IMAGE_BUILD_MODE_SELECTED ?= ""
addhandler ostro_sanity_check_eventhandler
ostro_sanity_check_eventhandler[eventmask] = "bb.event.SanityCheck"
python ostro_sanity_check_eventhandler() {
    if not d.getVar('OSTRO_IMAGE_BUILD_MODE_SELECTED', True):
        bb.fatal('''local.conf must be explicitly edited to select between building
production and development images. See the comments in local.conf.sample
and doc/howtos/building-images.rst.''')
}
