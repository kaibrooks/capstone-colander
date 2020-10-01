
# Creates .csv files with the assignment column added in and filled.
import pandas as pd
import prints
import load_csv


def outputCSV(studentFileData, outputFileName, optimalSolution):
    # optimalSolution is a numpy array
    # Matching projectID's to their indexed number in optimalSolution
    for i in range(len(optimalSolution)):
        optimalSolution[i] = load_csv.projectIDs[int(optimalSolution[i])]

    studentFileData['assignment'] = ''  # If there's no 'Assignment' column, create its header
    assignments = pd.DataFrame({'assignment': optimalSolution})  # Creating the dataframe
    studentFileData.update(assignments)  # Appending the dataframe assignments to studentFileData
    studentFileData = studentFileData.astype({"assignment": int})  # Treats assignment outputs as ints

    prints.debug(f"\n========outputCSV========\n\n{studentFileData} After")  # After changes output
    # Writes/Overwrites to a csv named outputFileName
    studentFileData.to_csv(outputFileName, index=False, float_format="%.3f")
