#!/usr/bin/python
'''
    This utility outputs input with certain latency between lines,
    allowing to debug json-streamed applications on small data subsed
'''

import sys
import time

try:
    latency=float(sys.argv[1])
except:
    latency=1

for line in sys.stdin:
    sys.stdout.write(line)
    time.sleep(latency)
