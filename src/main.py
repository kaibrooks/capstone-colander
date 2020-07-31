# capstone colander

# main.py parses command line arguments, handles command line errors,
# and calls remaining functions from other files.

import sys
import argparse
import os
from datetime import datetime
from load_csv import studentsHandler
import load_csv

#Code for development
#from student_error_checker import studentsHandler

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
print("Container built", now)  # print it


def main():

    # default program mode
    programMode = 'Assignment'

    # accepted command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--students", help="Students CSV filename", required=False, default='students.csv')
    parser.add_argument("-p", "--projects", help="Projects CSV filename", required=False, default='projects.csv')
    parser.add_argument("-u", "--settings", help="User Settings CSV filename", required=False, default='settings.csv')
    parser.add_argument("-o", "--output", help="Output (assignment) CSV filename", required=False, default='assignment.csv')
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

    # for debugging, remove when no longer necessary
    print("\n*** Debug print to verify file names ***")
    print("Students csv is: {0}".format(studentsFile))
    print("Projects csv is: {0}".format(projectsFile))
    print("Settings csv is: {0}".format(settingsFile))
    print("Output csv is: {0}".format(outputFile))
    print("Program mode is: {0}".format(programMode))

    return projectsFile, studentsFile, settingsFile, programMode


if __name__ == "__main__":

    # command line parser and error handling
    projFile, studFile, settFile, progMode = main()

    # read, parse, and handle errors of all three csv files
    #projectsHandler(projFile)
    load_csv.studentsHandler(studFile)
    # settingsHandler(settFile) ....will go here


    print("\n*** Program has completed running ***")