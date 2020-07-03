# load_csv
# loads a csv and reads it (imagine that)

import pandas as pd # loads csv
import random # make a random assignment for demoing

print("*** RUNNING LOAD_CSV.PY ***\n")

## load CSV
df = pd.read_csv('/io/students.csv') # load a file as a variable
print('Input CSV data')
print(df) # output it

# examples of data analysis
print("Total Students : ", df['ID'].count())
print("Average GPA    : ", df['GPA'].mean())

## add assignments to the file
# copy the first file so we don't overwrite it
df.to_csv('/io/students.csv', index=False)

## 'assign' a random project
# make an array of random numbers
project_assignment = []
for i in range(0, len(df)):
    n = random.randint(1,5) # assign random group
    project_assignment.append(n)

# add that column to the dataframe
df['Assignment'] = '' # if no 'Assignment' column, create it
new_data = pd.DataFrame({'Assignment': project_assignment}) # project assignments
df.update(new_data) # add them to the csv

## write a new csv
df.to_csv('/io/new_students.csv', index=False)
print('\nNew CSV data with assignments')
print(df) # output it