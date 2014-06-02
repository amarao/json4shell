json4shell
==========

Set of utilities for shell for json processing

(initial work in progress, do not use in production. Seriously!)

See 
* http://amarao-san.livejournal.com/2813949.html for whole idea (Russian)
* http://habrahabr.ru/post/102072 public idea (Russian)


Developer notes
===============

1. Contribution is welcome!
2. Any module is ok if it does not create additional dependences or force additional rules on other modules.
3. use pep8 on file before commiting (apt-get install pep8, pep8 *.py)

Internal architecture:

For development purposes commands are added as arg[1]. Later, selection will be moved to arg[0] and symlinks 
with different names to same binary.

Every module should use own argparse code. This can be changed in future to help support common options.

Common rules:
1. Output (except 'outputs') should be json only to stdout. Any complains may be send to stderr.
2. Exit codes:
    On success exit code is 0
    On critical failure (invalid options) exit code should be -1
    On unexpected file close exit code should be 2
    On invalid input exit code should be 3
    Rest of codes - for command-specific cases
3. Input (except 'input' type should be expected as one or more JSONs, separated by any combination of spaces, 
tabs and line feeds.
4. If few json's are in input, they should be threated as single array of elements (output can be few JSONs or
one JSON with array at you preferences)


Types of commands:
1. Inputs: take something (from stdin or from external datasource) and output json to stdout.
2. Filters: take json on stdin, return changed json to stdout.
3. Iterators: execute other commands on some (every?) element of JSON, return commands output instead of elements.
4. Outputs: take JSON, return something, depends on internals.

