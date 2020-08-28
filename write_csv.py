# Creates .csv files with the assignment column added in and filled.
import pandas as pd
import prints
import os

#insert at line 102 in main.py

def outputCreator(studentFileData, outputFile, optimalSolution):
    #change program to use studentFileData structure and now just the name.
    df = pd.read_csv(studentFileData) # load a file as a variable
    #df = studentFileData
    prints.debug(f"{df}") # Before changes output
    
    # Copy the first file so we don't overwrite it
    df.to_csv(studentFileData, index = False) # Setting index to False prevents storing of the row numbers in the csv
 
    df['assignment'] = '' # If there's no 'Assignment' column, create its header
    new_data = pd.DataFrame({'assignment': optimalSolution}) # Assign data to that header
    df.update(new_data) # Adding them to the csv

    i = 1
    z = len(outputFile)
    while (os.path.isfile(outputFile)):
        #outputFile = outputFile[:z] + str(i) + outputFile[z + 1:]
        outputFile = outputFile[:z - 4] + str(i) + '.csv' # Creates a new file if the old one exists named outputFile"i".csv
        i += 1
    
    # Writes/Overwrites to a csv named outputFile.csv
    df.to_csv(outputFile, index=False)
    prints.debug(f"{df}") # After changes output

optimalSolution = [1, 7, 7, 4]
inputFile = 'students.csv'
outputFile = 'koa.csv'
outputCreator(inputFile, outputFile, optimalSolution)