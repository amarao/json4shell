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

def get_type(obj):
    return type(obj[1])


class JStore:
    def __init__(self, sequence):
        self.value = None
        for e in sequence:
            print "processing",e
            self.value =  self.add(self.value, e[0], e[1])
            print "result so far", self.value, "\n\n"

    def add(self, obj, path, value):
        if obj is None or not path:
            print "simple add", obj, '<=', path, value, "will return", value
            return value

        if len(path)==1:
            print "simple insertion", obj, "<=", path, value
            while(len(obj)<=path[0] and type(obj)==list):
                print "enlarging list", obj, "(len", len(obj), ") to", path[0]
                obj.append(None)
                print "becoming", obj, len(obj)
            obj[path[0]]=value
            return obj
        else:
            print "recursion", obj, path[1:], value
            x=obj
            x[path[0]]=self.add(obj[path[0]], path[1:], value)
            print "after recursion", x
            return x

    def res(self):
        return self.value


a= [o for o in JSONStream(filestream())]
print "input", a
b=JStore(a)
print "assembed", assembled(a)
print "jstore  ", b.res()

