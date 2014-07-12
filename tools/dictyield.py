#!/usr/bin/env python

from jsonstream import JSONStream
from jsonstream import assembled
import sys

def filestream():
    while True:
        line = sys.stdin.readline()
        if not line: 
            break # EOF
        yield line

class JStore:
    def __init__(self, iterator):
        self.value = None
        self.iterator=iterator.__iter__

    def __iter__(self):
        return self.yielder()

    def yielder(self):
        for e in self.iterator():
            new_value =  self.add(self.value, e[0], e[1])
            if len(new_value) == 0 and self.value:
                yield self.value.pop(0)
            self.value=new_value
            if len(self.value)>1:
                yield self.value.pop(0)
        yield self.value.pop(0)


    def add(self, obj, path, value):

        if obj is None or not path:
            return value

        if type(obj) == list:
            key=-1
            if len(path) == 1:
                obj.append(None)
        elif type(obj) == dict:
            key = path[0]
            if len(path) == 1:
                obj[path[0]] = None
        else:
            raise TypeError()

        obj[key] = self.add(obj[key],path[1:],value)
        return obj

    def res(self):
        return self.value


for o in JStore(JSONStream(filestream())):
    print "out", o
    
