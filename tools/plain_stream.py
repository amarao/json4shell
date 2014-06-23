#!/usr/bin/env python
from jsonstream import JSONStream
import sys

def filestream():
    while True:
        line = sys.stdin.readline()
        if not line:
            break # EOF
        yield line

for o in JSONStream(filestream()):
    print(o)


