#!/usr/bin/env python
'''Function for json iteration'''
import subprocess
import sys


def get_array_inner_types(a):
    '''
        Return tuple of types
        found in array
    '''
    return tuple(set(map(type, a)))


def simple_exec(cmd, j):
    args = cmd + [str(j)]
    subprocess.call(
        args,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
