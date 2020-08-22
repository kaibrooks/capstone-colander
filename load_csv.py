# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import sys
import pandas as pd
import prints

#For studentsHandler()
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype

# function verifies that there are no duplicate required column names
# ignore any duplicate non-required fields
def findDuplicateCols(fileData, requiredCols, fileName):
    columnsArray = fileData.columns.str.rsplit('.', n=1).str[0] # separate each column name into an array of strings
    mask = columnsArray.isin(requiredCols) & columnsArray.duplicated() # create an array of bools, indicating if there is or isn't a duplicate from our req. columns
    for dup in mask:
        if dup:
            duplicateColumns = fileData.columns[mask]
            prints.err("Found a duplicate required column in the {0}: {1}. Terminating Program.".format(fileName, duplicateColumns))


def projectsHandler(projectsFileData):
    global minTeamSize
    global maxTeamSize
    global projectIDs
    global errFlg

    # verify required project csv headers are present
    projectsColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
    for col in projectsColumns:
        if col not in projectsFileData.columns:
            prints.err("Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

    # call function to verify there are no duplicates of required columns
    findDuplicateCols(projectsFileData, projectsColumns, 'Projects CSV file')

    # function to verify that all require values in projects csv file are integers within the required range
    def int_checker_projects(columnName):

        tempArray = []
        for value in projectsFileData[columnName]:
            if isinstance(value, object):
                try:
                    value = float(value)
                except ValueError:
                    prints.logerr("{0} in the {1} column is not an integer.".format(value, columnName))
                    errFlg = True
            if isinstance(value, float):
                if value.is_integer():
                    value = int(value)
            if isinstance(value, int):
                if (value < 1) or (value > pow(2, 64)):
                    prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, columnName))
                    errFlg = True
                tempArray.append(value)
            else:
                prints.logerr("{0} in the {1} column is not an integer.".format(value, columnName))
                errFlg = True
        return tempArray

    # verify that all values in program csv file are integers
    projectIDs = int_checker_projects('projectID')

    # verify that there are no duplicate project IDs in the projectID column
    if projectsFileData.projectID.duplicated().any():
        prints.logerr("projectid {0} is a duplicate projectID in the csv file.".format({projectsFileData[projectsFileData.projectID.duplicated()].projectID.iloc[0]}))

    # if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
    projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(defaultMinTeamSize)
    minTeamSize = int_checker_projects('minTeamSize')
    projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(defaultMaxTeamSize)
    maxTeamSize = int_checker_projects('maxTeamSize')

    # verify minTeamSize is not greater than maxTeamSize
    for min,max,pid in zip(minTeamSize,maxTeamSize,projectIDs):
        if min > max:
            prints.logerr("minTeamSize is greater than maxTeamSize for projectID {0}.".format(pid))

    # warn user if gap found in projectID sequence that starts a projectID '1'
    projectIDGap = projectIDs[-1]*(projectIDs[-1] + projectIDs[0]) / 2 - sum(projectIDs)
    if projectIDGap > 0:
        prints.warn("gap found in projectID sequence in the projects csv file.")


