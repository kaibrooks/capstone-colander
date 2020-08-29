# Creates .csv files with the assignment column added in and filled.
import pandas as pd
import prints


# insert at line 102 in main.py

def outputCreator(studentFileData, outputFile, optimalSolution):
    df = studentFileData
    # prints.debug(f"{df}") # Before changes output
    # Copy the first file so we don't overwrite it
    df.to_csv(studentFileData, index=False)  # Setting index to False prevents storing of the row numbers in the csv

    df['assignment'] = ''  # If there's no 'Assignment' column, create its header
    new_data = pd.DataFrame({'assignment': optimalSolution})  # Assign data to that header
    df.update(new_data)  # Adding them to the csv

    # Writes/Overwrites to a csv named outputFile.csv
    df.to_csv(outputFile, index=False)
    # prints.debug(f"{df}") # After changes output