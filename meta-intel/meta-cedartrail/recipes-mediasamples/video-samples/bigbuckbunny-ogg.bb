SUMMARY = "Big Buck Bunny video OGG sample "
DESCRIPTION = "Installs Big Buck Bunny Video OGG file samples in /home/video dir "

LICENSE = "CC-BY-3.0"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/CC-BY-3.0;md5=dfa02b5755629022e267f10b9c0a2ab7"

PR = "r0"

SRC_URI = "http://blender-mirror.kino3d.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_stereo.ogg \
            "


SRC_URI[md5sum] = "576424c653da53e31b86c027e55758ae"
SRC_URI[sha256sum] = "785b09a585be55f81326a3fcef2cdeeb7ebbc33932b6305fd84209928df67f28"

do_install() {

install -d ${D}${base_prefix}/home/Videos
install -m 0644  ${WORKDIR}/*.ogg ${D}${base_prefix}/home/Videos
}

FILES_${PN} += "${base_prefix}/home/Videos/*.ogg"
