# capstone colander (a good name)

# this is a "staging" file, it just calls another file
# it's here because docker always builds "main.py"
# don't develop in this

import sys
import pandas as pd
import argparse
import os
from datetime import datetime


# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
print("Container built", now)  # print it

# default program mode
programMode = 'Assignment'

# accepted command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--students", help="Students CSV filename", required=False, default='io/students.csv')
parser.add_argument("-p", "--projects", help="Projects CSV filename", required=False, default='io/projects.csv')
parser.add_argument("-u", "--settings", help="User Settings CSV filename", required=False, default='io/settings.csv')
parser.add_argument("-o", "--output", help="Output (assignment) CSV filename", required=False, default='io/assignment.csv')
parser.add_argument("-a", "--assign", help="Run the program in Assignment mode", required=False, action='store_true')
parser.add_argument("-c", "--score", help="Run the program in Scoring mode", required=False, action='store_true')
parser.add_argument("-v", "--verbose", help="Run the program in verbose mode", required=False, action='store_true')

argument = parser.parse_args()

# assign csv file names and mode preference
if argument.students:
    studentsFile = argument.students
if argument.projects:
    projectsFile = argument.projects
if argument.settings:
    settingsFile = argument.settings
if argument.output:
    outputFile = argument.output
if argument.score:
    programMode = 'Scoring'
if argument.assign:
    programMode = 'Assignment'
if argument.verbose:
    programMode = 'Verbose'

# for debugging, remove when no longer necessary
print("Students csv is: {0}".format(studentsFile))
print("Projects csv is: {0}".format(projectsFile))
print("Settings csv is: {0}".format(settingsFile))
print("Output csv is: {0}".format(outputFile))
print("Program mode is: {0}".format(programMode))

# verify user provided files exist and that they are .csv files
userFiles = [studentsFile, projectsFile, settingsFile]
for file in userFiles:
    if not os.path.exists(file):
        if not file.endswith('.csv'):
            sys.exit("ERROR: {0} is neither a '.csv' file nor can it be found in the directory. Input files must have .csv extension. Terminating Program.".format(file))
        sys.exit("ERROR: {0} can not be found. Terminating Program.".format(file))
    if not file.endswith('.csv'):
        sys.exit("ERROR: {0} is not a '.csv' file. Input files must have .csv extension. Terminating Program.".format(file))

# inform user if the output they provided already exists and terminate program
if os.path.exists(outputFile) and programMode == 'Assignment':
    sys.exit("ERROR: {0} already exists in the directory. Enter a unique output file name using the -o FILENAME command. Terminating Program.".format(outputFile))

# load projects csv file
projectsFileData = pd.read_csv(projectsFile)

# verify all column headers are present in projects csv file
projectsColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
for col in projectsColumns:
    if col not in projectsFileData.columns:
        sys.exit("ERROR: Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

# debug print to verify data has been loaded
print(projectsFileData)


# function to verify that values listed in csv files are integers
def int_checker(columnName):
    intArray = []
    for value in projectsFileData[columnName]:
        try:
            intArray.append(int(value))
        except ValueError:
            sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
    return intArray


# verify that all values in program csv file are integers
projectIDs = int_checker('projectID')
# if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(42)  # 42 needs to be changed to settings.csv value
minTeamSize = int_checker('minTeamSize')
projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(42)
maxTeamSize = int_checker('maxTeamSize')

# debugging prints
print(projectIDs)
print(minTeamSize)
print(maxTeamSize)

# call another script
if not programMode == 'verbose':
    print('Calling the next function...')
    #os.system('python src/test/test_main.py') # put what file we actually want run here
#os.system('python src/run_ga.py') # put what file we actually want run here