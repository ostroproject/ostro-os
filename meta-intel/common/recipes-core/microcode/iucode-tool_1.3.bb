SUMMARY = "Update Intel CPU microcode"

DESCRIPTION = "iucode_tool is a program to manipulate Intel i686 and X86-64\
 processor microcode update collections, and to use the kernel facilities to\
 update the microcode on Intel system processors.  It can load microcode data\
 files in text and binary format, sort, list and filter the microcode updates\
 contained in these files, write selected microcode updates to a new file in\
 binary format, or upload them to the kernel. \
 It operates on microcode data downloaded directly from Intel:\
 http://feeds.downloadcenter.intel.com/rss/?p=2371\
"
HOMEPAGE = "https://gitlab.com/iucode-tool/"
BUGTRACKER = "https://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=iucode-tool;repeatmerged=0"

LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://COPYING;md5=751419260aa954499f7abaabaa882bbe \
                    file://iucode_tool.c;beginline=1;endline=15;md5=f65c2be08bfd462331cadff25869588e"

SRC_URI = "https://gitlab.com/iucode-tool/releases/raw/master/iucode-tool_${PV}.tar.xz"
SRC_URI[md5sum] = "ad5aa3ed5eee2f9ef58a291fe7ca711d"
SRC_URI[sha256sum] = "c6e134fc63ac7e765f729c500adc9e154da57b02e991be35b421acf9c7eb0ea9"

S = "${WORKDIR}/iucode_tool-${PV}"

inherit autotools

BBCLASSEXTEND = "native"

COMPATIBLE_HOST = "(i.86|x86_64).*-linux"
