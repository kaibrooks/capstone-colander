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
import write_csv
import assign
import score
import prints
import write_csv
import time

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
prints.gen("Program started {0}".format(now))  # print it


def main():

    # default program mode
    programMode = 'Assignment'

    # accepted command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--students", help="Students CSV filename", required=False, default='../io/students.csv')
    parser.add_argument("-p", "--projects", help="Projects CSV filename", required=False, default='../io/projects.csv')
    parser.add_argument("-u", "--settings", help="User Settings CSV filename", required=False, default='../io/settings.csv')
    parser.add_argument("-o", "--output", help="Output (assignment) CSV filename", required=False, default='../io/assign.csv')
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
            prints.warn("both Scoring (-c) and Assignment (-a) modes selected. Program will run in Assignment mode.")

    # when running program in Assignment mode
    # if output user provided already exists when running in Assignment mode, warn user
    # or if directory of user provided output does not exist, terminate program
    if programMode == 'Assignment':
        if os.path.exists(outputFile):
            prints.warn("output file {0} already exists in the directory and will be overwritten with new assignments.".format(outputFile))
        elif not os.path.isdir(os.path.dirname(os.path.abspath(outputFile))):
            prints.err("directory for output file {0} does NOT exist.".format(outputFile))

    # function to verify user provided files exist and that they are csv files by attempting to read file into a data structure
    # returns data structure assuming all files are csv files
    # otherwise, sets an errorFlag to True to terminate program after each filed is checked
    main.errorFlag = False
    def csvFileCheck(csvFileName):
        if not os.path.exists(csvFileName):
            # if original filename not found, add .csv extension and check again
            tempFileName = csvFileName + '.csv'
            if not os.path.exists(tempFileName):
                prints.logerr("{0} csv file can not be found.".format(csvFileName))
                main.errorFlag = True
                return 0, 0
            csvFileName = tempFileName
        try:
            tempDataStruct = pd.read_csv(csvFileName)
        except ValueError:
            prints.logerr("{0} is not a valid csv file.".format(csvFileName))
            main.errorFlag = True
            return 0, 0
        return tempDataStruct, csvFileName

    # load projects csv file
    settingsData, settingsFile = csvFileCheck(settingsFile)
    projectsData, projectsFile = csvFileCheck(projectsFile)
    studentsData, studentsFile = csvFileCheck(studentsFile)

    # terminate program if any errors detected in the csvFileCheck function
    if main.errorFlag is True:
        prints.err("Program Terminated in command line handler. See messages(s) above for additional information.")

    return settingsData, projectsData, studentsData, studentsFile, outputFile, programMode


if __name__ == "__main__":

    # command line parser and error handling
    settingsFileData, projectsFileData, studentsFileData, studentsFile, outputFile, progMode = main()

    # read, parse, and handle errors of all three csv files
    load_csv.settingsHandler(settingsFileData)
    load_csv.projectsHandler(projectsFileData)
    load_csv.studentsHandler(studentsFile, progMode)

    if progMode == 'Assignment':
        t0 = time.time()
        optimalSolution = assign.run_ga()
        run_time = time.time() - t0
        run_time = str(round(run_time, 2))
        prints.gen("\nRun time: {0} seconds".format(run_time))
        write_csv.outputCreator(studentsFileData, outputFile, optimalSolution)
    elif progMode == 'Scoring':
        finalScore = score.scoringMode(load_csv.studentAssignment)
        prints.gen("Assignment Score: {0}".format(finalScore))

    prints.gen("** Program has completed running **")