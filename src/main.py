# capstone colander

# main.py parses command line arguments, handles command line errors,
# and calls remaining functions from other files.

import sys
import argparse
import os
from datetime import datetime
import pandas as pd
import load_csv
#import run_ga ...when GA is completed and tested
#import scoring ...when Scoring is completed and tested

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
print("Program started", now)  # print it


def main():
    global studentsFile

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

    # if output user provided already exists when running in Assignment mode, terminate program
    if programMode == 'Assignment' and os.path.exists(outputFile):
        sys.exit("ERROR: {0} already exists in the directory. Enter a unique output file name using the -o FILENAME command. Terminating Program.".format(outputFile))

    # function to verify user provided files exist and that they are csv files
    def csvFileCheck(csvFileName):
        if not os.path.exists(csvFileName):
            # if original filename not found, add .csv extension and check again
            tempFileName = csvFileName + '.csv'
            if not os.path.exists(tempFileName):
                sys.exit("ERROR: {0} csv file can not be found. Terminating Program.".format(csvFileName))
            csvFileName = tempFileName
        try:
            tempDataStruct = pd.read_csv(csvFileName)
        except ValueError:
            sys.exit("ERROR: {0} is not a valid csv file. Terminating Program.".format(csvFileName))
        return tempDataStruct

    # load projects csv file
    settingsData = csvFileCheck(settingsFile)
    projectsData = csvFileCheck(projectsFile)
    studentsData = csvFileCheck(studentsFile)

    return settingsData, projectsData, studentsData, programMode


if __name__ == "__main__":

    # command line parser and error handling
    settingsFileData, projectsFileData, studentsFileData, progMode = main()

    # read, parse, and handle errors of all three csv files
    load_csv.settingsHandler(settingsFileData)
    load_csv.projectsHandler(projectsFileData)
    load_csv.studentsHandler(studentsFile) 

    if progMode == 'Assignment':
        print("\nProgram running in Assignment mode with a max run time of {0} minutes.".format(load_csv.maxRunTime))
        #run_ga.geneticAlgorithmFunction() ...when complete, call GA for assignment mode
    elif progMode == 'Scoring':
        print("\nProgram running in Scoring mode.")
        #scoring.scoreFunction() ...when complete, call Scoring function

    print("\n*** Program has completed running ***")