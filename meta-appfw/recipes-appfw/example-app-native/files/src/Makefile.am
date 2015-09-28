SUBDIRS = .
MANIFEST_FILE = @PACKAGE_NAME@.manifest

example_PROGRAMS = hello-world
exampledir = @INSTALL_PATH@

hello_world_SOURCES = hello-world.c
hello_world_CFLAGS = $(AM_CFLAGS) -DIOTPM_APPDIR=@APPDIR@

manifest_DATA = $(MANIFEST_FILE)
manifestdir = @MANIFEST_PATH@

BUILT_SOURCES = $(MANIFEST_FILE)

$(MANIFEST_FILE): hello-world.manifest
	cp $< $(MANIFEST_FILE)

# cleanup
clean-local:
	-rm -f *~
