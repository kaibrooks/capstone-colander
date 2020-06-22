# load_csv
# loads a csv and reads it (imagine that)

import pandas as pd # loads csv

print("*** RUNNING LOAD_CSV.PY ***\n")

# read CSV
df = pd.read_csv ('data/data.csv') # load a file as a variable

print(df.head(50)) # print first n rows

# examples of data analysis
print("Total Students : ", df['ID'].count())
print("Average GPA    : ", df['GPA'].mean())
print("Number of CE's : ", df['Major'].str.count('CE').sum())
print("GPA of CE's    : ", ) # ???
print(df.groupby('Major').size())