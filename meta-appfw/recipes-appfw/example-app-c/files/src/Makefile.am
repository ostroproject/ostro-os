SUBDIRS = .
MANIFEST_FILE = manifest

example_PROGRAMS = hello-world
exampledir = @INSTALL_PATH@

hello_world_SOURCES = hello-world.c

manifest_DATA = $(MANIFEST_FILE)
manifestdir = @MANIFEST_PATH@

# cleanup
clean-local:
	-rm -f *~
