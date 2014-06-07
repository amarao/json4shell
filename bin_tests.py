#!/usr/bin/env python

import subprocess
import unittest

from bin.lib import jsonops


def exec_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).stdout.read()


def retcode_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).wait()


class json_array_enum_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-enum'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-enum')),
            {"0": 1, "1": 2, "2": 3})

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[\\"foo\\",1,2,3]" | ./bin/json-array-enum')),
            {"0": "foo", "1": 1, "2": 2, "3": 3})

    def test_with_cnt(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-enum -c 1')),
            {"1": 1, "2": 2, "3": 3})

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[\\"foo\\",1,2,3]" | ./bin/json-array-enum -c 2')),
            {"2": "foo", "3": 1, "4": 2, "5": 3})


class json_array_get_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-get 0'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1,2,3]" | ./bin/json-array-get'), 0)

    def test_array(self):
        self.assertEqual(
            exec_cmd('echo "[1,2,3]" | ./bin/json-array-get 1'),
            '2\n')

        self.assertEqual(
            exec_cmd('echo "[\\"bar\\",2,3]" | ./bin/json-array-get 0'),
            '"bar"\n')

class json_array_slice_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-slice'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1,2,3]" | ./bin/json-array-slice'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1,2,3]" | ./bin/json-array-slice 1'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-slice 1 1')),
            [])

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-slice 1 2')),
            [2])

class json_array_head_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-head'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-head 1'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1,2,3]" | ./bin/json-array-head'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-head 0')),
            [])

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-head 2')),
            [1,2])

class json_array_tail_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-tail'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-tail 1'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1,2,3]" | ./bin/json-array-tail'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-tail 3')),
            [])

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-tail 1')),
            [2,3])


class json_array_shuffle_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-shuffle'), 0)

    def test_array(self):
        self.assertEqual(
            len(jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-shuffle'))),
            3)

class json_array_sort_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-sort'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-sort')),
            [3,2,1])

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,3]" | ./bin/json-array-sort -r')),
            [1,2,3])


class json_array_uniq_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-array-uniq'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[1,2,2,2,3,3,3]" | ./bin/json-array-uniq')),
            [1,2,3])

class json_object_get_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-object-get'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "{\\"foo\\":\\"bar\\"}" | ./bin/json-object-get'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-object-get foo'), 0)

    def test_array(self):

        self.assertEqual(
            exec_cmd('echo "{\\"foo\\":\\"bar\\"}" | ./bin/json-object-get foo'),
            '"bar"\n')

        self.assertEqual(
            exec_cmd('echo "{\\"foo\\":1}" | ./bin/json-object-get foo'),
            '1\n')


class json_object_keys_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-object-keys'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "{\\"foo\\":\\"bar\\"}" | ./bin/json-object-keys')),
            ["foo"])

        self.assertEqual(
            len(jsonops.load_json(exec_cmd('echo "{\\"0\\":\\"1\\", \\"1\\":\\"2\\"}" | ./bin/json-object-keys'))),
            2)

class json_object_values_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-object-values'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "{\\"foo\\":\\"bar\\"}" | ./bin/json-object-values')),
            ["bar"])

        self.assertEqual(
            len(jsonops.load_json(exec_cmd('echo "{\\"0\\":\\"1\\", \\"1\\":\\"2\\"}" | ./bin/json-object-values'))),
            2)

class json_print_tests(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(
            retcode_cmd('echo "" | ./bin/json-print'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "foo" | ./bin/json-print'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "[1" | ./bin/json-print'), 0)

        self.assertNotEqual(
            retcode_cmd('echo "{\\"foo\\":\\"bar\\"" | ./bin/json-print'), 0)

    def test_array(self):
        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "{\\"foo\\":\\"bar\\"}" | ./bin/json-print')),
            {"foo":"bar"})

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "{\\"0\\":\\"1\\", \\"1\\":\\"2\\"}" | ./bin/json-print')),
            {"0":"1", "1":"2"})

        self.assertEqual(
            jsonops.load_json(exec_cmd('echo "[0,\\"1\\",\\"foo\\",\\"3\\", null]" | ./bin/json-print')),
            [0, "1", "foo", "3", None])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
