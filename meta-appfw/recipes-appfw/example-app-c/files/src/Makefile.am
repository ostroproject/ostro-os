SUBDIRS = .
MANIFEST_FILE = manifest

bin_PROGRAMS = hello-world

hello_world_SOURCES = hello-world.c

manifest_DATA = $(MANIFEST_FILE)
manifestdir = @MANIFEST_PATH@

# cleanup
clean-local:
	-rm -f *~
