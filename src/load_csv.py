# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import pandas as pd
import prints
# for studentsHandler()
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype


# function verifies that there are no duplicate required column names
# ignores any duplicate non-required fields
def findDuplicateCols(fileData, requiredCols, csvFile):
    # duplicate columns have a '.1' attached to them in the pandas dataframe
    # so, remove any '.1's from column names and place each column name into an array
    columnNamesArray = fileData.columns.str.rsplit('.', n=1).str[0]
    # create an array of booleans, indicating if there is or isn't a duplicate from the required columns
    # by performing a bitwise AND operation on required columns array and if they are duplicated
    mask = columnNamesArray.isin(requiredCols) & columnNamesArray.duplicated()
    # if duplicate (True) found, display which required columns were duplicated
    # and in which csv file they are located
    for dup in mask:
        if dup:
            duplicateColumns = fileData.columns[mask]
            prints.err("Found duplicate required column(s) in the {0}: {1}. Terminating Program.".format(csvFile, duplicateColumns))
            break


def projectsHandler(projectsFileData):
    global projectsErrFlag
    # arrays indexed by project
    global minTeamSize
    global maxTeamSize
    global projectIDs

    projectsErrFlag = False

    # verify required project csv headers are present
    requiredColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
    for col in requiredColumns:
        if col not in projectsFileData.columns:
            prints.err("Required {0} column not found in the projects csv file. Terminating Program.".format(col))

    # call function to verify there are no duplicates of required columns
    findDuplicateCols(projectsFileData, requiredColumns, 'Projects CSV file')

    # function to verify that all required values in projects csv file are integers within the required range
    def int_checker_projects(columnName):
        global projectsErrFlag

        tempArray = []
        for value in projectsFileData[columnName]:
            if isinstance(value, object):
                try:
                    value = float(value)
                except ValueError:
                    prints.logerr("{0} in the {1} column is not an integer.".format(value, columnName))
                    projectsErrFlag = True
            if isinstance(value, float):
                if value.is_integer():
                    value = int(value)
            if isinstance(value, int):
                if (value < 1) or (value > pow(2, 64)):
                    prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, columnName))
                    projectsErrFlag = True
                tempArray.append(value)
            else:
                prints.logerr("{0} in the {1} column is not an integer.".format(value, columnName))
                projectsErrFlag = True
        return tempArray

    # verify that all values in program csv file are integers
    projectIDs = int_checker_projects('projectID')

    # verify that there are no duplicate project IDs in the projectID column
    if projectsFileData.projectID.duplicated().any():
        projectsErrFlag = True
        projectDuplicates = projectsFileData[projectsFileData.projectID.duplicated()]
        for i in range(len(projectDuplicates)):
            prints.logerr("Duplicate projectID found: {0}".format(projectsFileData[projectsFileData.projectID.duplicated()].iloc[i]))

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
    projectIDGap = projectIDs[-1]*(projectIDs[0] + projectIDs[-1]) / 2 - sum(projectIDs)
    if projectIDGap > 0:
        prints.warn("gap found in projectID sequence in the projects csv file.")

    return projectsErrFlag


