#!/usr/bin/env python
'''Function for json iteration'''
import subprocess
import sys
import jpath
import json


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
    subprocess.call(
        cmd,
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


def split_on_queries(line):
    '''
        Split line to list of 'normal' strings
        and jpath queries, queries are cleaned from braces
        Input:
            junk{.foo}trash{.bar}garbage
        Output:
            [ {'str':'junk'}, {'jpath':'.foo'},
            {'str':'trash'}, {'jpath':'bar'}, {'str':'garbage'}]

        '\\' is '\', '\(anycharacter)' is that character
        unescaped '{expression}' is jpath expression
        rest is just strings

    '''

    # finite state machine goes here, faster implementation welcomed
    # states: None - normal text
    # '{' - inside jpath
    # '\' - inside escaping
    buf = ""
    state = None
    for c in line:
        if state is None:
            if c == '{':
                if len(buf) > 0:
                    yield {'str': buf}
                buf = ""
                state = '{'
                continue
            if c == '\\':
                state = '\\'
                continue
            buf += c
            continue
        elif state == '{':
            if c == '}':
                yield {'jpath': buf}
                buf = ""
                state = None
                continue
            else:
                buf += c
        elif state == '\\':
            buf += c
            state = None
            continue
    if len(buf) > 0 and state is None:
        yield {'str': buf}
    if state is not None:
        pass  # Invalid syntax here


def make_queries(parsed_arg, json):
    '''
        apply jpath to every query in parsed args
        return list of strs
        (plain text and results of queries)
        expected generator as parsed_args
        and json to pass to jpath.
    '''
    for a in parsed_arg:
        if a.keys()[0] == 'str':
            yield a['str']
        elif a.keys()[0] == 'jpath':
            result = jpath.get(a['jpath'], json)
            # typechecking here
            yield str(result)


def process_arguments(arg_list, json, error_control=None):
    for arg in arg_list:
        yield ''.join(make_queries(split_on_queries(arg), json))


def prepare_out(out):
    '''
        prepare json output from subprocess object
        output is json object with following keys:
            returncode - return code of process
            stdout - stdout output of process
            stderr - stderr output of process

        Note: output should be collected prior wait()
        or deadlock occure!
    '''
    output = {}
    output['stdout'], output['stderr'] = out.communicate()
    out.wait()
    output['returncode'] = out.returncode
    return output


def jpath_exec(
    args,
    json_data,
    error_control=None,
    json_out=False,
    verbose=False
):

    to_exec = list(process_arguments(args, json_data, error_control))

    if verbose and not json_out:
        sys.stderr.write(' '.join(to_exec)+'\n')

    out_pipe = subprocess.PIPE
    err_pipe = subprocess.PIPE

    try:
        out = subprocess.Popen(
            to_exec,
            stdin=None,
            stdout=out_pipe,
            stderr=err_pipe
        )
        result = prepare_out(out)
    except OSError as error:
        result = {
            'stderr': str(to_exec[0]+": "+error.strerror),
            'stdout': '',
            'returncode': error.errno
        }
    if verbose and json_out:
        result['command'] = json.dumps(to_exec)

    if json_out:
        j = json.dumps(result)
        sys.stdout.write(j + '\n')
        if verbose:
            sys.stderr.write(j + '\n')
    else:
        if result['stdout']:
            sys.stdout.write(result['stdout']+'\n')
        if result['stderr']:
            sys.stderr.write(result['stderr']+'\n')
