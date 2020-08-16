# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import sys
import pandas as pd
import prints


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
    global maxRunTime
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
    settingsRows = ['teamSize', 'lowGPAThreshold', 'maxLowGPAStudents', 'maxESLStudents', 'maxRunTime', 'weightMaxLowGPAStudents',
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

    # verify that provided maxRunTime is an integer.
    # If it is, set it as maxRunTime for the program, otherwise, use default hour run time.
    try:
        maxRunTime = int(settingsFileData.set_index('name').at['maxRunTime', 'max'])
    except:
        maxRunTime = 60
        prints.warn("maxRunTime value in settings csv is not an integer. Running with default value of 60 minutes.")
    if maxRunTime < 0:
        maxRunTime = 60
        prints.warn("maxRunTime in the settings csv is not a value between 1 and 2^64. Running with default value of 60 minutes.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use.
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except:
        prints.logerr("The lowGPAThreshold 'min' value is not a float.")
    if (lowGPAThreshold < 0) or (lowGPAThreshold > 4.00) or (pd.isna(lowGPAThreshold)):
        prints.logerr("lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.")


def studentsHandler(studentsFile, progMode):

    print("\nstudentHandler will be here.")