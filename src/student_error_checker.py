import sys
import pandas as pd

def studentsHandler(studentsFile):

    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    #global studentChoiceN
    #global studentAvoidN

    #flags to indicate that optional headers have been included default False
    #colPriority = False
    #colAvoid = False

    #load students csv file
    studentsFileData = pd.read_csv(studentsFile)

    # debug print to verify data has been loaded
    print(studentsFileData)

    ######Store Data#######
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].copy()
    studentPriority = studentsFileData['studentPriority'].copy()

    #debug print to verify studentID has been stored
    print("Student ID Array Test")
    print(studentID)

    


    ########################Validate Data######################
    #########################UNFINISHED########################
    # verify all column headers are present in students csv file
    #studentsColumns = ['studentID', 'studentChoice1', 'studentGPA']
    #for col in studentsColumns:
    #    if col not in studentsFileData.columns:
    #        sys.exit("ERROR: Required {0} column header not found in the students csv file. Terminating Program.".format(col))

    # look for optional column headers in students csv file
    #if 'studentPriority' not in studentsFileData.columns:
    #    print("Warning: studentPriority column header not found in the students csv file.")
    #else:
        #set colPriority flag to true
    #    colPriority = True
        #debug print
    #    print("Priority Flag column found")

    #if 'studentAvoid1' not in studentsFileData.columns:
    #    print("Warning: studentAvoid1 column header not found in the students csv file. No avoids will be considered for the solution.")
    #else:
        #set colAvoid flag to true
    #    colAvoid = True
        #debug print
    #    print("Avoid1 Flag column found")

    

    #Create a series to indicate datatypes of each column
    #studentDTypes = studentsFileData['studentID'].dtype
    #studentDTypes = studentsFileData.dtype

    #debug print to verify datatype series is correct
    #print(studentDTypes)

    #Validate only integers are present in studentID
    #if studentsFileData['studentID'].dtype != np.int64
    #    print('studentID incorrect ')        
    #else:
    #    sys.exit("ERROR: Unexpected data type found in studentID. Terminating Program.")
    #Validate only integers are present in studenChoice1
    #if studentDTypes['studentChoice1'] != 'int64'
    #    sys.exit("ERROR: Unexpected data type found in studentChoice1. Terminating Program.")
    #Validate only floats are present in studentID
    #if studentDTypes['studentGPA'] != 'float64'
    #    sys.exit("ERROR: Unexpected data type found in studentGPA. Terminating Program.")

    # if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
    ## REVIEW (maybe use for esl/priority flags?)
    #projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(42)  # 42 needs to be changed to settings.csv value
    #minTeamSize = int_checker('minTeamSize')
    #projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(42)
    #maxTeamSize = int_checker('maxTeamSize')



