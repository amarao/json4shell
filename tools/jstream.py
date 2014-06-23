#!/usr/bin/env python
'''
    test application to see how jsonstream works.
    should be used together with slowpipe.py
'''

from jsonstream import JSONStream
from jsonstream import assembled
import sys
import jpath

def filestream():
    while True:
        line = sys.stdin.readline()
        if not line: 
            break # EOF
        yield line

def dict_o_stream(stream):
    '''
        stream whole dicts out of stream
    '''
    j=JSONStream(stream).__iter__()
    empty=((), {})
    buffer=[]
    while True:
        try:
            obj=j.next()
            if ( obj[1] == [] or obj[1] == {}):
                if buffer and buffer != [empty]:
                #new object detected
#                    print "yield", buffer
                    yield assembled(buffer)
                #like we start an new dict
                buffer=[empty]
#                print "adding", buffer
            else:
                # like if we just creating dict
                buffer.append((((obj[0][-1]),), obj[1]))
#                print "adding", obj, "  ==>   ", (((obj[0][-1]),), obj[1]), "           ====> ",buffer
        except StopIteration:
            if buffer:
                yield assembled(buffer)
            return

for o in dict_o_stream(filestream()):
    print(o)

