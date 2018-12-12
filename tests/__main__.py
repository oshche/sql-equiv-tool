import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')  # to include parent packages

import unittest
from test1 import *
from test2 import *
from test3 import *


if __name__ == '__main__':
    unittest.main()
