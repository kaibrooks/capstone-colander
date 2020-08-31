# Creates .csv files with the assignment column added in and filled.
import pandas as pd
import prints
import load_csv

# insert at line 102 in main.py

def outputCreator(studentFileData, outputFile, optimalSolution):
    df = studentFileData

    # Matching projectID's to their indexed number in optimalSolution
    for i in range(len(optimalSolution)):
        optimalSolution[i] = load_csv.projectIDs[int(optimalSolution[i])]

    df['assignment'] = ''  # If there's no 'Assignment' column, create its header
    new_data = pd.DataFrame({'assignment': optimalSolution})  # Assign data to that header
    df.update(new_data)  # Adding them to the csv
    df = df.astype({"assignment": int}) # Treats assignment outputs as ints

    prints.debug(f"{df} After") # After changes output
    # Writes/Overwrites to a csv named outputFile.csv
    df.to_csv(outputFile, index=False)