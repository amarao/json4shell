#!/usr/bin/env python

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

class JStore:
    def __init__(self, sequence):
        self.value = None
        for e in sequence:
            self.value =  self.add(self.value, e[0], e[1])

    def add(self, obj, path, value):
        if obj is None or not path:
            return value

        if len(path)==1:
            while(len(obj)<=path[0] and type(obj)==list):
                obj.append(None)
            obj[path[0]]=value
        else:
            obj[path[0]]=self.add(obj[path[0]], path[1:], value)
        return obj

    def res(self):
        return self.value


a= [o for o in JSONStream(filestream())]
print "input", a
b=JStore(a)
print "assembed", assembled(a)
print "jstore  ", b.res()

