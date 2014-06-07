#!/usr/bin/env python

import json
'''
    JSON ops - operation on json
    Every function accepts:
        j - json object
        args - defaultdict with options (None if no option defined)
    Every function returns processed json or raise exception
'''


def array_slice(j, start, end):
    '''
        slice array with given "start" and "end"
    '''
    start = min(start, len(j))
    end = min(end, len(j))
    return pprint(j[start:end])


def array_head(j, end):
    '''
        like array_slice, but "start" is zero
    '''
    end = min(end, len(j))
    return pprint(j[:end])


def array_tail(j, start):
    '''
        like array_slice, but "end" is len(j)
    '''
    start = min(start, len(j))
    return pprint(j[start:])


def array_get(j, index):
    '''
        get array element by it index
    '''
    # TODO: handle bad index
    return j[index]


def array_uniq(j):
    '''
        returns array with only unique elements
    '''
    # Can't think of any possible arguments now
    seen = {}
    result = []
    for item in j:
        if item in seen:
            continue
        seen[item] = 1
        result.append(item)
    return pprint(result)


def array_shuffle(j):
    '''
        randomly displaces array elements
    '''
    # No args needed
    from random import shuffle
    shuffle(j)
    return pprint(j)


def array_sort(j, is_reversed=False):
    '''
        sort array by it values
    '''
    # TODO: implement string sorting
    # according to language - will need to ompletely revise
    j.sort(reverse=is_reversed)
    return pprint(j)


def object_get(j, key):
    '''
        return value for key
    '''
    # TODO: types for keys!
    # TODO: Bad argument handling
    return pprint(j[key])


def object_keys(j):
    '''
        return array of keys from object (stip off values)
    '''
    return pprint(j.keys())


def object_values(j):
    '''
        return array of values from object (stip off keys)
    '''
    return pprint(j.values())


def array_enumerate(j, cnt=0):
    '''
        convert array to object, adding order number as key
        if cnt present, it used as number, if not,
        numbering happens from 0.
    '''
    ret = {}
    for e in j:
        ret[cnt] = e
        cnt += 1
    return pprint(ret)


def load_json(line):
    '''
        reads string as JSON object and return python representation
    '''
    return json.loads(line, "utf-8")


def pprint(j, indent=4, sort_keys=False):
    '''
        pretty-prints json object/array.
        indent - number of spaces to indent nesting
        sort_keys - sort keys in objects
    '''
    return json.dumps(
        j, ensure_ascii=False, indent=indent,
        encoding="utf-8", sort_keys=sort_keys)
