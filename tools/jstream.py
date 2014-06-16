#!/usr/bin/python
'''
    test application to see how jsonstream works.
    should be used together with slowpipe.py
'''

from jsonstream import JSONStream
import sys

def filestream(fd):
    for line in fd:
        yield line 

for o in JSONStream(filestream(sys.stdin)):
    print o
