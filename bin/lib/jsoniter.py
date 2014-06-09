#!/usr/bin/env python
'''Function for json iteration'''
import subprocess
import sys


def get_array_inner_types(a):
    '''
        Return tuple of types
        found in array
    '''
    return set(map(type, a))


def simple_exec(cmd, j):
    '''
        execute cmd (list of command and it arguments)
        take j objects to iterate over
    '''
    args = cmd + j
    subprocess.call(
        args,
        stdout=sys.stdout,
        stderr=sys.stderr
    )


def iterate_array_in_depth(a, recursion):
    for e in a:
        if type(e) == list:
            if recursion == 'depth':
                for i in iterate_array_in_depth(e, recursion):
                    yield i
            else:
                raise Exception  # fix!
        elif type(e) in (str, bool, int):
            yield e
        else:
            raise Exception  # fix!


def iterate_array_in_width(a, recursion):
    toplevel = []
    for e in a:
        if type(e) == list:
            toplevel.append(e)
        elif type(e) in (str, bool, int):
            yield e
        else:
            raise Exception  # fix!
    if toplevel and recursion != 'width':
        raise Exception  # fix!
    for l in toplevel:
        for i in iterate_array_in_width(l, recursion):
            yield i


def iterate_array(j, items_at_once=0, recursion=None):
    '''
        Iterate over array or recursive arrays (j)
        Perform recursion:
            * None - no recursion
            * "depth" - in depth
            * "width" - in width
        Limit yelding to 'items_at_once' elements
        per time (0 - no limit)
        Raise ExceptionObject if dict found
        Raise ExceptionNoRecursion if no recursion
            and (sub)list found

        All returned elements are converted to strings
    '''
    stash = []
    if recursion == 'width':
        op = iterate_array_in_width
    else:
        op = iterate_array_in_depth  # in depth and no recursion
    for obj in op(j, recursion):
        if len(stash) >= items_at_once and items_at_once > 0:
            yield stash
            stash = []
        stash.append(str(obj))
    if len(stash) > 0:
        yield stash
