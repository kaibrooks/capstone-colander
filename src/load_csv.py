# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import sys
import pandas as pd
import prints
#For studentsHandler()
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype


def projectsHandler(projectsFileData):
    global minTeamSize
    global maxTeamSize
    global projectIDs

    # verify required project csv headers are present
    projectsColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
    for col in projectsColumns:
        if col not in projectsFileData.columns:
            sys.exit("ERROR: Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

    # function to verify that all require values in projects csv file are integers within the required range
    def int_checker_projects(columnName):

        tempArray = []
        for value in projectsFileData[columnName]:
            if isinstance(value, object):
                try:
                    value = float(value)
                except ValueError:
                    sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
            if isinstance(value, float):
                if value.is_integer():
                    value = int(value)
            if isinstance(value, int):
                if (value < 1) or (value > pow(2, 64)):
                    sys.exit("ERROR: Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, columnName))
                tempArray.append(value)
            else:
                sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
        return tempArray

    # verify that all values in program csv file are integers
    projectIDs = int_checker_projects('projectID')

    # verify that there are no duplicate project IDs in the projectID column
    if projectsFileData.projectID.duplicated().any():
        sys.exit("ERROR: projectid {0} is a duplicate projectID in the csv file. Terminating Program.".format({projectsFileData[projectsFileData.projectID.duplicated()].projectID.iloc[0]}))

    # if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
    projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(defaultMinTeamSize)
    print(projectsFileData)
    minTeamSize = int_checker_projects('minTeamSize')
    projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(defaultMaxTeamSize)
    print(projectsFileData)
    maxTeamSize = int_checker_projects('maxTeamSize')

    # verify minTeamSize is not greater than maxTeamSize
    for min,max,pid in zip(minTeamSize,maxTeamSize,projectIDs):
        if min > max:
            sys.exit("ERROR: minTeamSize is greater than maxTeamSize for projectID {0}.".format(pid))

    # warn user if gap found in projectID sequence that starts a projectID '1'
    projectIDGap = projectIDs[-1]*(projectIDs[-1] + projectIDs[0]) / 2 - sum(projectIDs)
    if projectIDGap > 0:
        print("\nWARNING: gap found in projectID sequence in the projects csv file.")


def settingsHandler(settingsFileData):
    global weightMaxLowGPAStudents
    global weightMaxESLStudents
    global weightTeamSize
    global weightStudentPriority
    global weightStudentChoice1
    global weightAvoid
    global maxRunTime
    global defaultMaxTeamSize
    global defaultMinTeamSize
    global maxLowGPAStudents
    global maxESLStudents
    global lowGPAThreshold

    # verify required settings csv headers are present
    settingsColumns = ['name', 'min', 'max', 'points']
    for col in settingsColumns:
        if col not in settingsFileData.columns:
            sys.exit("ERROR: Required {0} column header not found in the settings csv file. Terminating Program.".format(col))

    # verify required settings csv rows are present
    settingsRows = ['teamSize', 'lowGPAThreshold', 'maxLowGPAStudents', 'maxESLStudents', 'maxRunTime', 'weightMaxLowGPAStudents',
                       'weightMaxESLStudents', 'weightTeamSize', 'weightStudentPriority', 'weightStudentChoice1', 'weightAvoid']
    for row in settingsRows:
        if row not in settingsFileData['name'].values:
            sys.exit("ERROR: Required {0} row 'name' not found in the settings csv file. Terminating Program.".format(row))

    # function to verify values in the csv file are integers.
    def int_checker_settings(value, rowName, minValue):

        if isinstance(value, int):
            if (value < minValue) or (value > pow(2, 64)):
                 sys.exit("ERROR: Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
            return value

        # function to verify integer if data type of value is not originally set as int (dtype could be obj or float)
        def is_integer_settings(value, rowName, minValue):
            if value.is_integer():
                tempInt = int(value)
                if (tempInt < minValue) or (tempInt > pow(2, 64)):
                    sys.exit("ERROR: Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
                return tempInt
            else:
                sys.exit("ERROR: {0} in the {1} row is not an integer. Terminating Program.".format(value, rowName))

        # if pandas set column data type to float
        # this would happen when there are only floats or empty fields found in the column
        if isinstance(value, float):
            return is_integer_settings(value, rowName, minValue)

        # if pandas set column data type to a python object
        # this would happen when there are strings found in the column
        if isinstance(value, object):
            try:
                tempInt = float(value)
            except ValueError:
                sys.exit("ERROR: {0} in the {1} row is not an integer. Terminating Program.".format(value, rowName))
            return is_integer_settings(tempInt, rowName, minValue)


    # verify required values in 'points' column are integers
    # if they are, assign value to global variable for scoring function to use
    weightMaxLowGPAStudents = int_checker_settings(
        (settingsFileData.set_index('name').at['weightMaxLowGPAStudents', 'points']), 'weightMaxLowGPAStudents', 0)
    weightMaxESLStudents = int_checker_settings(
        (settingsFileData.set_index('name').at['weightMaxESLStudents', 'points']), 'weightMaxESLStudents', 0)
    weightTeamSize = int_checker_settings(
        (settingsFileData.set_index('name').at['weightTeamSize', 'points']), 'weightTeamSize', 0)
    weightStudentPriority = int_checker_settings(
        (settingsFileData.set_index('name').at['weightStudentPriority', 'points']), 'weightStudentPriority', 0)
    weightStudentChoice1 = int_checker_settings(
        (settingsFileData.set_index('name').at['weightStudentChoice1', 'points']), 'weightStudentChoice1', 0)
    weightAvoid = int_checker_settings(
        (settingsFileData.set_index('name').at['weightAvoid', 'points']), 'weightAvoid', 0)

    # verify required values in 'max' and 'min' column are integers
    # if they are, assign value to global variable for scoring function to use.
    defaultMaxTeamSize = int_checker_settings(
        (settingsFileData.set_index('name').at['teamSize', 'max']), 'teamSize', 1)
    defaultMinTeamSize = int_checker_settings(
        (settingsFileData.set_index('name').at['teamSize', 'min']), 'teamSize', 1)
    maxLowGPAStudents = int_checker_settings(
        (settingsFileData.set_index('name').at['maxLowGPAStudents', 'max']), 'maxLowGPAStudents', 1)
    maxESLStudents = int_checker_settings(
        (settingsFileData.set_index('name').at['maxESLStudents', 'max']), 'maxESLStudents', 1)

    # verify that provided maxRunTime is an integer.
    # If it is, set it as maxRunTime for the program, otherwise, use default hour run time.
    try:
        maxRunTime = int(settingsFileData.set_index('name').at['maxRunTime', 'max'])
    except:
        maxRunTime = 60
        print("WARNING: maxRunTime value in settings csv is invalid. Running with default value of 60 minutes.")
    if maxRunTime < 0:
        maxRunTime = 60
        print("WARNING: maxRunTime in the settings csv is not an integer between 1 and 2^64. Running with default value of 60 minutes.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use.
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except:
        sys.exit("The lowGPAThreshold 'min' value is not a float. Terminating program.")
    if (lowGPAThreshold < 0) or (lowGPAThreshold > 4.00) or (pd.isna(lowGPAThreshold)):
        sys.exit("ERROR: lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value. Terminating program.")# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

def studentsHandler(studentsFile):

    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentChoiceN
    global studentAvoidN

    #Error Flag
    errFlg = False

    prints.gen('\nstudentHandler() begin:')

    #Load csv file
    studentsFileData = pd.read_csv(studentsFile)
    # debug print 
    #print(studentsFileData)


    ### Store Data

    prints.gen('Loading global variables...')

    #Verify required columns are present 
    studentsColumns = ['studentID', 'studentChoice1', 'studentGPA','studentESL']
    for col in studentsColumns:
       if col not in studentsFileData.columns:
           prints.err("ERROR: Required {0} column header not found in the students csv file. Terminating Program.".format(col))

    #Create studentChoiceN global dataframe
    fields = [col for col in studentsFileData.columns if 'studentChoice' in col] 
    studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields)  

    #Create global series
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].fillna(False)
    studentPriority = studentsFileData['studentPriority'].fillna(False)


    ### Validate Data
    prints.gen('Verifying data...')

    #Verify studentID contains numbers
    if is_numeric_dtype(studentID) == False:
         prints.logerr("ERROR: Unexpected data type found in studentID.")
         errFlg = True
    #else:
        #debug print
        #print('studentID type correct')
    
    #Verify studentGPA contains numbers
    if is_numeric_dtype(studentGPA) == False:
         prints.logerr("ERROR: Unexpected data type found in studentGPA.")        
         errFlg = True
    #else:
        #debug print
        #print('studentGPA type correct')
     
    #Verify studenChoiceN contains numbers
    clmn = list(studentChoiceN) 
    for i in clmn: 
        if is_numeric_dtype(studentChoiceN[i]) == False:
            prints.logerr("ERROR: Unexpected data type found in studentChoice.")        
            errFlg = True
        #else:
            #debug print
            #print('studentChoice type correct')

    #Verify studentESL contains booleans
    if is_bool_dtype(studentESL) == False:
            prints.logerr("ERROR: Unexpected data type found in studentPriority.")        
            errFlg = True
        #else:
            #debug print
            #print('studentPriority type correct')

    #Check studentID for duplicate
    if studentID.duplicated().any():
        prints.logerr('Duplicate studentID found')
        errFlg = True
    
    #Check studentGPA within range
    for value in studentGPA:
        if (value < 0.0) or (value > 4.0):
            prints.logerr('{0} outside of acceptable GPA range'.format(value))
            errFlg = True

    #Verify studentChoiceN contains valid project ids
    clmns = list(studentChoiceN) 
    for cid in clmns:                   
        for rid in studentChoiceN.index:
            if pd.isna(studentChoiceN[cid][rid]) == False:     #If element not empty
                sChoiceMatch = False
                for i in range(len(projectIDs)):   #Find matching id in global projectIDs
                    if (studentChoiceN[cid][rid] == projectIDs[i]): 
                        sChoiceMatch = True
                        break
                if sChoiceMatch == False:
                    prints.logerr("No matching project id found for studentChoice = {0:n}".format(studentChoiceN[cid][rid]))
                    errFlg = True 
    
    #Check for optional studentPriority column
    if 'studentPriority' in studentsFileData.columns:
        #debug print
        #print ('studentPriority found')
    
        #Verify studentPriority contains booleans
        if is_bool_dtype(studentPriority) == False:
            prints.logerr("Unexpected data type found in studentPriority.")        
        #else:
            #debug print
            #print('studentPriority type correct')
    else:
        prints.warn('studentPriority column not found')

    #Check for optional studentAvoid 
    if 'studentAvoid' in studentsFileData.columns:
        #debug print
        #print('studentAvoid found')
        
        #Create studentAvoidN global dataframe
        fields = [col for col in studentsFileData.columns if 'studentAvoid' in col] 
        studentAvoidN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields)

        #Verify studentAvoidN contains numbers
        clmn = list(studentAvoidN) 
        for i in clmn: 
            if is_numeric_dtype(studentAvoidN[i]) == False:
                prints.logerr("Unexpected data type found in studentAvoid.")        
                errFlg = True
            #else:
                #debug print
                #print('studentAvoid type correct')
        
        #Verify studentAvoidN contains valid student ids
        clmns = list(studentAvoidN) 
        for cid in clmns:                   
            for rid in studentAvoidN.index: 
                if pd.isna(studentAvoidN[cid][rid]) == False:     #If element not empty
                    sAvoidMatch = False
                    for i in studentID.index:          #Find matching id in global studentID
                        if (studentAvoidN[cid][rid] == studentID[i]): 
                            sAvoidMatch = True
                            break
                    if sAvoidMatch == False:
                        prints.logerr("No matching student id found for studentAvoid = {0:n}".format(studentAvoidN[cid][rid])) 
                        errFlg = True
    else:
        prints.warn('studentAvoid NOT found')

    prints.gen('studentHandler done.')

    #Exit when error conditions met
    if errFlg == True:
        prints.err("Invalid data found in Students CSV file. Terminating program.")