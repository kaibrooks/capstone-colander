# check if debug mode is on
# kai brooks
# github.com/kaibrooks

import sys
import unittest
sys.path.insert(1, 'src/') # look for imports in the project root
from prints import check_debug

class debugModeTest(unittest.TestCase):
    def test_debug_is_off(self):
        self.assertEqual(check_debug(), False) #  = false for prod