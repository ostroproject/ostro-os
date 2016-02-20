SUBDIRS = .
MANIFEST_FILE = manifest

example_PROGRAMS = bad-groups
exampledir = @INSTALL_PATH@

hello_world_SOURCES = bad-groups.c
hello_world_CFLAGS = $(AM_CFLAGS) -DIOTPM_APPDIR=@APPDIR@

manifest_DATA = $(MANIFEST_FILE)
manifestdir = @MANIFEST_PATH@

BUILT_SOURCES = $(MANIFEST_FILE)

$(MANIFEST_FILE): manifest
	cp $< $(MANIFEST_FILE)

# cleanup
clean-local:
	-rm -f *~