def settingsHandler(settingsFileData):
    global weightMaxLowGPAStudents
    global weightMaxESLStudents
    global weightTeamSize
    global weightStudentPriority
    global weightStudentChoice1
    global weightAvoid
    global effort
    global defaultMaxTeamSize
    global defaultMinTeamSize
    global maxLowGPAStudents
    global maxESLStudents
    global lowGPAThreshold
    global errFlg

    errFlg = False

    # verify required settings csv headers are present
    settingsColumns = ['name', 'min', 'max', 'points']
    for col in settingsColumns:
        if col not in settingsFileData.columns:
            prints.err("Required {0} column header not found in the settings csv file. Terminating Program.".format(col))

    # call function to verify there are no duplicates of required columns
    findDuplicateCols(settingsFileData, settingsColumns, 'Settings CSV file')

    # verify required settings csv rows are present
    settingsRows = ['teamSize', 'lowGPAThreshold', 'maxLowGPAStudents', 'maxESLStudents', 'weightMaxLowGPAStudents',
                       'weightMaxESLStudents', 'weightTeamSize', 'weightStudentPriority', 'weightStudentChoice1', 'weightAvoid']
    for row in settingsRows:
        if row not in settingsFileData['name'].values:
            prints.err("Required {0} row not found in the settings csv file. Terminating Program.".format(row))
        if len(settingsFileData[settingsFileData['name'] == row]) > 1:
            prints.err("Required {0} row is duplicated in the settings csv file. Terminating Program.".format(row))

    # function to verify values in the csv file are integers.
    def int_checker_settings(value, rowName, minValue):

        if isinstance(value, int):
            if (value < minValue) or (value > pow(2, 64)):
                prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
                errFlg = True
            return value

        # function to verify integer if data type of value is not originally set as int (dtype could be obj or float)
        def is_integer_settings(value, rowName, minValue):
            if value.is_integer():
                tempInt = int(value)
                if (tempInt < minValue) or (tempInt > pow(2, 64)):
                    prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
                    errFlg = True
                return tempInt
            else:
                prints.logerr("{0} in the {1} row is not an integer.".format(value, rowName))
                errFlg = True
                return 0

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
                prints.logerr("{0} in the {1} row is not an integer.".format(value, rowName))
                errFlg = True
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

    # verify that provided 'effort' value is an integer.
    # If it is, set it as effort for the program, otherwise, use default
    try:
        effort = int(settingsFileData.set_index('name').at['effort', 'max'])
    except:
        effort = 20
    if effort < 0 or effort > 100:
        effort = 20
        prints.warn("'effort' in the settings csv is not an int between 1 and 100. Running with default value of 20.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use.
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except:
        prints.logerr("The lowGPAThreshold 'min' value is not a float.")
        errFlg = True
    if (lowGPAThreshold < 0) or (lowGPAThreshold > 4.00) or (pd.isna(lowGPAThreshold)):
        prints.logerr("lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.")
        errFlg = True


def studentsHandler(studentsFile, progMode):

    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentChoiceN
    global studentAvoid
    global studentAssignment
    global numStudents
    global errFlg
    global numStudentChoices

    #Load csv file
    studentsFileData = pd.read_csv(studentsFile)

    #Verify required columns are present
    studentsColumns = ['studentID', 'studentChoice1', 'studentGPA','studentESL','studentAvoid']
    for col in studentsColumns:
       if col not in studentsFileData.columns:
           prints.err("Required {0} column header not found in the students csv file. Terminating Program.".format(col))


    #Create studentChoiceN global dataframe
    fields = [col for col in studentsFileData.columns if 'studentChoice' in col]
    studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields)

    #Sort studentChoiceN columns sequentially
    studentChoiceN = studentChoiceN.reindex(sorted(studentChoiceN.columns), axis=1)

    #Append list of column names to include studentChoice columns
    studentsColumns.extend(studentChoiceN)
    #Find duplicate required columns
    findDuplicateCols(studentsFileData, studentsColumns, studentsFile)

    #Create global series
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].fillna(False)
    studentPriority = studentsFileData['studentPriority'].fillna(False)
    studentAvoid = studentsFileData['studentAvoid'].copy()

    
    #Define global variable
    numStudents = len(studentsFileData)
    numStudentChoices = len(studentChoiceN.columns)


    #Check for Assign column when in Assign mode
    if progMode == 'Scoring':
        if 'assignment' in studentsFileData.columns:

            #Store assignment column
            studentAssignment = studentsFileData['assignment'].copy()

            #Verify assignment contains numbers
            if is_numeric_dtype(studentAssignment) == False:
                prints.logerr("Unexpected data type found in assignment column.")
                errFlg = True

            #Verify assignment contains valid projects
            for student in range(numStudents):
                if pd.isna(studentAssignment[student]) == True:     #If element empty
                    prints.err("Empty field found in row {0} Assignment column.".format(student))
                else:
                    sAssignmentMatch = False
                    for j in range(len(projectIDs)):   #Find matching id in global projectIDs
                        if (studentAssignment[student] == projectIDs[j]):
                            sAssignmentMatch = True
                            #replace project id with project index
                            studentAssignment.at[student] = j
                            break
                    if sAssignmentMatch == False:
                        prints.logerr("No matching project id found for assignment = {0:n}".format(studentAssignment[student]))
                        errFlg = True
        else:
            prints.err("No assignment column found. Terminating program.")

    #Verify studentID has no NaN values
    for student in range(numStudents):
        if pd.isna(studentID[student]) == True:     #If element empty
            prints.logerr("Empty element found in row {0} of the studentID column".format(student))
            errFlg = True
    
    #Verify studentGPA has no NaN values
    for student in range(numStudents):
        if pd.isna(studentGPA[student]) == True:     #If element empty
            prints.logerr("Empty element found in row {0} of the studentGPA column".format(student))
            errFlg = True
    
    #Verify studentID contains numbers
    if is_numeric_dtype(studentID) == False:
         prints.logerr("Unexpected data type found in studentID.")
         errFlg = True

    #Verify studentGPA contains numbers
    if is_numeric_dtype(studentGPA) == False:
         prints.logerr("Unexpected data type found in studentGPA.")
         errFlg = True

    #Verify studenChoiceN contains numbers
    clmn = list(studentChoiceN)
    for i in clmn:
        if is_numeric_dtype(studentChoiceN[i]) == False:
            prints.logerr("Unexpected data type found in studentChoice.")
            errFlg = True

    #Verify studentESL contains booleans
    if is_bool_dtype(studentESL) == False:
            prints.logerr("Unexpected data type found in studentESL.")
            errFlg = True

    #Check studentID for duplicate
    if studentID.duplicated().any():
        prints.logerr('Duplicate studentID found')
        errFlg = True

    
    #Verify studentAvoid contains numbers
    if is_numeric_dtype(studentAvoid) == False:
         prints.logerr("Unexpected data type found in studentAvoid.")
         errFlg = True

    #Check studentGPA within range
    for value in studentGPA:
        if (value < 0.0) or (value > 4.0):
            prints.logerr('{0} outside of acceptable GPA range'.format(value))
            errFlg = True


    #Verify studentAvoid contains valid student IDs
    for student in range(numStudents):
        if pd.isna(studentAvoid[student]) == False:     #If element not empty
            sAvoidMatch = False
            for j in studentID.index:   #Find matching id in studentIDs
               if (studentAvoid[student] == studentID[j]):
                    sAvoidMatch = True
                    #replace student id with student index
                    studentAvoid.at[student] = j
                    break
            if sAvoidMatch == False:
                prints.logerr("No matching student id found for student = {0:n} in studentAvoid column".format(studentAvoid[student]))
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
                        #replace project id with project index
                        studentChoiceN.at[rid,cid] = i
                        break
                
                if sChoiceMatch == False:
                    prints.logerr("No matching project id found for studentChoice = {0:n}".format(studentChoiceN[cid][rid]))
                    errFlg = True

    #Check for optional studentPriority column
    if 'studentPriority' in studentsFileData.columns:

        #Verify studentPriority contains booleans
        if is_bool_dtype(studentPriority) == False:
            prints.logerr("Unexpected data type found in studentPriority.")
    else:
        prints.warn('studentPriority column not found')

    #Exits when error conditions met
    if errFlg == True:
        prints.err("Invalid data found in input CSV files. Terminating program.")