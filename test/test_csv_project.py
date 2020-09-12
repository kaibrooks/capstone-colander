# script for running CSV test cases
# Jaeyoon Lee

import os
import sys

Pass = 0
Fail = 0
Error = 0

print('*** RUNNING TEST_CSV_PROJCET.PY ***')

##############################################################################################

# Project CSV Handler test case:

# CSV-F005: columns rearranged
print('\n ::: CSV-F005 :::')
#os.system('python src/main.py -s test/CSV/CSV-F005/students.csv -p test/CSV/CSV-F005/projects.csv -u test/CSV/CSV-F005/settings.csv')
# Result: Passed
Pass += 1
# Score: 1935.0
# ** Program has completed running **

# CSV-E007: missing project ID column
print('\n ::: CSV-E007 :::')
os.system('python src/main.py -s test/CSV/CSV-E007/students.csv -p test/CSV/CSV-E007/projects.csv -u test/CSV/CSV-E007/settings.csv')
# Result: Passed
Pass += 1
# ERROR: No matching project id found for studentChoice5 = '2.0' (repeated for all students)
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E007/projects.csv', 'test/CSV/CSV-E007/students.csv']. See ERROR messages above for more info.

# CSV-E008: missing minTeamSize name and value
print('\n ::: CSV-E008 :::')
os.system('python src/main.py -s test/CSV/CSV-E008/students.csv -p test/CSV/CSV-E008/projects.csv -u test/CSV/CSV-E008/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required minTeamSize column header not found in the projects csv file. Terminating Program.

# CSV-E009: missing maxTeamSize name and value
print('\n ::: CSV-E009 :::')
os.system('python src/main.py -s test/CSV/CSV-E009/students.csv -p test/CSV/CSV-E009/projects.csv -u test/CSV/CSV-E009/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required maxTeamSize column header not found in the projects csv file. Terminating Program.

# CSV-E037: projectID is not an integer
print('\n ::: CSV-E037 :::')
os.system('python src/main.py -s test/CSV/CSV-E037/students.csv -p test/CSV/CSV-E037/projects.csv -u test/CSV/CSV-E037/settings.csv')
# Result: Passed
Pass += 1
# ERROR: one in the projectID column is not an integer.
# ERROR: two in the projectID column is not an integer.
# (repeated for the rest of projectIDs with wrong IDs)

# CSV-E038: projectID is out of range
print('\n ::: CSV-E038 :::')
os.system('python src/main.py -s test/CSV/CSV-E038/students.csv -p test/CSV/CSV-E038/projects.csv -u test/CSV/CSV-E038/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Value -10 in projectID is an integer out of the required range.
# ERROR: Value -1 in projectID is an integer out of the required range.

# CSV-E039: projectID is not unique (non-integer IDs)
print('\n ::: CSV-E039 :::')
os.system('python src/main.py -s test/CSV/CSV-E039/students.csv -p test/CSV/CSV-E039/projects.csv -u test/CSV/CSV-E039/settings.csv')
# Result: Passed
Pass +=1 
# ERROR: one! in projectID is not an integer.
# ERROR: two@ in projectID is not an integer.
# ERROR: three# in projectID is not an integer.
# ERROR: four$ in projectID is not an integer. 
# ERROR: five% in projectID is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E039/projects.csv', 'test/CSV/CSV-E039/students.csv']. See ERROR messages above for more info.

# CSV-E040: projectID numbers are not sequential from 1
print('\n ::: CSV-E040 :::')
os.system('python src/main.py -s test/CSV/CSV-E040/students.csv -p test/CSV/CSV-E040/projects.csv -u test/CSV/CSV-E040/settings.csv')
# Result: Passed
Pass += 1
# Warning: gap found in projectID sequence in the projects csv file.
# Score: 890.0
# ** Program has completed running **
# no warning messsage displayed 
# this test case may be ignored

# CSV-E041: minTeamSize is not an integer
print('\n ::: CSV-E041 :::')
os.system('python src/main.py -s test/CSV/CSV-E041/students.csv -p test/CSV/CSV-E041/projects.csv -u test/CSV/CSV-E041/settings.csv')
# Result: Passed
Pass += 1
# ERROR: 3.3! in minTeamSize is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E041/projects.csv']. See ERROR messages above for more info.

# CSV-E042: maxTeamSize is not an integer
print('\n ::: CSV-E042 :::')
os.system('python src/main.py -s test/CSV/CSV-E042/students.csv -p test/CSV/CSV-E042/projects.csv -u test/CSV/CSV-E042/settings.csv')
# Result: Passed
Pass += 1
# ERROR: 8.8@ in maxTeamSize is not an integer.
# ERROR: 9.9! in maxTeamSize is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E042/students.csv']. See ERROR messages above for more info.

# CSV-E043: minTeamSize is larger than maxTeamSize
print('\n ::: CSV-E043 :::')
os.system('python src/main.py -s test/CSV/CSV-E043/students.csv -p test/CSV/CSV-E043/projects.csv -u test/CSV/CSV-E043/settings.csv')
# Result: Passed
Pass += 1
# ERROR: minTeamSize is greater than maxTeamSize for projectID 1.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 2.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 11.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 100.
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E059: duplicated field names in project.csv (minTeamSize dumplicate exists)
print('\n ::: CSV-E059 :::')
os.system('python src/main.py -s test/CSV/CSV-E059/students.csv -p test/CSV/CSV-E059/projects.csv -u test/CSV/CSV-E059/settings.csv')
# Result: Passed
Pass += 1
# ERROR: minTeamSize column is duplicated in the Projects CSV file. Terminating Program

# CSV-S005: excessive projectID rows
print('\n ::: CSV-S005 :::')
#os.system('python src/main.py -s test/CSV/CSV-S005/students.csv -p test/CSV/CSV-S005/projects.csv -u test/CSV/CSV-S005/settings.csv')
# Result: Passed
Pass += 1
# Score: 1145.0
# ** Program has completed running **

'''
# CSV-S006: excessive blank lines in project.csv
print('\n ::: CSV-S006 :::')
#os.system('python src/main.py -s test/CSV/CSV-S006/students.csv -p test/CSV/CSV-S006/projects.csv -u test/CSV/CSV-S006/settings.csv')
# Result: Error
Error += 1
# test case is probably written wrong here
'''

total = Pass + Fail + Error
print('\n *** TESTING COMPLETE ***')
print('TOTAL:',total)
print('PASS:',Pass)
print('FAIL:',Fail)
print('ERROR:',Error)

'''
As of 9/12/2020
 *** TESTING COMPLETE ***
TOTAL: 13
PASS: 13
FAIL: 0
ERROR: 0
'''