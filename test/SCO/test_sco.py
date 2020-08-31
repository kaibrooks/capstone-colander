# run scoring tests
# kai brooks
# github.com/kaibrooks

import sys
import unittest
from unittest.mock import patch
sys.path.insert(1, 'src/') # look for imports in the project root
from score import pointsStudentChoice, pointsESLStudents, pointsStudentPriority, pointsMaxLowGPAStudents, pointsTeamSize, pointsAvoid
import load_csv
import pandas as pd

class ScoreTest(unittest.TestCase):
    def setUp(self): # use these for all tests unless re-defined in the test def
        load_csv.studentID  = [1,2,3,4]
        load_csv.studentChoiceN = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]], columns=['studentChoice1', 'studentChoice2', 'studentChoice3','studentChoice4','studentChoice5'])
        load_csv.projectIDs = [1,2,3,4,5,6]
        
        load_csv.minTeamSize = [1,1,1,1,1,1]
        load_csv.maxTeamSize = [10,10,10,10,10,10]

        load_csv.weightTeamSize = 100
        load_csv.weightStudentChoice1  = 100
        self.assignment = [1,1,1,1]

    def test_SCO_F001_studentChoice(self): # student choice
        self.assertEqual(pointsStudentChoice(self.assignment), 400) #  = 400

    def test_SCO_F001_teamSize(self): # group size
        self.assertEqual(pointsTeamSize(self.assignment), 100) #  = 100

    def test_SCO_F002_studentChoice(self):
        load_csv.studentChoiceN = pd.DataFrame([[1,None,None,None,None],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]], columns=['studentChoice1', 'studentChoice2', 'studentChoice3','studentChoice4','studentChoice5'])
        self.assignment = [2,2,2,2]
        self.assertEqual(pointsStudentChoice(self.assignment), 400) #  = 400

    def test_SCO_F003_studentChoice(self):
        load_csv.studentChoiceN = pd.DataFrame([[1,2,3,4,5]], columns=['studentChoice1', 'studentChoice2', 'studentChoice3','studentChoice4','studentChoice5'])
        self.assignment = [6]
        self.assertEqual(pointsStudentChoice(self.assignment), 0) #  = 0