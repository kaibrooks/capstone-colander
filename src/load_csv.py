# load_csv
# loads a csv and reads it (imagine that)

import pandas as pd # loads csv

print("*** RUNNING LOAD_CSV.PY ***\n")

## load CSV
df = pd.read_csv ('/io/students.csv') # load a file as a variable
print('CSV data')
print(df) # output it

# examples of data analysis
print("Total Students : ", df['ID'].count())
print("Average GPA    : ", df['GPA'].mean())

## add assignments to the file
# copy the first file so we don't overwrite it
df.to_csv('/io/new_students.csv', index=False)

# add project assignments
new_data = pd.DataFrame({'Assignment': ['Superman NanoCape', 'Bee Swarm Laser', 'Gravity Inverter', 'Moon Tractor Beam']}) # project assignments
df.update(new_data) # add them to the csv

## write new csv
df.to_csv('/io/new_students.csv', index=False)
print(df) # output it