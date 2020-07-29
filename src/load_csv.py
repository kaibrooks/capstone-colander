
def projectsHandler():
	global minTeamSize
	global maxTeamSize
	global projectIDs

	projectIDs  = [1, 2, 10, 11, 100, 101, 102, 110, 111, 200]
	minTeamSize = [4, 4, 4, 3, 4, 3, 3, 3, 4, 3]
	maxTeamSize = [5, 4, 7, 4, 4, 5, 6, 4, 5, 5]


def settingsHandler():
    global weightMaxLowGPAStudents
    global weightMaxESLStudents
    global weightTeamSize
    global weightStudentPriority
    global weightStudentChoice1
    global weightAvoid
    global maxLowGPAStudents
    global maxESLStudents
    global lowGPAThreshold

    maxESLStudents          = 2
    lowGPAThreshold         = 2.75
    maxLowGPAStudents       = 2
    weightMaxLowGPAStudents = 100
    weightMaxESLStudents    = 75
    weightTeamSize          = 50
    weightStudentPriority   = 100
    weightStudentChoice1    = 75
    weightAvoid             = 60

def studentsHandler():
    global studentID
    global studentGPA
    global studentESL
    global studentChoice
    global studentPriority
    global studentAvoid1

    studentID = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    studentGPA = [2.5, 2.5, 2.5, 2.5, 3.5, 4.0, 4.0, 2.0, 2.0, 1.0]
    studentESL = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    studentChoice = [0, 0, 0, 0, 1, 2, 4, 4, 11, 100]
    studentPriority = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
    studentAvoid = ["Blank", "Blank", "Blank", 4, 3, "Blank", 1, "Blank", "Blank", "Blank"]