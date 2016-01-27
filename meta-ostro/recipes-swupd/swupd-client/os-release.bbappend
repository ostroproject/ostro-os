VERSION_ID = "${@bb.data.getVar('BUILD_ID',d,1).split('-')[-1].join(['', '0']) }"
