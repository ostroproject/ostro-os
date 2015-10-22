#!/usr/bin/env python

import os
import sys

try:
	uid = int(sys.argv[1])
	sys.argv.pop(1)
	label = sys.argv[1]
	sys.argv.pop(1)
	open("/proc/self/attr/current", "w").write(label)
	path=sys.argv[1]
	sys.argv.pop(0)
	os.setgid(uid)
	os.setuid(uid)	
	os.execv(path,sys.argv)

except Exception,e:
	print e.message
	sys.exit(1)
