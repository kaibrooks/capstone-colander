# Creates .csv files with the assignment column added in and filled.
import pandas as pd
import prints

# insert at line 102 in main.py

def outputCreator(studentFileData, outputFile, optimalSolution):
    df = studentFileData
    prints.debug(f"{df}") # Before changes output

    # Turning optimalSolution back into a series of ints
    optimalSolution.tolist()
    optimalSolution = list(map(int, optimalSolution)) 

    df['assignment'] = ''  # If there's no 'Assignment' column, create its header
    new_data = pd.DataFrame({'assignment': optimalSolution})  # Assign data to that header
    df.update(new_data)  # Adding them to the csv

    # Writes/Overwrites to a csv named outputFile.csv
    df.to_csv(outputFile, index=False, float_format='%g') # float_format g keeps panda's from generating excessively long decimals
    prints.debug(f"{df}") # After changes output