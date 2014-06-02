#!/usr/bin/python
import unittest
import jsonops
import json


class Array_slice_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.array_slice([], ["[1:2]"]) == [])

    def test_one(self):
        self.failUnless(jsonops.array_slice([1], ["[0:1]"]) == [1])

    def test_normal_slice(self):
        self.failUnless(jsonops.array_slice(range(10), ["[3:5]"]) == [3, 4])

    def test_reverse_range(self):
        self.failUnless(jsonops.array_slice(range(10), ["[9:1]"]) == [])


class Array_head_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.array_head([], ["1"]) == [])

    def test_one(self):
        self.failUnless(jsonops.array_head([1], ["1"]) == [1])

    def test_normal(self):
        self.failUnless(jsonops.array_head(range(9), ["3"]) == [0, 1, 2])

    def test_out_of_range(self):
        self.failUnless(jsonops.array_head(range(3), ["11"]) == [0, 1, 2])


class Array_tail_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.array_tail([], ["1"]) == [])

    def test_one(self):
        self.failUnless(jsonops.array_tail([1], ["0"]) == [1])

    def test_normal(self):
        self.failUnless(jsonops.array_tail(range(9), ["7"]) == [7, 8])

    def test_out_of_range(self):
        self.failUnless(jsonops.array_tail(range(3), ["7"]) == [])


class Object_get_tests(unittest.TestCase):
    def test_strings(self):
        self.failUnless(jsonops.object_get({"f": "b", "z": "q"}, ["z"]) == "q")


class Object_keys_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.object_keys({}, []) == [])

    def test_normal(self):
        self.failUnless(
            jsonops.object_keys({"1": "a", "2": "b"}, []) == ["1", "2"]
        )


class Object_values_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.object_values({}, []) == [])

    def test_normal(self):
        self.failUnless(
            jsonops.object_values({"1": "a", "2": "b"}, []) == ["a", "b"]
        )


class Object_values_tests(unittest.TestCase):
    def test_empty(self):
        self.failUnless(jsonops.array_enumerate([], ["4"]) == {})

    def test_normal(self):
        self.failUnless(
            jsonops.array_enumerate({"a", "b"}, ["4"]) == {4: "a", 5: "b"}
        )


def main():
    unittest.main()

if __name__ == '__main__':
    main()
