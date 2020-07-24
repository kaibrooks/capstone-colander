# points calculation for capstone-colander
# github.com/kaibrooks/capstone-colander

import math # ceil()

def points( assignment_choice, num_projects, points_max ):
   
    if assignment_choice > num_projects:
        exit('Error: assignment choice doesn\'t exist')
        # in reality this zeroes the entire solutions score and moves on to the next one
        # but that code isn't implemented yet
        print('You shouldn\'t see this if the program exited correctly')
    elif assignment_choice == 0: # if a studen't didn't get any of their choices
        total = 0
    else: 
        total = math.ceil( points_max - (points_max / num_projects)*(assignment_choice - 1) )
    return total

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

###
# sample variables and values
studentID = [1,2,3,4,5,6,7,8,9,10]  # students from 1 to 10
studentGPA = [3.00,2.99,2.88,2.77,2.66,2.55,2.44,2.33,2.22,2.11]    # student GPAs for 1 to 10
studentESL = [0,0,1,0,1,0,0,0,1,0]  # students 3, 5, and 9 are ESL students
studentESL = [3,5,9]    # students 3, 5, and 9 are ESL students
studentChoice = [1,2,3,1,2,3,1,2,3,1] # student project choice
studentPriority = [0,0,0,0,1,0,0,0,0,1] # student priority flag
studentPriority = [5,10] # student priority flag
studentAvoid = [,3,2,,,,,,3,9] # student avoid choice
projectID = [1,2,3] # project numbers
minTeamSize = [2,2,3] # min group size for each project
maxTeamSize = [4,4,5] # max grou psize for each project
teamSize = [4,3,3] # group size desired by user
lowGPAThreshold = [2.40] # min GPA cutoff
maxLowGPAStudents = [2] # min GPA cutoff students limit
maxESLStudents = [2] # ESL student limit
maxRunTime = [30] # program max run time
studentAssignments = [1,1,2,2,3,3,1,2,1,2]

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointMaxLowGPAStudents(studentGPA, lowGPAThreshold, maxLowGPAStudents, weightMaxLowGPAStudents)
    # Look at assignments column
    # Check studentGPA and check lowGPAThreshold
    # Count student[i] that studentGPA < lowGPAThreshold
    # if student[i] < maxLowGPAStudents
        # then weightMaxLowGPAStudents += 50
        # else weightMaxLowGPAStudents += 0
    return weightMaxLowGPAStudents

# This calculates bonus points for having met group size constraints
def pointsTeamSize(minTeamSize, maxTeamSize, teamSize, weightTeamSize)
    # Look at assignments column
    # Count projectStudent[i] in each projectID
    for 
    # if minTeamSize < projectStudent[i] < maxTeamSize
        # then weightTeamsize += 50
        # else weightTeamsize += 0
    # if projectStudents[i] == teamSize
        # then weightTeamSize += 50
        # else weightTeamSize += 0
    # else
        # weightTeamSize += 0
    return weightTeamSize

# This calculates bonus for not violating student disallowance constraint
def pointsAvoid(studentID, studentAvoid, weightAvoid)
    # Look at assignments column
    # Check studentAvoid for each studentID
    # Check if studentAvoid == studentID within the same projectID
    # if studentID == studentAvoid
        # then weightAvoid += 0
    # else if studentID != studentAvoid for any studentID in same projectID
        # then weightAvoid += 100
    return weightAvoid