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
        self.iterator=iterator

    def __iter__(self):
        self.iterator=self.iterator.__iter__()
        self.processed=1
        return self

    def gather(self):
        old_size=1
        for e in self.iterator:
            self.value =  self.add(self.value, e[0], e[1])
            if len(self.value)>old_size:
                yield 
            

    def next(self):
#        print "iteration start:", self.value
        while not self.value or len(self.value)<=self.processed:
            e = self.iterator.next()
            self.value =  self.add(self.value, e[0], e[1])
#        print "iteration end:", self.value
        self.processed += 1
        return self.value[self.processed-2]


    def add(self, obj, path, value):
        if obj is None or not path:
            return value

        if len(path)==1:
            if type(obj) == list:
                obj.append(value)
            elif type(obj) == dict:
                obj[path[0]] = value
            else:
                raise Exception("Bad obj")
        else:
            if type(obj) == list:
                obj[-1] = self.add(obj[-1], path[1:], value)
            elif type(obj) == dict:
                obj[path[0]] = self.add(obj[path[0]], path[1:], value)
            else:
                raise Exception("Bad obj")
        return obj

    def res(self):
        return self.value


for o in JStore(JSONStream(filestream())):
    print "out", o
    
