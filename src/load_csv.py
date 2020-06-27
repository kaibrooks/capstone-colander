# load_csv
# loads a csv and reads it (imagine that)

import pandas as pd # loads csv

print("*** RUNNING LOAD_CSV.PY ***\n")

# read CSV
df = pd.read_csv ('io/data.csv') # load a file as a variable
print('CSV data')
print(df) # output it

# examples of data analysis
print("Total Students : ", df['ID'].count())
print("Average GPA    : ", df['GPA'].mean())
print("Number of CE's : ", df['Major'].str.count('CE').sum())
print("GPA of CE's    : ", ) # ???
print(df.groupby('Major').size())

# shuffle
ds = df.sample(frac=1) # frac = portion of rows to shuffle, 1=all
print('\nShuffle')
print(ds)

# sort alphabetically
dt = df.sort_values(by=['Name'])
print('\nSort alphabetically')
print(dt)

# sort by GPA
du = df.sort_values(by=['GPA'], ascending=False)
print('\nSort by GPA')
print(du)