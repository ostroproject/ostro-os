#!/usr/bin/env python

import os
import sys

os.setuid(1)

try:
    path=sys.argv[1]
    sys.argv.pop(0)
    os.execv(path,sys.argv)
except Exception,e:
    print e.message
    sys.exit(1)

sys.exit(0)