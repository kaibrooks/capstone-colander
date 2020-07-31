# Bliss Brass & Jae Lee

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

# sample local variables and values
studentID = [1,2,3,4,5,6,7,8,9,10]  # students from 1 to 10
studentGPA = [3.00,2.99,2.88,2.77,2.66,2.55,2.44,2.33,2.22,2.11]    # student GPAs for 1 to 10
studentESL1 = [0,0,1,0,1,0,0,0,1,0]  # students 3, 5, and 9 are ESL students one way to read it
studentESL2 = [3,5,9]    # students 3, 5, and 9 are ESL students the other way to read it
studentChoice = [1,2,3,1,2,3,1,2,3,1] # student project choice
studentPriority1 = [0,0,0,0,1,0,0,0,0,1] # student priority flag one way to read it
studentPriority2 = [5,10] # student priority flag the other way to read it
studentAvoid = ['blank',3,2,'blank','blank','blank','blank','blank',3,9] # student avoid choice
projectID = [1,2,3] # project numbers 1 to 3
minTeamSize = [2,2,3] # min group size for each project for projects 1 to 3
maxTeamSize = [4,4,5] # max grou psize for each project for projects 1 to 3
min_teamSize = [2,2,2] # min group size desired by user for projects 1 to 3
max_teamSize = [4,4,5] # max group size dsired by user for projects 1 to 3
lowGPAThreshold = 2.40 # min GPA cutoff
maxLowGPAStudents = 2 # min GPA cutoff students limit is 2 students
maxESLStudents = 2 # ESL student limit is 2 students
maxRunTime = 30 # program max run time is 30 min (not important)
studentAssignments = [1,1,2,2,3,3,1,2,1,2] # GA assignments for student 1 to 10
group_size = [4,4,2]
weightMaxLowGPAStudents = 100
weightMaxESLStudents    = 75
weightTeamSize          = 50
weightStudentPriority   = 100
weightStudentChoice1    = 75
weightAvoid             = 60

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointMaxLowGPAStudents():
    points = 0
    # Look at assignments column
    # Check studentGPA and check lowGPAThreshold
    # Count student[i] that studentGPA < lowGPAThreshold
    # if student[i] < maxLowGPAStudents
    print(lowGPAThreshold, 'min GPA cutoff')
    print(maxLowGPAStudents, 'max students with min GPA in a group')
    for studentID[i] in score:
        if studentGPA[float] < lowGPAThreshold[float]:
            if studentID[i] < maxLowGPAStudents
                points += weightMaxLowGPAStudents
                print(points, 'total score =')
            else:
                pass
        # then weightMaxLowGPAStudents += 50
        # else weightMaxLowGPAStudents += 0
    return points

# This calculates bonus points for having met group size constraints
def pointsTeamSize():
    # Look at assignments column
    # Count projectStudent[i] in each projectID
    # if minTeamSize < projectStudent[i] < maxTeamSize
    points = 0
    for i in score:
    print(minTeamSize[i], 'minTeamSize')
    print(maxTeamSize[i], 'maxTeamSize')
    print(group_Size[i], 'group size')
        if minTeamsize[i] < group_size[i] < maxTeamSize[i]:
        # then weightTeamsize += 50
        # else weightTeamsize += 0
            points += weightTeamSize
            print(points, 'total points =')
        # if a project does not have min and max TeamSize values, then default to settings.csv teamSize
        else min_temaSize[i] < group_size[i] < max_teamSize[i]:
             points += weightTeamSize
             print(points, 'total points =')
    return points

# This calculates bonus for not violating student disallowance constraint
def pointsAvoid():
    # Look at assignments column
    # Check studentAvoid for each studentID
    # Check if studentAvoid == studentID within the same projectID
    # if studentID == studentAvoid
        # then weightAvoid += 0
    points = 0
    for i in studentAssignments:
    if studnetID[i] == studnetAvoid[i]
        points += 0
        print(points, 'total points =')
    # else if studentID != studentAvoid for any studentID in same projectID
        # then weightAvoid += 100
    else:
        points += weightAvoid
        print(points, 'total points =')
    return points