#!/usr/bin/env python
"""
Not ready

StartState - starting state
OkayState - ready for regular string
ValueState - ready for string in jpath
EscapeState - going to add not-regular symbol (like '{') to buffer
"""

import unittest
try:
    from builtins import chr as _chr
except ImportError:
    from __builtin__ import unichr as _chr


class Action(object):
    """Main class for various actions """

    def __init__(self, state, result, token, buffer, before):
        self.state = state
        self.result = result
        self.token = token
        self.buffer = buffer
        self.before = before

    def perform_state_switch(self):
        getattr(self, self.state)()

    def change_action(self, action):
        self.__class__ = action

    def return_result(self):
        result = self.result
        self.result = None
        return result

    def buf_append(self, string):
        if self.buffer is None:
            self.buffer = ""
        self.buffer += string

    def StartState(self):
        pass

    def OkayState(self):
        pass

    def ValueState(self):
        pass

    def EscapeState(self):
        pass


class OpenCurlyBracketAction(Action):
    """ { symbol action """

    def StartState(self):
        if self.buffer is not None:
            self.result = {"str": self.buffer}
            self.buffer = None
        self.state = "ValueState"

    def OkayState(self):
        if self.buffer is not None:
            self.result = {"str": self.buffer}
            self.buffer = None
        self.state = "ValueState"

    def ValueState(self):
        raise Exception("SyntaxError - can't open brace in another brace!")

    def EscapeState(self):
        self.buf_append(self.token)
        self.state = self.before


class CloseCurlyBracketAction(Action):
    """ } symbol action """

    def StartState(self):
        raise Exception("SyntaxError - close brace in start of line")

    def OkayState(self):
        raise Exception("SyntaxError - can't close brace, if there is no open")

    def ValueState(self):
        if self.buffer is not None:
            self.result = {"jpath": self.buffer}
            self.buffer = None
        elif self.buffer is None:
            self.result = {"jpath": ""}
        self.state = "OkayState"

    def EscapeState(self):
        self.buf_append(self.token)
        self.state = self.before


class BackslashAction(Action):
    """ \ symbol action """

    def StartState(self):
        self.before = self.state
        self.state = "EscapeState"

    def OkayState(self):
        self.before = self.state
        self.state = "EscapeState"

    def ValueState(self):
        self.before = self.state
        self.state = "EscapeState"

    def EscapeState(self):
        self.buf_append("\\")
        self.state = self.before


class StringAction(Action):
    """ Action for everything else """

    def StartState(self):
        self.buf_append(self.token)

    def OkayState(self):
        self.buf_append(self.token)

    def ValueState(self):
        self.buf_append(self.token)

    def EscapeState(self):
        if self.token[:1] == "t":
            value = "\t" + self.token[1:]
        elif self.token[:1] == "n":
            value = "\n" + self.token[1:]
        elif self.token[:1] == "b":
            value = "\b" + self.token[1:]
        elif self.token[:1] == "f":
            value = "\f" + self.token[1:]
        elif self.token[:1] == "r":
            value = "\r" + self.token[1:]
        elif self.token[:1] == "u":
            value = _chr(int(self.token[1:5], 16)) + self.token[5:]
        else:
            value = self.token

        self.buf_append(value)
        self.state = self.before


class EOFAction(Action):
    """ End Of File action """

    def StartState(self):
        if self.buffer is not None:
            self.result = {"str": self.buffer}
            self.buffer = None

    def OkayState(self):
        if self.buffer is not None:
            self.result = {"str": self.buffer}
            self.buffer = None

    def ValueState(self):
        raise Exception("SyntaxError - not closed brace")

    def EscapeState(self):
        raise Exception("SyntaxError - tried to escape EOF")


def tokenize_line(line):
    token_syms = ["\\", "{", "}"]
    cpos = 0
    while True:
        current_piece = line[cpos:]
        piece_len = len(current_piece)
        positions = map(current_piece.find, token_syms)
        norm_positions = map(lambda x: piece_len if x < 0 else x, positions)
        min_i, min_v = min(enumerate(norm_positions), key=lambda p: p[1])

        if min_v:
            yield current_piece[:min_v]

        if min_v == piece_len:
            break

        yield token_syms[min_i]
        cpos += min_v + len(token_syms[min_i])


def split_on_queries_ex(line):

    action = Action(
        state="StartState",
        result=None,
        token=None,
        buffer=None,
        before=None)

    for i in tokenize_line(line):
        action.token = i

        if i == "{":
            action.change_action(OpenCurlyBracketAction)
            action.perform_state_switch()

        elif i == "}":
            action.change_action(CloseCurlyBracketAction)
            action.perform_state_switch()

        elif i == "\\":
            action.change_action(BackslashAction)
            action.perform_state_switch()

        else:
            action.change_action(StringAction)
            action.perform_state_switch()

        result = action.return_result()
        if result is not None:
            yield result

    action.change_action(EOFAction)
    action.perform_state_switch()

    result = action.return_result()
    if result is not None:
        yield result


class TokenizaTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            list(tokenize_line("")),
            []
        )

    def test_simple(self):
        self.assertEqual(
            list(tokenize_line("foo{foo{foo{bar")),
            ['foo', '{', 'foo', '{', 'foo', '{', 'bar']
        )
        self.assertEqual(
            list(tokenize_line("junk{.foo\\}trash\\{.bar}garbage")),
            ['junk', '{', '.foo', '\\', '}', 'trash',
                '\\', '{', '.bar', '}', 'garbage']
        )
        self.assertEqual(
            list(tokenize_line("junkfoo\\trash\\bargarbage")),
            ['junkfoo', '\\', 'trash', '\\', 'bargarbage']
        )
        self.assertEqual(
            list(tokenize_line("junkfoo\\{trash")),
            ['junkfoo', '\\', '{', 'trash']
        )
        self.assertEqual(
            list(tokenize_line("junk{.foo}trash{.bar}garbage")),
            ['junk', '{', '.foo', '}', 'trash', '{', '.bar', '}', 'garbage']
        )

    # TODO: MOAR TEST


class SplitOnQueriesTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            list(split_on_queries_ex('')),
            []
        )

    def test_simple(self):
        self.assertEqual(
            list(split_on_queries_ex('a')),
            [{'str': 'a'}]
        )

    def test_one(self):
        self.assertEqual(
            list(split_on_queries_ex('{query}')),
            [{'jpath': 'query'}]
        )
        self.assertEqual(
            list(split_on_queries_ex('{}')),
            [{'jpath': ''}]
        )

    def test_escaping(self):
        self.assertEqual(
            list(split_on_queries_ex('\\\\\\{\\a\}')),
            [{'str': '\\{a}'}]
        )

    def test_complex(self):
        self.assertEqual(
            list(split_on_queries_ex(
                '\\\\_#{$~}-!("){}a1@*{\\\\}')),
            [
                {'str': '\\_#'}, {'jpath': '$~'},
                {'str': '-!(")'}, {'jpath': ''},
                {'str': 'a1@*'}, {'jpath': '\\\\'}
            ]
        )

    def test_various(self):
        self.assertEqual(
            list(split_on_queries_ex(
                'junk{.foo}trash{.bar}garbage')),
            [{'str': 'junk'}, {'jpath': '.foo'},
                {'str': 'trash'}, {'jpath': '.bar'}, {'str': 'garbage'}]
        )
        self.assertEqual(
            list(split_on_queries_ex(
                'junk{.foo\\}trash\\{.bar}garbage')),
            [{'str': 'junk'}, {'jpath': '.foo}trash{.bar'}, {'str': 'garbage'}]
        )
        self.assertEqual(
            list(split_on_queries_ex(
                'ju\\nk{.foo}trash{.bar}garbage')),
            [{'str': 'ju\nk'}, {'jpath': '.foo'},
                {'str': 'trash'}, {'jpath': '.bar'}, {'str': 'garbage'}]
        )
        self.assertEqual(
            list(split_on_queries_ex(
                'junk{.foo}t\\rash{.bar}garbage')),
            [{'str': 'junk'}, {'jpath': '.foo'},
                {'str': 't\rash'}, {'jpath': '.bar'}, {'str': 'garbage'}]
        )

    def test_unicode(self):
        self.assertEqual(
            list(split_on_queries_ex('{\\u0843}')),
            [{'jpath': u'\u0843'}]
        )

        self.assertEqual(
            list(split_on_queries_ex('\\u0843{\\u0843}\\u0843')),
            [{'str': u'\u0843'}, {'jpath': u'\u0843'}, {'str': u'\u0843'}]
        )

    def test_control_chars(self):
        self.assertEqual(
            list(split_on_queries_ex('{\\t\\n\\b\\f\\r}')),
            [{'jpath': '\t\n\b\f\r'}]
        )
        self.assertEqual(
            list(split_on_queries_ex(
                '\\t\\n\\b\\f\\r{\\t\\n\\b\\f\\r}\\t\\n\\b\\f\\r')),
            [{'str': '\t\n\b\f\r'}, {'jpath': '\t\n\b\f\r'},
                {'str': '\t\n\b\f\r'}]
        )

    # TODO: MOAR TEST


def main():
    unittest.main()

if __name__ == '__main__':
    main()
