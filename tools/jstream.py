#!/usr/bin/env python
'''
    test application to see how jsonstream works.
    should be used together with slowpipe.py
'''

from jsonstream import JSONStream
import sys

def filestream():
    while True:
        line = sys.stdin.readline()
        if not line: break # EOF
        yield line

for o in JSONStream(filestream()):
    print(o)
