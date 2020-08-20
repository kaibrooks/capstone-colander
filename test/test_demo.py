# test
# kai brooks
# github.com/kaibrooks/capstone-colander

# the codebase is not modular enough to perform automated build testing, but this is

import sys
import unittest
from unittest.mock import patch
sys.path.insert(1, 'src/')
from score import pointsStudentChoice
import load_csv
import pandas as pd

print('\n')

class ScoreTest(unittest.TestCase):
    def testDummy(self):
        self.assertEqual(dummy_fn(2), 4)

    def test_SCO_F001(self):
        load_csv.weightStudentChoice1  = 100
        load_csv.studentID  = [1,2,3]
        load_csv.studentChoiceN = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]], columns=['studentChoice1', 'studentChoice2', 'studentChoice3','studentChoice4','studentChoice5'])
        assignment = [1,1,1,1]
        total = pointsStudentChoice(assignment)
        self.assertEqual(total, 700) #  = 700

# DUMMY FUNCTION
def dummy_fn(theinput):
    return theinput * 2
