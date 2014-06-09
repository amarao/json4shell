#!/usr/bin/env python
#iterate_array

import unittest
from bin.lib import jsoniter
import json


class iterate_array_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array([], 0, None)] == []
        )

    def test_simple_no_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 0, None)] ==
            [['1', '2', '3']]
        )

    def test_types(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 'a2', True, False], 0, None)] ==
            [['1', 'a2', 'True', 'False']]
        )

    def test_simple_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3, 4], 2, None)] ==
            [['1', '2'], ['3', '4']]
        )

    def test_simple_uneven_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 2, None)] ==
            [['1', '2'], ['3']]
        )

    def test_simple_overlimit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, 3], 4, None)] ==
            [['1', '2', '3']]
        )

    def test_depth_no_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 0, 'depth')] ==
            [['1', '2', '3', '4', '5', '6', '7']]
        )

    def test_depth_uneven_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 3, 'depth')] ==
            [['1', '2', '3'], ['4', '5', '6'], ['7']]
        )

    def test_width_no_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 0, 'width')] ==
            [['1', '2', '3', '4', '7', '5', '6']]
        )

    def test_width_uneven_limit(self):
        self.failUnless(
            [x for x in jsoniter.iterate_array(
                [1, 2, [3, 4, [5, 6], 7]], 3, 'width')] ==
            [['1', '2', '3'], ['4', '7', '5'], ['6']]
        )

        # TODO
        #  No exception testing (no normal exception in code!)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
