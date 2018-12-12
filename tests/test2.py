from check_equiv import check_equiv

import unittest
from functools import partial
import os
import sys


class Test2(unittest.TestCase):
    def setUp(self):
        self.QueryDir = 'tests/queries/2'

    def test(self):
        with open(self.QueryDir + '/query1.txt', 'r') as f1:
            query1 = f1.read()
        with open(self.QueryDir + '/query2.txt', 'r') as f2:
            query2 = f2.read()

        self.assertRaises(ValueError, partial(check_equiv, query1, query2))


if __name__ == '__main__':
    unittest.main()
