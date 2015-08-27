include dpdk.inc

SRC_URI += "file://dpdk-1.8.0-and-2.0.0-examples-add-config-variable-to-enable-disable-dpdk.patch"

SRC_URI[dpdk.md5sum] = "11ad8785aaa869cc87265bcb8d828f22"
SRC_URI[dpdk.sha256sum] = "9f5386830bd999355182e20408f3fc2cfa0802a4497fdded8d43202feede1939"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"

do_install_append () {

	install -m 0755 -d ${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp
	install -m 0755 ${S}/${RTE_TARGET}/hostapp/*	${D}/${INSTALL_PATH}/${RTE_TARGET}/hostapp/
}
