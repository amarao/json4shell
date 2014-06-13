#!/usr/bin/env python
#iterate_array

import unittest
from bin.lib import jsoniter
import json


class iterate_array_tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array([], 0, None)],
            []
        )

    def test_simple_no_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 0, None)],
            [['1', '2', '3']]
        )

    def test_types(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 'a2', True, False], 0, None)],
            [['1', 'a2', 'True', 'False']]
        )

    def test_simple_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3, 4], 2, None)],
            [['1', '2'], ['3', '4']]
        )

    def test_simple_uneven_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 2, None)],
            [['1', '2'], ['3']]
        )

    def test_simple_overlimit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 4, None)],
            [['1', '2', '3']]
        )

    def test_depth_no_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 0, 'depth')],
            [['1', '2', '3', '4', '5', '6', '7']]
        )

    def test_depth_uneven_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 3, 'depth')],
            [['1', '2', '3'], ['4', '5', '6'], ['7']]
        )

    def test_width_no_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 0, 'width')],
            [['1', '2', '3', '4', '7', '5', '6']]
        )

    def test_width_uneven_limit(self):
        self.assertEqual(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 3, 'width')],
            [['1', '2', '3'], ['4', '7', '5'], ['6']]
        )

        # TODO
        #  No exception testing (no normal exception in code!)


class SplitOnQueriesTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            [x for x in jsoniter.split_on_queries('')],
            []
        )

    def test_simple(self):
        self.assertEqual(
            [x for x in jsoniter.split_on_queries('a')],
            [{'str': 'a'}]
        )

    def test_one(self):
        self.assertEqual(
            [x for x in jsoniter.split_on_queries('{query}')],
            [{'jpath': 'query'}]
        )

    def test_escaping(self):
        self.assertEqual(
            [x for x in jsoniter.split_on_queries('\\\\\\{\\a\}')],
            [{'str': '\\{a}'}]
        )

    def test_complex(self):
        self.assertEqual(
            [x for x in jsoniter.split_on_queries(
                '\\\\_#{$~}-!("){}a1@*{\\\\}')],
            [
                {'str': '\\_#'}, {'jpath': '$~'},
                {'str': '-!(")'}, {'jpath': ''},
                {'str': 'a1@*'}, {'jpath': '\\\\'}
            ]
        )


class MakeQueriesTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries([], [])],
            []
        )

    def test_simple(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries([{'str': 'a'}], [])],
            ['a']
        )

    def test_empty_query(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries([{'jpath': ''}], '')],
            ['']
        )

    def test_simple_dict(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries([{'jpath': 'a'}], {'a': 'foo'})],
            ['foo']
        )

    def test_mixed(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries(
                [   # input args
                    {'str': 'a'},
                    {'jpath': '.one'},
                    {'str': 'b'},
                    {'jpath': 'two'}
                ],
                # json to substitute
                {'one': '1', 'two': 2}  # note 2 is int, not str
            )],
            ['a', '1', 'b', '2']  # result
        )

    def test_complex(self):
        self.assertEqual(
            [x for x in jsoniter.make_queries(
                [   # input args
                    {'str': 'su'},
                    {'jpath': '[1].two'},
                    {'jpath': '[3].four.five[6]'}
                ],
                #json to substitute
                [
                    'ignore0',
                    {'two': 'ccee'},
                    'ignore2',
                    {
                        'four': {
                            'five': [
                                'ign0',
                                'ign1',
                                'ign2',
                                'ign3',
                                'ign4',
                                'ign5',
                                'ss'
                            ]
                        }
                    }
                ]
            )],
            ['su', 'ccee', 'ss']
        )


def main():
    unittest.main()

if __name__ == '__main__':
    main()
