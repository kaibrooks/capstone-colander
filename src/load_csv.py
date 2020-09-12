# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import pandas as pd
import prints
# for studentsHandler()
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_integer_dtype

# function to look for duplicated required columns
def findDuplicateCols(fileData, requiredCol, csvFile):
    # pandas dataframe appends '.1.' to duplicate columns so check if 'requiredCol'.1 exists
    newCol = str(requiredCol) + '.1'
    if newCol in fileData.columns:
        prints.err("{0} column is duplicated in the {1}". format(requiredCol, csvFile))


# initialize maxValue to be used in verifying a value's range
maxValue = pow(2, 64) - 1

'''
Pandas CSV Dataframe info: If at least one field in a column contains a float, with the rest being integers, the 
dataframe considers all values in the column to be floats. If at least one field in a column contains a string, 
with the rest being either ints or floats, all values in the column are considered objects. Empty fields are 
considered to be floats. The reason this is important is because the way the settings csv is formatted, there are 
multiple fields in each column that are empty and per the requirements document, are ignored by the program. 
This means that the user can fill those fields with random data of strings, ints, or floats and the program ignores 
it, but it effects the data type of the fields we need to verify are ints!
'''
# function to verify required values in the csv file are valid integers
def int_checker(columnName, rowName, fileData, minValue):
    intErrFlag = False

    # function to check if int is within required range
    def check_range(value, location, minValue):
        if (value < minValue) or (value > maxValue):
            prints.logerr(
                "Value {0} in {1} is an integer out of the required range."
                    .format(value, location))
            return True
        return False

    # check if the data type of the value is an int. If it is, verify it's within the required range
    # and return the confirmation that it is an int, the value, and errFlag if it's out of range or not
    def isinstance_int(value, location, minValue):
        if isinstance(value, int):
            return True, value, check_range(value, location, minValue)
        return False, value, False

    # check if the data type of the value is a float. If it is, check if it's an int and if it is,
    # verify it's within the required range and return confirmation of type, value, and errFlag if out of range
    def isinstance_float(value, location, minValue):
        if isinstance(value, float):
            if value.is_integer():
                tempInt = int(value)
                return True, tempInt, check_range(value, location, minValue)
            return True, value, True
        return False, value, False

    # check if the data type of the value is an obj. If it is, try to convert to float, and then check if it's an
    # int within the required range. return confirmation of type, value, and errFlag
    def isinstance_obj(value, location, minValue):
        try:
            tempFloat = float(value)
        except ValueError:
            prints.logerr("{0} in {1} is not an integer.".format(value, location))
            return True, 0, True
        isObj, value, intErrFlag = isinstance_float(tempFloat, location, minValue)
        return isObj, value, intErrFlag

    # if settings csv file is being checked, only check one value at a time and return value with errFlag
    if rowName:
        isInteger, value, intErrFlag = isinstance_int(fileData, rowName, minValue)
        if isInteger:
            return value, intErrFlag
        isFloat, value, intErrFlag = isinstance_float(fileData, rowName, minValue)
        if isFloat:
            return value, intErrFlag
        isObj, value, intErrFlag = isinstance_obj(fileData, rowName, minValue)
        return value, intErrFlag

    # if projects csv file, iterate through entire column to verify all values are valid integers,
    # append them into an array and return array with errFlag (True if any invalid values found)
    if columnName:
        tempArray = []
        for value in fileData[columnName]:
            isInteger, value, tempErrFlag = isinstance_int(value, columnName, minValue)
            if tempErrFlag:
                intErrFlag = tempErrFlag
            if isInteger:
                tempArray.append(value)
                continue
            isFloat, value, tempErrFlag = isinstance_float(value, columnName, minValue)
            if tempErrFlag:
                intErrFlag = tempErrFlag
            if isFloat:
                tempArray.append(value)
                continue
            isObj, value, tempErrFlag = isinstance_obj(value, columnName, minValue)
            if tempErrFlag:
                intErrFlag = tempErrFlag
            tempArray.append(value)
        return tempArray, intErrFlag


