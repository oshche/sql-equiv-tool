from check_equiv import check_equiv

import unittest
import os
import sys


class Test1(unittest.TestCase):
    def setUp(self):
        self.QueryDir = 'tests/queries/1'

    def test(self):
        with open(self.QueryDir + '/query1.txt', 'r') as f1:
            query1 = f1.read()
        with open(self.QueryDir + '/query2.txt', 'r') as f2:
            query2 = f2.read()

        queries_are_equiv, msg = check_equiv(query1, query2)
        self.assertTrue(queries_are_equiv)


if __name__ == '__main__':
    unittest.main()
