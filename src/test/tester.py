# Bliss Brass
#for variable_name in range(start, stop, step)

from array import *
import struct
import math

# var = struct.pack('hhl',1,2,3) 
#Projects = struct.pack('iii', )
#Students = struct.pack('if?ifi', )
#rows, cols = (5, 5)

class Students:
    "Stores name and place pairs"

    # This creates a class variable shared among all instances of this class
    #kind = 'canine'

    # This creates variables specific to an instance of this class
    def __init__(self, studentID, studentGPA, studentESL, studentChoice1, studentPriority, studentAvoid1, studentAssignment):
        self.studentID = studentID
        self.studentGPA = studentGPA
        self.studentESL = studentESL
        self.studentChoice1 = studentChoice1
        self.studentPriority = studentPriority
        self.studentAvoid1 = studentAvoid1
        self.studentAssignment = studentAssignment

class Projects:
    "Stores Project information"

    def __init__(self, projectID, minTeamSize, maxTeamSize, teamActualSize):
        self.projectID = projectID
        self.minTeamSize = minTeamSize
        self.maxTeamSize = maxTeamSize
        self.teamActualSize = teamActualSize

class Settings:
    "Data structure for user settings"

    #def __init__(self, weightStudentChoice1):
    weightStudentChoice1 = 100



people = []

people.append(Students(0, 2.00, 0, 0, 0, 'Blank', 0)) # Low GPA test case
people.append(Students(1, 3.00, 1, 0, 0, "Blank", 1)) # ESL test case
people.append(Students(2, 2.75, 0, 1, 1, "Blank", 1)) # Priority student test case
people.append(Students(3, 2.50, 0, 4, 1, 2, 4)) # General avoidance test case
people.append(Students(4, 4.00, 1, 3, 0, 5, 3)) # Mutual avoidance test case
people.append(Students(5, 3.00, 0, 3, 0, 4, 3)) # Mutual avoidance test case
people.append(Students(6, 2.50, 0, 0, 0, "Blank", 4))

projectList = []
settingsList = []

#settingsList.append(Settings(10)) #Dummy weight for StudentChoice1
#Settings.weightStudentChoice1 = 50

#dataStructure = [[Projects() for i in range(cols)] for j in range(rows)] 
#segmentList = [Segment() for i in range(10)]
# Declaring a 2D array and initializing its elements to 0
#dataStructure = [[0 for i in range(cols)] for j in range(rows)] 

def pointsStudentChoice(people, projectList, settingsList):
    totalPSC = 0
    points_max = 0
    num_projects = 5
    #assignment_choice = 1
    print(points_max)
    points_max = Settings.weightStudentChoice1

    print(points_max)

    Settings.weightStudentChoice1 = 50
    points_max = Settings.weightStudentChoice1

    print(points_max)

    for data in people:
        if data.studentChoice1 == data.studentAssignment:
            #totalPSC = totalPSC + 5 * settingsList.
            totalPSC = math.ceil(points_max - (points_max / num_projects) * (data.studentAssignment - 1))
        else:
            totalPSC = totalPSC

    print('totalPSC =', totalPSC)

    return totalPSC

def scoringMode(people, projectList, settingsList, a):
    print("Hello from a function")

    score = 0
    
    #dataStructure[0][0] = 1
    for data in people:
        print(data.studentID, data.studentGPA, data.studentESL, data.studentChoice1, data.studentPriority, data.studentAvoid1) 
    print(cat)

    score = pointsStudentChoice(people, projectList, settingsList)

    print('score =', score)

cat = 'Vera'
scoringMode(people, projectList, settingsList, cat)
