# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import sys
import pandas as pd


def projectsHandler(projectsFile):
    global minTeamSize
    global maxTeamSize
    global projectIDs

    # load projects csv file
    projectsFileData = pd.read_csv(projectsFile)

    # verify required project csv headers are present
    projectsColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
    for col in projectsColumns:
        if col not in projectsFileData.columns:
            sys.exit("ERROR: Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

    # function to verify that values listed in the projects csv are integers within required range
    def int_checker_projects(columnName):
        intArray = []
        for value in projectsFileData[columnName]:
            try:
                intArray.append(int(value))
            except ValueError:
                sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
        for value in intArray:
            if (value < 0) or (value > pow(2, 64)):
                sys.exit("ERROR: Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, columnName))
        return intArray

    # verify that all values in program csv file are integers
    projectIDs = int_checker_projects('projectID')

    # verify that there are no duplicate project IDs in the projectID column
    if projectsFileData.projectID.duplicated().any():
        sys.exit("ERROR: projectid {0} is a duplicate projectID in the csv file. Terminating Program.".format({projectsFileData[projectsFileData.projectID.duplicated()].projectID.iloc[0]}))

    # if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
    projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(defaultMinTeamSize)
    minTeamSize = int_checker_projects('minTeamSize')
    projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(defaultMaxTeamSize)
    maxTeamSize = int_checker_projects('maxTeamSize')

    # verify minTeamSize is not greater than maxTeamSize
    for min,max,pid in zip(minTeamSize,maxTeamSize,projectIDs):
        if min > max:
            sys.exit("ERROR: minTeamSize is greater than maxTeamSize for projectID {0}.".format(pid))

    # warn user if gap found in projectID sequence that starts a projectID '1'
    projectIDGap = projectIDs[-1]*(projectIDs[-1] + projectIDs[0]) / 2 - sum(projectIDs)
    if projectIDGap > 0:
        print("\nWARNING: gap found in projectID sequence in the projects csv file.")


def settingsHandler(settingsFile):
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

    # load projects csv file
    settingsFileData = pd.read_csv(settingsFile)

    print(settingsFileData)
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

    # function to verify that values listed in the settings csv are integers within range
    def int_checker_settings(value, rowName, minValue):
        try:
            tempInt = int(value)
        except ValueError:
            sys.exit("ERROR: {0} in the {1} row is not an integer. Terminating Program.".format(value, rowName))
        if (value < minValue) or (value > pow(2, 64)):
            sys.exit("ERROR: Value {0} in the {1} column must be an integer greater than zero and less than 2^64.".format(value, rowName))
        return tempInt

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
    maxRunTime = 60
    try:
        maxRunTime = int(settingsFileData.set_index('name').at['maxRunTime', 'max'])
    except:
        pass
    if maxRunTime < 0:
        sys.exit("maxRunTime in the settings csv must be an integer between 1 and 2^64.")

    # verify that provided lowGPAThreshold is not empty and that it's a float within range
    # If it is, assign value to global variable for scoring function to use.
    try:
        lowGPAThreshold = float(settingsFileData.set_index('name').at['lowGPAThreshold', 'min'])
    except:
        sys.exit("The lowGPAThreshold 'min' value is not a float. Terminating program.")
    if (lowGPAThreshold < 0) or (lowGPAThreshold > 4.00) or (pd.isna(lowGPAThreshold)):
        sys.exit("ERROR: lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value. Terminating program.")
