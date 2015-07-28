include dpdk.inc

SRC_URI[dpdk.md5sum] = "e9e7935c9eec920841ad373949514934"
SRC_URI[dpdk.sha256sum] = "643789a3be5ba44dd84d6b248cdf5471b260f8736dada177dadf076aebfbff3f"

export EXAMPLES_BUILD_DIR = "${RTE_TARGET}"
export ARCHDIR = "generic"