def check_error_flag(errFlag, currFlag):
    if errFlag:
        return errFlag
    return currFlag


# initialize values used in settingsHandler()
weightMaxLowGPAStudents = 0
weightMaxESLStudents = 0
weightMaxTeamSize = 0
weightMinTeamSize = 0
weightStudentPriority = 0
weightStudentChoice1 = 0
weightAvoid = 0
effort = 20
minEffort = 0
maxEffort = 100
defaultEffort = 20
maxLowGPAStudents = 1
maxESLStudents = 1
lowGPAThreshold = 1
minGPAThreshold = 0.00
maxGPAThreshold = 4.00
defaultMaxTeamSize = 1
defaultMinTeamSize = 1

def settingsHandler(settingsFileData):
    global weightMaxLowGPAStudents
    global weightMaxESLStudents
    global weightMaxTeamSize
    global weightMinTeamSize
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

    # verify required settings csv headers are present and not duplicated
    requiredColumns = ['name', 'min', 'max', 'points']
    for col in requiredColumns:
        if col not in settingsFileData.columns:
            prints.err("Required {0} column header not found in the settings csv. Terminating Program.".format(col))
        else:
            findDuplicateCols(settingsFileData, col, 'Settings CSV file')

    # verify required settings csv rows are present and not duplicated
    requiredRows = ['teamSize', 'lowGPAThreshold', 'maxLowGPAStudents', 'maxESLStudents', 'weightMaxLowGPAStudents',
                    'weightMaxESLStudents', 'weightMinTeamSize', 'weightMaxTeamSize', 'weightStudentPriority',
                    'weightStudentChoice1', 'weightAvoid', 'effort']
    for row in requiredRows:
        if row not in settingsFileData['name'].values:
            prints.err("Required {0} row not found in the settings csv file. Terminating Program.".format(row))
        if len(settingsFileData[settingsFileData['name'] == row]) > 1:
            prints.err("Required {0} row is duplicated in the settings csv file. Terminating Program.".format(row))

    # verify required fields in 'points' column contain integers
    # if they are, assign value to global variable for scoring function to use
    weightMaxLowGPAStudents, intErr = int_checker(None, 'weightMaxLowGPAStudents',
                                                  (settingsFileData.set_index('name').
                                                      at['weightMaxLowGPAStudents', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightMaxESLStudents, intErr = int_checker(None, 'weightMaxESLStudents',
                                               (settingsFileData.set_index('name')
                                                   .at['weightMaxESLStudents', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightMinTeamSize, intErr = int_checker(None, 'weightMinTeamSize',
                                            (settingsFileData.set_index('name')
                                                .at['weightMinTeamSize', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightMaxTeamSize, intErr = int_checker(None, 'weightMaxTeamSize',
                                            (settingsFileData.set_index('name')
                                                .at['weightMaxTeamSize', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightStudentPriority, intErr = int_checker(None, 'weightStudentPriority',
                                                (settingsFileData.set_index('name')
                                                    .at['weightStudentPriority', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightStudentChoice1, intErr = int_checker(None, 'weightStudentChoice1',
                                               (settingsFileData.set_index('name')
                                                   .at['weightStudentChoice1', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    weightAvoid, intErr = int_checker(None, 'weightAvoid',
                                      (settingsFileData.set_index('name').at['weightAvoid', 'points']), 0)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)

    # verify required values in 'max' and 'min' column are integers
    # if they are, assign value to global variable for scoring function to use
    defaultMaxTeamSize, intErr = int_checker(None, 'teamSize',
                                             (settingsFileData.set_index('name').at['teamSize', 'max']), 1)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    defaultMinTeamSize, intErr = int_checker(None, 'teamSize',
                                             (settingsFileData.set_index('name').at['teamSize', 'min']), 1)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    maxLowGPAStudents, intErr = int_checker(None, 'maxLowGPAStudents',
                                            (settingsFileData.set_index('name').at['maxLowGPAStudents', 'max']), 1)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)
    maxESLStudents, intErr = int_checker(None, 'maxESLStudents',
                                         (settingsFileData.set_index('name').at['maxESLStudents', 'max']), 1)
    settingsErrFlag = check_error_flag(intErr, settingsErrFlag)

    # if effort value is provided in the csv file, verify the value is an integer within the required range
    # if it is not, use default value
    try:
        effort = int(settingsFileData.set_index('name').at['effort', 'max'])
    except ValueError:
        prints.warn("valid 'effort' value not found in the settings csv. Running with default value.")
    if effort < minEffort or effort > maxEffort:
        effort = defaultEffort
        prints.warn("'effort' in the settings csv is not an int between 1 and 100. Running with default value of 20.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except ValueError:
        prints.logerr("The lowGPAThreshold 'min' value is not a float.")
        settingsErrFlag = True
        lowGPAThreshold = 0  # temp value to pass statement below to allow program to continue checking for errors
    if (lowGPAThreshold < minGPAThreshold) or (lowGPAThreshold > maxGPAThreshold) or (pd.isna(lowGPAThreshold)):
        prints.logerr("lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.")
        settingsErrFlag = True

    return settingsErrFlag


# initialize values used in settingsHandler()
minTeamSize = []
maxTeamSize = []
projectIDs = []

def projectsHandler(projectsFileData):
    # arrays indexed by project
    global minTeamSize
    global maxTeamSize
    global projectIDs

    projectsErrFlag = False
    # verify required project csv headers are present and not duplicated
    requiredColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
    for col in requiredColumns:
        if col not in projectsFileData.columns:
            prints.err("Required {0} column not found in the projects csv file. Terminating Program.".format(col))
        else:
            findDuplicateCols(projectsFileData, col, 'Projects CSV file')

    # verify that all values in program csv file are integers
    projectIDs, intErr = int_checker('projectID', None, projectsFileData, 1)
    projectsErrFlag = check_error_flag(intErr, projectsErrFlag)

    # verify that there are no duplicate project IDs in the projectID column
    if projectsFileData.projectID.duplicated().any():
        projectsErrFlag = True
        projectDuplicates = projectsFileData[projectsFileData.projectID.duplicated()]
        for i in range(len(projectDuplicates)):
            prints.logerr("Duplicate projectID found: {0}".format(
                projectsFileData[projectsFileData.projectID.duplicated()].iloc[i]))

    # if values for team sizes are blank, enter size from settings csv and then verify all values are integers
    projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(defaultMinTeamSize)
    minTeamSize, intErr = int_checker('minTeamSize', None, projectsFileData, 1)
    projectsErrFlag = check_error_flag(intErr, projectsErrFlag)
    projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(defaultMaxTeamSize)
    maxTeamSize, intErrFlag = int_checker('maxTeamSize', None, projectsFileData, 1)
    projectsErrFlag = check_error_flag(intErr, projectsErrFlag)

    # verify minTeamSize is not greater than maxTeamSize
    # zip() used to iterate in parallel over multiple iterables
    for minSize, maxSize, pid in zip(minTeamSize, maxTeamSize, projectIDs):
        if minSize > maxSize:
            projectsErrFlag = True
            prints.logerr("minTeamSize is greater than maxTeamSize for projectID {0}.".format(pid))

    # warn user if gap found in projectID sequence, assuming projectIDs start at projectID '1'
    # arithmetic series = (n(firstNum + lastNum)) / 2, where n is # of terms in sequence,
    # then subtract real sum of projectIDs
    try:
        projectIDGap = projectIDs[-1] * (projectIDs[0] + projectIDs[-1]) / 2 - sum(projectIDs)
    except ValueError:
        projectIDGap = 0 # temp value to pass next if statement. Cause of error would have already been identified.
    if not projectIDGap == 0:
        prints.warn("gap found in projectID sequence in the projects csv file.")

    return projectsErrFlag


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


    def checkExists(dataSeries):
        errNan = False
        for student in range(numStudents):
            # Verify series has no NaN values
            if pd.isna(dataSeries[student]) is True:     # If element empty
                prints.logerr("Empty element found in {0} column, row {1}".format(dataSeries.name, student))
                errNan = True
        return errNan

    def checkInt(dataSeries):
        errInt = False
        if is_numeric_dtype(dataSeries) is False:   # Look at series label
            errInt = True
            for student in range(numStudents):
                if dataSeries[student].isnumeric() is False and pd.isna(dataSeries[student]) is False:    # Look at element
                    prints.logerr("Unexpected data found in {0}, row {1} = '{2}'".format(dataSeries.name, student, dataSeries[student]))
        elif is_integer_dtype(dataSeries) is False:
            for student in range(numStudents):
                if not dataSeries[student].is_integer() and pd.isna(dataSeries[student]) is False:
                    prints.logerr("Unexpected data found in {0}, row {1} = '{2}'".format(dataSeries.name, student, dataSeries[student]))
        return errInt

    def checkFloat(dataSeries):
        errFloat = False
        if is_numeric_dtype(dataSeries) is False:
            errFloat = True
            for student in range(numStudents):
                try:
                    float(dataSeries[student])
                except ValueError:
                    prints.logerr("Unexpected data found in {0}, row {1} = '{2}'".format(dataSeries.name, student, dataSeries[student]))
        return errFloat

    def checkBool(dataSeries):
        errBool = False
        if is_bool_dtype(dataSeries) is False:
            errBool = True
            for student in range(numStudents):
                val = dataSeries[student]
                if val is not False:
                    val = val.lower()
                if val is not False and val != 'true' and val != 'false':
                    prints.logerr("Unexpected data found in {0}, row {1} = '{2}'".format(dataSeries.name, student, dataSeries[student]))
        return errBool

    def checkRange(dataSeries, rmin, rmax):
        errRange = False
        for value in dataSeries:
            if (value < rmin) or (value > rmax):
                prints.logerr('{0} outside of acceptable range for {1}. Accepted values are between {2} - {3}'.format(value, dataSeries.name, rmin, rmax))
                errRange = True
        return errRange

    def checkDup(dataSeries):
        errDup = False
        if dataSeries.duplicated().any():
            errDup = True
            sDuplicates = dataSeries[dataSeries.duplicated()]
            for i in range(len(sDuplicates)):
                prints.logerr("Duplicate {0} found '{1}'".format(dataSeries.name, dataSeries[dataSeries.duplicated()].iloc[i]))
        return errDup

    def match1D(dataSeries, parentData):  # dataSeries is being checked against parentData
        errMatch = False
        for student in range(numStudents):
            if pd.isna(dataSeries[student]) is False:     # If element not empty
                sMatch = False
                for j in range(len(parentData)):   # Find matching element in parentData
                    if (dataSeries[student] == parentData[j]):
                        sMatch = True
                        # replace element with parentData index
                        dataSeries.at[student] = j
                        break
                if sMatch is False:
                    prints.logerr("No match found in {0} column, row {1} = {2:n}".format(dataSeries.name, student, dataSeries[student]))
                    errMatch = True
        return errMatch

    def matchProject2D(dataFrame):
        errProj = False

        # when Pandas finds unexpected data type, elements in dataFrame cast as objects, not int
        for col in dataFrame.columns:
            # Set flag for typecasting when column is not numeric
            numeric = True
            if is_numeric_dtype(dataFrame[col]) is False:
                numeric = False
            for row in dataFrame.index:
                if pd.isna(dataFrame[col][row]) is False:     # If element not empty
                    # Numeric typecasting for when a letter is present in the column
                    if numeric is False:
                        try:
                            dataFrame.at[row, col] = int(dataFrame[col][row])
                        except:
                            prints.logerr("Unexpected data found in {0}, row {1} = '{2}'".format(col, row, dataFrame[col][row]))
                            errProj = True

                    for i in range(len(projectIDs)):   # Find matching id in global projectIDs
                        sChoiceMatch = False
                        if (dataFrame[col][row] == projectIDs[i]):
                            sChoiceMatch = True
                            # replace project id with project index
                            dataFrame.at[row, col] = i
                            break
                    if sChoiceMatch is False:
                        prints.logerr("No matching project id found for {0} = '{1}'".format(col, dataFrame[col][row]))
                        errProj = True
        return errProj

    def checkStudentID(studentID):
        errID = False

        if checkExists(studentID):
            errID = True
        if errID is False and checkInt(studentID):
            errID = True
        if errID is False and checkDup(studentID):
            errID = True
        if errID is False and checkRange(studentID, 0, maxValue):
            errID = True

        return errID

    def checkStudentGPA(studentGPA):
        errGPA = False

        if checkExists(studentGPA):
            errGPA = True
        if errGPA is False and checkFloat(studentGPA):
            errGPA = True
        if errGPA is False and checkRange(studentGPA, 0.0, 4.0):
            errGPA = True

        return errGPA

    def checkStudentESL(studentESL):
        errESL = False

        if checkBool(studentESL):
            errESL = True
        return errESL

    def checkStudentPriority(studentPriority):
        errPri = False

        if checkBool(studentPriority):
            errPri = True
        return errPri

    def checkAssignment(studentAssignment):
        errAssign = False

        if checkExists(studentAssignment):
            errAssign = True
        if erAssign is False and checkInt(studentAssignment):
            errAssign = True
        if errAssign is False and match1D(studentAssignment, projectIDs):
            errAssign = True
        return errAssign

    def checkAvoid(studentAvoid):
        errAvoid = False

        if checkInt(studentAvoid):
            errAvoid = True
        if errAvoid is False and match1D(studentAvoid, studentID):
            errAvoid = True
        return errAvoid

    def checkChoices(studentChoiceN):
        errChoice = False

        if checkExists(studentChoiceN['studentChoice1']):
            errChoice = True
        if matchProject2D(studentChoiceN):
            errChoice = True
        return errChoice

    # Verify required columns are present
    requiredColumns = ['studentID', 'studentChoice1', 'studentGPA', 'studentESL', 'studentAvoid', 'studentPriority']
    for col in requiredColumns:
        if col not in studentsFileData.columns:
            prints.err("Required {0} column header not found in the students csv file. Terminating Program.".format(col))
        findDuplicateCols(studentsFileData, requiredColumns, 'Students CSV File')

    # Search for sequential studentChoice columns to store in global dataframe
    choiceFields = ['studentChoice1']
    studentsCols = list(studentsFileData)
    for i in range(1, len(studentsFileData.columns)):   # iterate through each column in the studentsFileData
        sChoiceI = 'studentChoice' + str(i)
        if sChoiceI in studentsCols and i != 1:
            choiceFields.append(sChoiceI)           # Create list of found header names
        elif sChoiceI not in studentsCols:
            break
    # Store studentChoice columns in global dataframe
    studentChoiceN = studentsFileData[choiceFields].copy()

    # Create global series
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].fillna(False)
    studentPriority = studentsFileData['studentPriority'].fillna(False)
    studentAvoid = studentsFileData['studentAvoid'].copy()

    # Define global variable
    numStudents = len(studentsFileData)
    numStudentChoices = len(studentChoiceN.columns)

    # Verify student ID data
    if checkStudentID(studentID):
        errFlag = True
    else:
        # if student ID data is correct verify student avoid data
        if checkAvoid(studentAvoid):
            errFlag = True

    # Verify studentGPA data
    if checkStudentGPA(studentGPA):
        errFlag = True

    # Verify studentESL data
    if checkStudentESL(studentESL):
        errFlag = True

    # Verify student Priority data
    if checkStudentPriority(studentPriority):
        errFlag = True

    # Verify student Choices
    if checkChoices(studentChoiceN):
        errFlag = True

    # Verify assignment column when in assignment mode
    if progMode == 'Scoring':

        if 'assignment' in studentsFileData.columns:

            # Store assignment column
            studentAssignment = studentsFileData['assignment'].copy()
            if checkAssignment(studentAssignment):
                errFlag = True
        else:
            prints.err("No assignment column found. Terminating program.")

    return errFlag
