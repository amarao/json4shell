#!/usr/bin/python
'''
	JSON ops - operation on json
	Every function accepts:
		j - json object
		args - defaultdict with options (None if no option defined)
	Every function returns processed json or raise exception
'''

def array_slice (j, args):
	start=args["start"]
	end=args["end"]
	if type(start) != int or start > len(j):
		start=None
	if type (end) != int or end >len(j):
		end=None
	return j[start:end]

def array_head(j,args):
	if not args["end"]:
		args.update({"end":1})
	return array_slice(j,args)

def array_tail(j,args):
	if not args["start"]:
		args.update({"start":-1})
	return array_slice(j,args)

