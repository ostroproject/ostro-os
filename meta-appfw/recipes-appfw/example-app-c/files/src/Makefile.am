SUBDIRS = .
MANIFEST_FILE = manifest

example_PROGRAMS = hello-world
exampledir = @INSTALL_PATH@

hello_world_SOURCES = hello-world.c
hello_world_CFLAGS = $(AM_CFLAGS) -DIOTPM_APPDIR=@APPDIR@

manifest_DATA = $(MANIFEST_FILE)
manifestdir = @MANIFEST_PATH@

# cleanup
clean-local:
	-rm -f *~
