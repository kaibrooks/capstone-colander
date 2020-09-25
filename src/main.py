# capstone colander

# main.py parses command line arguments, handles command line errors,
# and calls remaining functions from other files.

import argparse
import os
from datetime import datetime
import time
import pandas as pd
# imports below are other python files used in this project
# which are required to call their functions from main
import load_csv
import write_csv
import assign
import score
import prints

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # get the date/time
prints.gen("Program started {0}".format(now))  # print it
start = time.time()

# default program mode
programMode = 'Assignment'

# initialize score breakdown option to be disabled
scoreBreakdown = False

# initialize default GA parameters
mutationProbability = 0.02
populationSize = 100
eliteRatio = 0.01
crossoverProbability = 0.5
parentsPortion = 0.3

def argumentParser():
    global scoreBreakdown
    global programMode

    global mutationProbability
    global populationSize
    global eliteRatio
    global crossoverProbability
    global parentsPortion

    # accepted command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--students", help="Students CSV filename", required=False, default='io/students.csv')
    parser.add_argument("-p", "--projects", help="Projects CSV filename", required=False, default='io/projects.csv')
    parser.add_argument("-u", "--settings", help="Settings CSV filename", required=False, default='io/settings.csv')
    parser.add_argument("-o", "--output", help="Output CSV filename", required=False, default='io/assign.csv')
    parser.add_argument("-a", "--assign", help="Run program in Assignment mode", required=False, action='store_true')
    parser.add_argument("-c", "--score", help="Run the program in Scoring mode", required=False, action='store_true')
    parser.add_argument("-b", "--breakdown", help="Display score breakdown", required=False, action='store_true')
    parser.add_argument("-mutation", "--mutation", help="Mutation Probability", required=False, default=0.02)
    parser.add_argument("-population", "--population", help="Population Size", required=False, default=100)
    parser.add_argument("-elite", "--elite", help="Population Size", required=False, default=0.01)
    parser.add_argument("-crossover", "--crossover", help="Population Size", required=False, default=0.5)
    parser.add_argument("-parents", "--parents", help="Population Size", required=False, default=0.3)

    argument = parser.parse_args()

    # assign csv file names and mode preference
    if argument.students:
        studentsFileName = argument.students
    if argument.projects:
        projectsFileName = argument.projects
    if argument.settings:
        settingsFileName = argument.settings
    if argument.output:
        outputFileName = argument.output
    if argument.score:
        programMode = 'Scoring'
    if argument.assign:
        programMode = 'Assignment'
        if argument.score:
            prints.warn("both Scoring (-c) and Assignment (-a) modes selected. Program will run in Assignment mode.")
    if argument.breakdown:
        scoreBreakdown = True
    if argument.mutation:
        mutationProbability = float(argument.mutation)
        if mutationProbability < 0.0 or mutationProbability > 1.0:
            prints.warn("Mutation Probability is out of required range, defaulting to 0.02")
            mutationProbability = 0.02
    if argument.population:
        try:
            populationSize = int(argument.population)
        except ValueError:
            prints.warn("Population Size is not an integer, defaulting to 100")
            populationSize = 100
    if argument.elite:
        eliteRatio = float(argument.elite)
        if eliteRatio < 0.0 or eliteRatio > 1.0:
            prints.warn("Elite Ratio is out of required range, defaulting to 0.01")
            eliteRatio = 0.01
    if argument.crossover:
        crossoverProbability = float(argument.crossover)
        if crossoverProbability < 0.0 or crossoverProbability > 1.0:
            prints.warn("Crossover Probability is out of required range, defaulting to 0.5")
            crossoverProbability = 0.5
    if argument.parents:
        parentsPortion = float(argument.parents)
        if parentsPortion < 0.0 or parentsPortion > 1.0:
            prints.warn("Parents Portion is out of required range, defaulting to 0.3")
            parentsPortion = 0.3

    # when running program in Assignment mode
    # if output user provided already exists when running in Assignment mode, warn user
    # or if directory of user provided output does not exist, terminate program
    if programMode == 'Assignment':
        if os.path.exists(outputFileName):
            prints.warn("output file {0} already exists in the directory and will be overwritten with new assignments."
                        .format(outputFileName))
        elif not os.path.isdir(os.path.dirname(os.path.abspath(outputFileName))):
            prints.err("directory for output file {0} does NOT exist.".format(outputFileName))

    return studentsFileName, projectsFileName, settingsFileName, outputFileName


# flag to keep track if errors found so the program can terminate
# after all files are checked, not immediately when one error is found
errFlag = False


# function to verify user provided files exist and that they are csv files
# by attempting to read file into a data structure
# returns data structure assuming all files are csv files
# otherwise, sets errFlag to True to terminate program after each filed is checked
def csvFileCheck(csvFileName):
    global errFlag

    if not os.path.exists(csvFileName):
        # if original filename not found, add .csv extension and check again
        tempFileName = csvFileName + '.csv'
        if not os.path.exists(tempFileName):
            prints.logerr("{0} csv file can not be found.".format(csvFileName))
            errFlag = True
            return 0, 0
        csvFileName = tempFileName
    try:
        tempDataStruct = pd.read_csv(csvFileName)
    except ValueError:
        prints.logerr("{0} is not a valid csv file.".format(csvFileName))
        errFlag = True
        return 0, 0
    return tempDataStruct, csvFileName


if __name__ == "__main__":

    # command line parser and error handling
    studentFile, projectFile, settingFile, outputFile = argumentParser()

    # load csv files. returns csv file dataframe and final csv filename
    settingsFileData, settingsFile = csvFileCheck(settingFile)
    projectsFileData, projectsFile = csvFileCheck(projectFile)
    studentsFileData, studentsFile = csvFileCheck(studentFile)

    # terminate program if any errors detected in the csvFileCheck function
    if errFlag:
        prints.err("Program Terminated in command line handler. See messages(s) above for additional information.")

    # read, parse, and handle errors of all three csv files
    # errFlag used if errors are found in the csv files
    # violating csv files are appended to array to inform user which file(s) the errors came from
    errFiles = []
    if load_csv.settingsHandler(settingsFileData):
        errFiles.append(settingsFile)
    if load_csv.projectsHandler(projectsFileData):
        errFiles.append(projectsFile)
    if load_csv.studentsHandler(studentsFileData, programMode):
        errFiles.append(studentsFile)

    if errFiles:
        prints.err("Program terminating due to errors in the following files: {0}."
                   " See ERROR messages above for more info.".format(errFiles))
    if programMode == 'Assignment':
        optimalSolution = assign.run_ga(mutationProbability, populationSize, eliteRatio, crossoverProbability, parentsPortion)
        optimalSolution.tolist()
        optimalSolution = list(map(int, optimalSolution))
        if scoreBreakdown:
            prints.breakMode = True
            score.scoringMode(optimalSolution)
        write_csv.outputCSV(studentsFileData, outputFile, optimalSolution)
    elif programMode == 'Scoring':
        if scoreBreakdown:
            prints.breakMode = True
        finalScore = score.scoringMode(load_csv.studentAssignment)
        prints.gen("Assignment Score: {0}".format(finalScore))

    end = time.time()
    runTime = round(((end - start) / 60),2)
    prints.gen("\n** Program has completed with a run time of {0} minutes **".format(runTime))
