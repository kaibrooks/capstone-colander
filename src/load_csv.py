import sys
import pandas as pd

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
    weightStudentChoice1    = 100
    weightAvoid             = 60

def studentsHandler(studentsFile):
    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentChoiceN
    global studentAvoidN
    global assignment

    #flags to indicate that optional headers have been included default False
    #colPriority = False
    #colAvoid = False

    #load students csv file
    studentsFileData = pd.read_csv(studentsFile)

    # debug print to verify data has been loaded
    #print(studentsFileData)


    #Move studentChoices into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentChoice' in col] # get columns named 'studentChoice'
    studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just choices

    #Move studentAvoid into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentAvoid' in col] # get columns named 'studentAvoid'
    studentAvoidN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just avoidances

    #print("student avoidances")
    #print(studentAvoidN)

    

    ######Store Data#######
    # Store single column data
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].copy()
    studentPriority = studentsFileData['studentPriority'].copy()
    assignment = studentsFileData['Assignment'].copy()


'''def studentsHandler():
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
<<<<<<< HEAD
    studentAvoid = ["Blank", "Blank", "Blank", 4, 3, "Blank", 1, "Blank", "Blank", "Blank"]'''
=======
    studentAvoid1 = ["Blank", "Blank", "Blank", 4, 3, "Blank", 1, "Blank", "Blank", "Blank"]

    #fauxGA = [0, 0, 0, 0, 1, 1, 1, 1, 9, 9]
>>>>>>> e6e06533e2ffec70e5bbe166a5284876705a5929
