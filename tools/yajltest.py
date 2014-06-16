#!/usr/bin/python
'''
    test application to see how yajl works.
    should be used together with slowpipe.py
    Most of the code from from https://pykler.github.io/yajl-py/
'''

from yajl import *
import sys

class ContentHandler(YajlContentHandler):
    def __init__(self):
        self.out = sys.stdout
    def yajl_null(self, ctx):
        self.out.write("null\n" )
    def yajl_boolean(self, ctx, boolVal):
        self.out.write("bool: %s\n" %('true' if boolVal else 'false'))
    def yajl_integer(self, ctx, integerVal):
        self.out.write("integer: %s\n" %integerVal)
    def yajl_double(self, ctx, doubleVal):
        self.out.write("double: %s\n" %doubleVal)
    def yajl_number(self, ctx, stringNum):
        ''' Since this is defined both integer and double callbacks are useless '''
        num = float(stringNum) if '.' in stringNum else int(stringNum)
        self.out.write("number: %s\n" %num)
    def yajl_string(self, ctx, stringVal):
        self.out.write("string: '%s'\n" %stringVal)
    def yajl_start_map(self, ctx):
        self.out.write("map open '{'\n")
    def yajl_map_key(self, ctx, stringVal):
        self.out.write("key: '%s'\n" %stringVal)
    def yajl_end_map(self, ctx):
        self.out.write("map close '}'\n")
    def yajl_start_array(self, ctx):
        self.out.write("array open '['\n")
    def yajl_end_array(self, ctx):
        self.out.write("array close ']'\n")

parser = YajlParser(ContentHandler())

parser.parse()
