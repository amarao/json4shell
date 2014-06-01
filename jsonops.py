#!/usr/bin/python
'''
	JSON ops - operation on json
	Every function accepts:
		j - json object
		args - defaultdict with options (None if no option defined)
	Every function returns processed json or raise exception
'''

def array_slice(j, args):
    argument = args[0] #The rest of arguments is not needed
    #argument is something like "[0:10]", let's try parsing that
    try:
        start, end = [int(x) for x in argument[1:-1].split(":")]
    except:
        raise #Need to define which exception is to be caught and which is to be thrown here
    if start > len(j):
        start=len(j)
    if end >len(j):
        end=len(j)
    return j[start:end]

def array_head(j,args):
    try:
        end = int(args[0])
    except:
        raise #Same here, need to see which exception is suitable here
    result = j[:end]
    return result

def array_tail(j,args):
    try:
        start = int(args[0])
    except:
        raise #Same here, need to see which exception is suitable here
    result = j[start:]
    return result

def array_get(j,args):
    try:
        position = int(args[0])
    except:
        raise #Same here, need to see which exception is suitable here
    result = j[position]
    return result

def array_uniq(j,args):
    #Can't think of any possible arguments now
    seen = {}
    result = []
    for item in j:
        if item in seen: continue
        seen[item] = 1
        result.append(item)
    return result

def array_shuffle(j, args):
    from random import shuffle
    #No args needed
    shuffle(j)
    return j

def array_sort(j,args):
    #TODO - implement string sorting according to language - will need to ompletely revise
    if "reversed" in args:
        j.sort(reverse=True)
    else:
        j.sort()
    return j
