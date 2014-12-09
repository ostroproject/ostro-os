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
HOMEPAGE = "http://gitorious.org/iucode-tool/"
BUGTRACKER = "https://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=iucode-tool;repeatmerged=0"

LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://COPYING;md5=751419260aa954499f7abaabaa882bbe \
                    file://iucode_tool.c;beginline=1;endline=15;md5=94d9128c5b95d5c249197a3854f40003"

SRC_URI = "git://gitorious.org/iucode-tool/iucode-tool.git"
SRCREV = "0ba2ebe57681435fdd0d8af2675c84783b5fa2aa"
S = "${WORKDIR}/git"

inherit autotools

BBCLASSEXTEND = "native"

COMPATIBLE_HOST = "(i.86|x86_64).*-linux"