def settingsHandler(settingsFileData):

    global settingsErrFlag
    global weightMaxLowGPAStudents
    global weightMaxESLStudents
    global weightTeamSize
    global weightStudentPriority
    global weightStudentChoice1
    global weightAvoid
    global effort
    global maxLowGPAStudents
    global maxESLStudents
    global lowGPAThreshold
    global defaultMaxTeamSize
    global defaultMinTeamSize

    settingsErrFlag = False

    # verify required settings csv headers are present
    requiredColumns = ['name', 'min', 'max', 'points']
    for col in requiredColumns:
        if col not in settingsFileData.columns:
            prints.err("Required {0} column header not found in the settings csv file. Terminating Program.".format(col))

    # verify there are no duplicates of required columns
    findDuplicateCols(settingsFileData, requiredColumns, 'Settings CSV file')

    # verify required settings csv rows are present and not duplicated
    requiredRows = ['teamSize', 'lowGPAThreshold', 'maxLowGPAStudents', 'maxESLStudents', 'weightMaxLowGPAStudents',
                       'weightMaxESLStudents', 'weightTeamSize', 'weightStudentPriority', 'weightStudentChoice1', 'weightAvoid']
    for row in requiredRows:
        if row not in settingsFileData['name'].values:
            prints.err("Required {0} row not found in the settings csv file. Terminating Program.".format(row))
        if len(settingsFileData[settingsFileData['name'] == row]) > 1:
            prints.err("Required {0} row is duplicated in the settings csv file. Terminating Program.".format(row))

    # function to verify values in the csv file are integers.
    def int_checker_settings(value, rowName, minValue):
        global settingsErrFlag

        if isinstance(value, int):
            if (value < minValue) or (value > pow(2, 64)):
                prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
                settingsErrFlag = True
            return value

        # function to verify integer if data type of value is not originally set as int (dtype could be obj or float)
        def is_integer_settings(value, rowName, minValue):
            global settingsErrFlag

            if value.is_integer():
                tempInt = int(value)
                if (tempInt < minValue) or (tempInt > pow(2, 64)):
                    prints.logerr("Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
                    settingsErrFlag = True
                return tempInt
            else:
                prints.logerr("{0} in the {1} row is not an integer.".format(value, rowName))
                settingsErrFlag = True
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
                settingsErrFlag = True
                return 0
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
        prints.warn("valid 'effort' value not found in the settings csv. Running with default value of 20.")
    if effort < 0 or effort > 100:
        effort = 20
        prints.warn("'effort' in the settings csv is not an int between 1 and 100. Running with default value of 20.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use.
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except:
        prints.logerr("The lowGPAThreshold 'min' value is not a float.")
        settingsErrFlag = True
        lowGPAThreshold = 0 # temp value to pass next if statement so allow program to continue checking for errors
    if (lowGPAThreshold < 0) or (lowGPAThreshold > 4.00) or (pd.isna(lowGPAThreshold)):
        prints.logerr("lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.")
        settingsErrFlag = True

    return settingsErrFlag


def studentsHandler(studentsFileData, progMode):
    # Series indexed by student
    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentAvoid
    global studentAssignment
    # DataFrame
    global studentChoiceN
    # Scalar
    global numStudents
    global numStudentChoices

    errFlag = False

    # Verify required columns are present
    requiredColumns = ['studentID', 'studentChoice1', 'studentGPA', 'studentESL', 'studentAvoid']
    for col in requiredColumns:
        if col not in studentsFileData.columns:
            prints.err(
                "Required {0} column header not found in the students csv file. Terminating Program.".format(col))

    # Search for sequential studentChoice columns to store in global dataframe
    choiceFields = ['studentChoice1']
    studentsCols = list(studentsFileData)
    for i in range(1, len(studentsFileData.columns)):  # iterate through each column in the studentsFileData
        sChoiceI = 'studentChoice' + str(i)
        if sChoiceI in studentsCols and i != 1:
            choiceFields.append(sChoiceI)  # Create list of found header names
        elif sChoiceI not in studentsCols:
            break
    # Store studentChoice columns in global dataframe
    studentChoiceN = studentsFileData[choiceFields].copy()

    # Append list of column names to include studentChoice columns
    requiredColumns.remove("studentChoice1")  # removes duplicate column from list
    requiredColumns.extend(choiceFields)
    # Find duplicate required columns
    findDuplicateCols(studentsFileData, requiredColumns, 'Students CSV File')

    # Create global series
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].fillna(False)
    studentPriority = studentsFileData['studentPriority'].fillna(False)
    studentAvoid = studentsFileData['studentAvoid'].copy()

    # Define global variable
    numStudents = len(studentsFileData)
    numStudentChoices = len(studentChoiceN.columns)

    # Check for Assign column when in Assign mode
    if progMode == 'Scoring':
        if 'assignment' in studentsFileData.columns:

            # Store assignment column
            studentAssignment = studentsFileData['assignment'].copy()

            # Verify assignment contains numbers
            if is_numeric_dtype(studentAssignment) == False:
                for student in range(numStudents):
                    if studentAssignment[student].isnumeric() == False:
                        prints.logerr("Unexpected data found in assignment column, row {0} = {1} ".format(student,
                                                                                                          studentAssignment[
                                                                                                              student]))
            else:
                # Verify assignment contains valid projects
                for student in range(numStudents):
                    if pd.isna(studentAssignment[student]) == True:  # If element empty
                        prints.err("Empty field found in Assignment column, row {0}.".format(student))
                    else:
                        sAssignmentMatch = False
                        for j in range(len(projectIDs)):  # Find matching id in global projectIDs
                            if (studentAssignment[student] == projectIDs[j]):
                                sAssignmentMatch = True
                                # replace project id with project index
                                studentAssignment.at[student] = j
                                break
                        if sAssignmentMatch == False:
                            prints.logerr("No matching project id found for assignment = {0:n}".format(
                                studentAssignment[student]))
                            errFlag = True
        else:
            prints.err("No assignment column found. Terminating program.")

    for student in range(numStudents):
        # Verify studentID has no NaN values
        if pd.isna(studentID[student]) == True:  # If element empty
            prints.logerr("Empty element found in studentID column, row {0}".format(student))
            errFlag = True

        # Verify studentGPA has no NaN values
        if pd.isna(studentGPA[student]) == True:  # If element empty
            prints.logerr("Empty element found in studentGPA column, row {0}".format(student))
            errFlag = True

    # Verify studentID contains numbers
    if is_numeric_dtype(studentID) == False:
        errFlag = True
        for student in range(numStudents):
            if studentID[student].isnumeric() == False:
                prints.logerr("Unexpected data found in studentID, row {0} = '{1}'".format(student, studentID[student]))

    # Verify studentGPA contains numbers
    if is_numeric_dtype(studentGPA) == False:
        errFlag = True
        for student in range(numStudents):
            try:
                float(studentGPA[student])
            except ValueError:
                prints.logerr(
                    "Unexpected data found in studentGPA, row {0} = '{1}'".format(student, studentGPA[student]))

    # Verify studentESL contains booleans
    if is_bool_dtype(studentESL) == False:
        errFlag = True
        for student in range(numStudents):
            val = studentESL[student]
            if val != False:
                val = val.lower()
                if val != 'true' and val != 'false':
                    prints.logerr(
                        "Unexpected data found in studentESL, row {0} = '{1}'".format(student, studentESL[student]))

    # Check for optional studentPriority column
    if 'studentPriority' in studentsFileData.columns:

        # Verify studentPriority contains booleans
        if is_bool_dtype(studentPriority) == False:
            errFlag = True
            for student in range(numStudents):
                val = studentPriority[student]
                if val != False:
                    val = val.lower()
                    if val != 'true' and val != 'false':
                        prints.logerr("Unexpected data found in studentPriority, row {0} = '{1}'".format(student,
                                                                                                         studentPriority[
                                                                                                             student]))

    # Check studentID for duplicate
    if studentID.duplicated().any():
        errFlag = True
        sDuplicates = studentID[studentID.duplicated()]
        for i in range(len(sDuplicates)):
            prints.logerr("Duplicate studentID found '{0}'".format(studentID[studentID.duplicated()].iloc[i]))

    # Verify studentAvoid contains numbers
    if is_numeric_dtype(studentAvoid) == False:
        errFlag = True
        for student in range(numStudents):
            if studentAvoid[student].isnumeric() == False:
                prints.logerr(
                    "Unexpected data found in studentAvoid, row {0} = '{1}'".format(student, studentAvoid[student]))

    if errFlag == True:
        prints.err("Unexpected data type(s) found in students input file. Terminating Program.")

    # Check studentGPA within range
    for value in studentGPA:
        if (value < 0.0) or (value > 4.0):
            prints.logerr('{0} outside of acceptable GPA range. Accepted values are between 0.0 - 4.0'.format(value))
            errFlag = True

    # Verify studentAvoid contains valid student IDs
    for student in range(numStudents):
        if pd.isna(studentAvoid[student]) == False:  # If element not empty
            sAvoidMatch = False
            for j in studentID.index:  # Find matching id in studentIDs
                if (studentAvoid[student] == studentID[j]):
                    sAvoidMatch = True
                    # replace student id with student index
                    studentAvoid.at[student] = j
                    break
            if sAvoidMatch == False:
                prints.logerr("No matching student id found in studentAvoid column, for student = {0:n}".format(
                    studentAvoid[student]))
                errFlag = True

    # Verify studentChoiceN contains valid project ids
    # when Pandas finds unexpected data type, elements in studentChoiceN cast as objects, not int

    for col in choiceFields:
        # Set flag for typecasting when column is not numeric
        numeric = True
        if is_numeric_dtype(studentChoiceN[col]) == False:
            numeric = False

        for row in studentChoiceN.index:
            if pd.isna(studentChoiceN[col][row]) == False:  # If element not empty
                # Numeric typecasting for when a letter is present in the column
                if numeric == False:
                    try:
                        studentChoiceN.at[row, col] = int(studentChoiceN[col][row])
                    except:
                        prints.logerr(
                            "Unexpected data found in {0}, row {1} = '{2}'".format(col, row, studentChoiceN[col][row]))
                        errFlag = True

                for i in range(len(projectIDs)):  # Find matching id in global projectIDs
                    sChoiceMatch = False
                    if (studentChoiceN[col][row] == projectIDs[i]):
                        sChoiceMatch = True
                        # replace project id with project index
                        studentChoiceN.at[row, col] = i
                        break
                if sChoiceMatch == False:
                    prints.logerr("No matching project id found for {0} = '{1}'".format(col, studentChoiceN[col][row]))
                    errFlag = True

    # Exits when error conditions met
    if errFlag == True:
        prints.err("Invalid data found in input CSV files. Terminating program.")