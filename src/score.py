# Bliss Brass & Jae Lee
#

import math # ceil()
import load_csv

load_csv.settingsHandler()
load_csv.projectsHandler()
load_csv.studentsHandler()

# Student 0, 1, 2, ..., 8, 9
fauxGA = [0, 0, 0, 0, 1, 1, 1, 1, 10, 10]

def pointsStudentChoice():
    totalPSC = 0
    points_max = 100
    num_projects = 5
    points_max = load_csv.weightStudentChoice1

    #print(load_csv.minTeamSize[3], 'zzz')

    for i in load_csv.studentID:
        if load_csv.studentChoice[i] == fauxGA[i]:
            totalPSC = totalPSC + math.ceil(points_max - (points_max / num_projects) * (fauxGA[i] - 1))
            print(totalPSC, "totalPSC IN LOOP")
            
        else:
            #totalPSC = totalPSC
            print(totalPSC, "totalPSC")

    print('totalPSC =', totalPSC)

    return totalPSC

def pointsESLStudents():
    totalPES = 100
    max_points = load_csv.weightMaxESLStudents / 100
    maxESL = load_csv.maxESLStudents
    dog = load_csv.projectIDs
    v = dog.count(dog)
    print(v, 'v')
    ESL_Group = [0] * 100
    x = 0

    #print(maxESL, max_points, 'max stuff')
    print(ESL_Group, 'ESL_Group')

    for i in load_csv.studentID:
        if load_csv.studentESL[i] == 1:
            print(load_csv.studentESL[i], 'load_csv.studentESL[i]')
            print(ESL_Group[fauxGA[i]], 'faux')
            ESL_Group[fauxGA[i]] = ESL_Group[fauxGA[i]] + 1

            #x += 1
            #if x > load_csv.maxTeamSize
            
            if ESL_Group[fauxGA[i]] > maxESL:
                totalPES = totalPES - (totalPES * max_points)
                print('I was hit!')
    print(ESL_Group, '44')

    return totalPES


def pointsStudentPriority():
    totalPSP = 0

def scoringMode(a):
    print("Hello from a function")
    score = 0

    print(cat)

    score = pointsStudentChoice()
    score += pointsESLStudents()

    print('score =', score)

cat = 'Vera'
scoringMode(cat)


##############################################################################################

# three functions below are parts of the scoring module functions
# tasked for Jaeyoon Lee
# Scoring module shall require data structure from CSV input files
# dataStruct Students {
#   studentID
#	studentChoice[N]
#	studentGPA
#   studentESL
#   studentPriority
#   studentAvoid
# }
#dataStruct Projects {
#	projectID
#	minTeamSize
#	maxTeamSize
#	teamActualSize
# }
#dataStruct Settings {
#	teamSize
#	lowGPAThreshold
#	maxLowGPAStudents
#	maxESLStudents
#	maxRunTime
#	weightMaxLowGPAStudents
#	weightMaxESLStudents
#	weightTeamSize
#	weightStudentPriority
#	weightStudentChoice1
#	weightAvoid
# }

### variables passed when these functions get called
# studentGPA: student GPA from students.csv [float]
# lowGPAThreshold: minimum GPA cutoff from settings.csv [float]
# maxLowGPAStudents: maximum number of students allowed in a group that fail GPA cutoff [int]
# minTeamSize: minimum group size allowed from project.csv [int]
# maxTeamSize: maximum group size allowed from project.csv [int]
# teamSize: desired group size from settings.csv [int]
# studentID: student identifier [int]
# studentAvoid: student to avoid in a group [int]
# weightMaxLowGPAStudents: score from settings.csv [int]
# weightTeamSize: score from settings.csv [int]
# weightAvoid: score from settings.csv [int]
###


### sample variables and values
#studentID = [1,2,3,4,5,6,7,8,9,10]  # students from 1 to 10
#studentGPA = [3.00,2.99,2.88,2.77,2.66,2.55,2.44,2.33,2.22,2.11]    # student GPAs for 1 to 10
#studentESL = [0,0,1,0,1,0,0,0,1,0]  # students 3, 5, and 9 are ESL students
#studentESL = [3,5,9]    # students 3, 5, and 9 are ESL students
#studentChoice = [1,2,3,1,2,3,1,2,3,1] # student project choice
#studentPriority = [0,0,0,0,1,0,0,0,0,1] # student priority flag
#studentPriority = [5,10] # student priority flag
#studentAvoid = [,3,2,,,,,,3,9] # student avoid choice
#projectID = [1,2,3] # project numbers
#minTeamSize = [2,2,3] # min group size for each project
#maxTeamSize = [4,4,5] # max grou psize for each project
#teamSize = [4,3,3] # group size desired by user
#lowGPAThreshold = [2.40] # min GPA cutoff
#maxLowGPAStudents = [2] # min GPA cutoff students limit
#maxESLStudents = [2] # ESL student limit
#maxRunTime = [30] # program max run time
#studentAssignments = [1,1,2,2,3,3,1,2,1,2]

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
#def pointMaxLowGPAStudents(studentGPA, lowGPAThreshold, maxLowGPAStudents, weightMaxLowGPAStudents)
    # Look at assignments column
    # Check studentGPA and check lowGPAThreshold
    # Count student[i] that studentGPA < lowGPAThreshold
    # if student[i] < maxLowGPAStudents
        # then weightMaxLowGPAStudents += 50
        # else weightMaxLowGPAStudents += 0
    #return weightMaxLowGPAStudents

# This calculates bonus points for having met group size constraints
#def pointsTeamSize(minTeamSize, maxTeamSize, teamSize, weightTeamSize)
    # Look at assignments column
    # Count projectStudent[i] in each projectID
    #for 
    # if minTeamSize < projectStudent[i] < maxTeamSize
        # then weightTeamsize += 50
        # else weightTeamsize += 0
    # if projectStudents[i] == teamSize
        # then weightTeamSize += 50
        # else weightTeamSize += 0
    # else
        # weightTeamSize += 0
    #return weightTeamSize

# This calculates bonus for not violating student disallowance constraint
#def pointsAvoid(studentID, studentAvoid, weightAvoid)
    # Look at assignments column
    # Check studentAvoid for each studentID
    # Check if studentAvoid == studentID within the same projectID
    # if studentID == studentAvoid
        # then weightAvoid += 0
    # else if studentID != studentAvoid for any studentID in same projectID
        # then weightAvoid += 100
    #return weightAvoid