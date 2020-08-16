# capstone colander

# main.py parses command line arguments, handles command line errors,
# and calls remaining functions from other files.

import argparse
import os
from datetime import datetime
import pandas as pd
# imports below are other python files used in this project
# which are required to call their functions from main
import load_csv
import assign
import score
import prints

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
prints.gen("Program started {0}".format(now))  # print it


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
        if argument.score:
            prints.printWarning("both Scoring (-c) and Assignment (-a) modes selected. Program will run in Assignment mode.")

    # if output user provided already exists when running in Assignment mode, warn user
    if programMode == 'Assignment' and os.path.exists(outputFile):
        prints.warn("output file {0} already exists in the directory and will be overwritten with new assignments.".format(outputFile))

    # function to verify user provided files exist and that they are csv files by attempting to read file into a data structure
    # returns data structure assuming all files are csv files
    # otherwise, sets an errorFlag to True to terminate program after each filed is checked
    main.errorFlag = False
    def csvFileCheck(csvFileName):
        if not os.path.exists(csvFileName):
            # if original filename not found, add .csv extension and check again
            tempFileName = csvFileName + '.csv'
            if not os.path.exists(tempFileName):
                prints.logerr("{0} csv file can not be found. Terminating program.".format(csvFileName))
                main.errorFlag = True
                return 0
            csvFileName = tempFileName
        try:
            tempDataStruct = pd.read_csv(csvFileName)
        except ValueError:
            pt.logerr("{0} is not a valid csv file. Terminating Program.".format(csvFileName))
            main.errorFlag = True
            return 0
        return tempDataStruct

    # load projects csv file
    settingsData = csvFileCheck(settingsFile)
    projectsData = csvFileCheck(projectsFile)
    studentsData = csvFileCheck(studentsFile)

    # terminate program if any errors detected in the csvFileCheck function
    if main.errorFlag is True:
        prints.err("Program Terminated. See messages(s) above for additional information.")

    return settingsData, projectsData, studentsData, studentsFile, programMode


if __name__ == "__main__":

    # command line parser and error handling
    settingsFileData, projectsFileData, studentsFileData, studentsFile, progMode = main()

    # read, parse, and handle errors of all three csv files
    load_csv.settingsHandler(settingsFileData)
    load_csv.projectsHandler(projectsFileData)
    load_csv.studentsHandler(studentsFile, progMode)

    if progMode == 'Assignment':
        optimalSolution = assign.run_ga()
    elif progMode == 'Scoring':
        finalScore = score.scoringMode(load_csv.studentAssignment)
        prints.gen("Assignment Score: {0}".format(finalScore))

    prints.gen("** Program has completed running **")