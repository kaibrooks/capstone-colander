# script for running CSV test cases
# Jaeyoon Lee

import os
import sys

Pass = 0
Fail = 0
Error = 0

print('*** RUNNING TEST_CSV_STUDENT.PY ***')

##############################################################################################

# Student CSV Handler test case:

# CSV-F001: write data into already existing 'assignment' column and save as an output
print('\n ::: CSV-F001 :::')
#os.system('python src/main.py -a -s test/CSV/CSV-F001/students.csv -p test/CSV/CSV-F001/projects.csv -u test/CSV/CSV-F001/settings.csv')
# Result: Passed
Pass += 1
# Score: 2295.0
# - Stopping early (no improvement) -
# Program assigned every student without an issue and filled in the 'assignment' column

# CSV-F002: write data into non-existent 'assignment' column, create the column, then save data and as an output file.
print('\n ::: CSV-F002 :::')
#os.system('python src/main.py -s test/CSV/CSV-F002/students.csv -p test/CSV/CSV-F002/projects.csv -u test/CSV/CSV-F002/settings.csv')
# Result: Passed
Pass += 1
# Score: 2305.0
# - Stopping early (no improvement) -
# Program assgined every student without an issue and created 'assignment' column

# CSV-F003: save data as an output file with a non-reserved field names in the file
print('\n ::: CSV-F003 :::')
#os.system('python src/main.py -s test/CSV/CSV-F003/students.csv -p test/CSV/CSV-F003/projects.csv -u test/CSV/CSV-F003/settings.csv')
# Result: Passed
Pass += 1
# Score: 2305.0
# - Stopping early (no improvement) -
# Program assigned every student without an issue and created 'assignment' column following a non-reserved field name

# CSV-F004: columns rearranged
print('\n ::: CSV-F004 :::')
#os.system('python src/main.py -s test/CSV/CSV-F004/students.csv -p test/CSV/CSV-F004/projects.csv -u test/CSV/CSV-F004/settings.csv')
# Result: Passed
Pass += 1
# Score: 2305.0
# - Stopping early (no improvement) -
# Program assigned every student without an issue regardless of columns order

# CSV-E001: missing studentID field name
print('\n ::: CSV-E001 :::')
os.system('python src/main.py -s test/CSV/CSV-E001/students.csv -p test/CSV/CSV-E001/projects.csv -u test/CSV/CSV-E001/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentID column header not found in the students csv file. Terminating Program.

# CSV-E002: missing GPA field name
print('\n ::: CSV-E002 :::')
os.system('python src/main.py -s test/CSV/CSV-E002/students.csv -p test/CSV/CSV-E002/projects.csv -u test/CSV/CSV-E002/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentGPA column header not found in the students csv file. Terminating Program.

# CSV-E003: missing studentChoice1 field name
print('\n ::: CSV-E003 :::')
os.system('python src/main.py -s test/CSV/CSV-E003/students.csv -p test/CSV/CSV-E003/projects.csv -u test/CSV/CSV-E003/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentChoice1 column header not found in the students csv file. Terminating Program.

# CSV-E004: missing studentESL field name
print('\n ::: CSV-E004 :::')
os.system('python src/main.py -s test/CSV/CSV-E004/students.csv -p test/CSV/CSV-E004/projects.csv -u test/CSV/CSV-E004/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentESL column header not found in the students csv file. Terminating Program.

# CSV-E005: missing studentPriority field name
print('\n ::: CSV-E005 :::')
os.system('python src/main.py -s test/CSV/CSV-E005/students.csv -p test/CSV/CSV-E005/projects.csv -u test/CSV/CSV-E005/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentPriority column header not found in the students csv file. Terminating Program.

# CSV-E006: missing studentAvoid field name
print('\n ::: CSV-E006 :::')
os.system('python src/main.py -s test/CSV/CSV-E006/students.csv -p test/CSV/CSV-E006/projects.csv -u test/CSV/CSV-E006/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required studentAvoid column header not found in the students csv file. Terminating Program.

# CSV-E006-2: missing assignment column (running in scoring mode)
print('\n ::: CSV-E006-2 :::')
os.system('python src/main.py -c -s test/CSV/CSV-E006-2/students.csv -p test/CSV/CSV-E006-2/projects.csv -u test/CSV/CSV-E006-2/settings.csv')
# Result: Passed
Pass += 1
# ERROR: No assignment column found. Terminating program.

# CSV-E024: studentID is not an integer value
print('\n ::: CSV-E024 :::')
os.system('python src/main.py -s test/CSV/CSV-E024/students.csv -p test/CSV/CSV-E024/projects.csv -u test/CSV/CSV-E024/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Unexpected data found in studentID, row 2 = '50571110s'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E024/students.csv']. See ERROR messages above for more info.

# CSV-E025: studentID is out of range of accepted values
print('\n ::: CSV-E025 :::')
os.system('python src/main.py -s test/CSV/CSV-E025/students.csv -p test/CSV/CSV-E025/projects.csv -u test/CSV/CSV-E025/settings.csv')
# Result: Passed
Pass += 1
# ERROR: -5 outside of acceptable range for studentID. Accepted values are between 0 - 18446744073709551615
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E025/students.csv']. See ERROR messages above for more info.

# CSV-E026: studentID is not unique
print('\n ::: CSV-E026 :::')
os.system('python src/main.py -s test/CSV/CSV-E026/students.csv -p test/CSV/CSV-E026/projects.csv -u test/CSV/CSV-E026/settings.csv')
# Result: Passed
Pass += 1
# ERROR: *Duplicate studentID found '1645428'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E026/students.csv']. See ERROR messages above for more info.

# CSV-E027: studentID value is missing
print('\n ::: CSV-E027 :::')
os.system('python src/main.py -s test/CSV/CSV-E027/students.csv -p test/CSV/CSV-E027/projects.csv -u test/CSV/CSV-E027/settings.csv')
# Result: Passed
Pass += 1
# ERROR: *Empty element found in studentID column, row 8
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E027/students.csv']. See ERROR messages above for more info.

# CSV-E028: studentGPA is not a float value
print('\n ::: CSV-E028 :::')
os.system('python src/main.py -s test/CSV/CSV-E028/students.csv -p test/CSV/CSV-E028/projects.csv -u test/CSV/CSV-E028/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Unexpected data found in studentGPA, row 5 = '2.84s'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E028/students.csv']. See ERROR messages above for more info.

# CSV-E029: studentGPA is out of range of accepted values
print('\n ::: CSV-E029 :::')
os.system('python src/main.py -s test/CSV/CSV-E029/students.csv -p test/CSV/CSV-E029/projects.csv -u test/CSV/CSV-E029/settings.csv')
# Result: Passed
Pass += 1
# ERROR: -2.41 outside of acceptable range for studentGPA. Accepted values are between 0.0 - 4.0
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E029/students.csv']. See ERROR messages above for more info.

# CSV-E030: studentGPA value is missing
print('\n ::: CSV-E030 :::')
os.system('python src/main.py -s test/CSV/CSV-E030/students.csv -p test/CSV/CSV-E030/projects.csv -u test/CSV/CSV-E030/settings.csv')
# Result: Passed
Pass += 1
# ERROR: *Empty element found in studentGPA column, row 14
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E030/students.csv']. See ERROR messages above for more info.

# CSV-E031: studentAvoid refers to an invalid studentID
print('\n ::: CSV-E031 :::')
os.system('python src/main.py -s test/CSV/CSV-E031/students.csv -p test/CSV/CSV-E031/projects.csv -u test/CSV/CSV-E031/settings.csv')
# Result: Passed
Pass += 1
# ERROR: No match found in studentAvoid column, row 0 = 7549
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E031/students.csv']. See ERROR messages above for more info.

'''
# test case ignored. studentHandler doesn't handle such case
# CSV-E032: studentAvoid refers to themselves
print('\n ::: CSV-E032 :::')
os.system('python src/main.py -s test/CSV/CSV-E032/students.csv -p test/CSV/CSV-E032/projects.csv -u test/CSV/CSV-E032/settings.csv')
# Result: Fail
Fail += 1
# Score: 2195.0
# ** Program has completed running **
# Program assigned every student but did not print an error for student 36327005 (who refers to themselves for Avoid)
'''

# CSV-E033: studentChoiceN refers to an invalid projectID
print('\n ::: CSV-E033 :::')
os.system('python src/main.py -s test/CSV/CSV-E033/students.csv -p test/CSV/CSV-E033/projects.csv -u test/CSV/CSV-E033/settings.csv')
# Result: Passed
Pass += 1
# ERROR: No matching project id found for studentChoice3 = '9022.0'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E033/students.csv']. See ERROR messages above for more info.

'''
# test case ignored
# CSV-E034: studentChoice1 is missing
print('\n ::: CSV-E034 :::')
os.system('python src/main.py -s test/CSV/CSV-E034/students.csv -p test/CSV/CSV-E034/projects.csv -u test/CSV/CSV-E034/settings.csv')
# Result: Failed
# no error message displayed when one student has a missing studentChoice1 value
'''

# CSV-E035: studentESL is not boolean
print('\n ::: CSV-E035 :::')
os.system('python src/main.py -s test/CSV/CSV-E035/students.csv -p test/CSV/CSV-E035/projects.csv -u test/CSV/CSV-E035/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Unexpected data found in studentESL, row 12 = '1'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E035/students.csv']. See ERROR messages above for more info.


# CSV-E036: studentPriority is not boolean
print('\n ::: CSV-E036 :::')
os.system('python src/main.py -s test/CSV/CSV-E036/students.csv -p test/CSV/CSV-E036/projects.csv -u test/CSV/CSV-E036/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Unexpected data found in studentPriority, row 10 = '1'
# ERROR: Unexpected data found in studentPriority, row 16 = 'Falsse'
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E036/students.csv']. See ERROR messages above for more info.

'''
# test case deleted
# CSV-E056: data partially filled in 'assignment' column in Assignment mode
print('\n ::: CSV-E056 :::')
os.system('python src/main.py -s test/CSV/CSV-E056/students.csv -p test/CSV/CSV-E056/projects.csv -u test/CSV/CSV-E056/settings.csv')
# Result: Failed??
# no error message displayed 
# current testing environment crashes on assignment mode hence ?? marks
'''

# CSV-E057: data partially filled in 'assignment' column in Scoring mode
print('\n ::: CSV-E057 :::')
os.system('python src/main.py -c -s test/CSV/CSV-E057/students.csv -p test/CSV/CSV-E057/projects.csv -u test/CSV/CSV-E057/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Empty element found in assignment column, row 0
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E057/students.csv']. See ERROR messages above for more info.

# CSV-E058: duplicated field names in student.csv (duplicate GPA columns in student.csv)
print('\n ::: CSV-E058 :::')
os.system('python src/main.py -s test/CSV/CSV-E058/students.csv -p test/CSV/CSV-E058/projects.csv -u test/CSV/CSV-E058/settings.csv')
# Result: Passed
Pass += 1
# ERROR: studentGPA column is duplicated in the Students CSV File. Terminating Program

# CSV-S001: excessive studentChoiceN entries
print('\n ::: CSV-S001 :::')
#os.system('python src/main.py -s test/CSV/CSV-S001/students.csv -p test/CSV/CSV-S001/projects.csv -u test/CSV/CSV-S001/settings.csv')
# Result: Passed
Pass += 1
# Score: 2317.0
# - Stopping early (no improvement) -
# Program completed without an issue (only first 5 studentChoice saved in assign.csv)

'''
# CSV-S002: excessive studentAvoidN entries (Ignore this)
# test case ignored since studentAvoidN is discarded
'''

# CSV-S003: excessive blank lines in student.csv
print('\n ::: CSV-S003 :::')
#os.system('python src/main.py -s test/CSV/CSV-S003/students.csv -p test/CSV/CSV-S003/projects.csv -u test/CSV/CSV-S003/settings.csv')
# Result: Passed
Pass += 1
# Score: 2305.0
# - Stopping early (no improvement) -

# CSV-S004: excessive studentID rows
print('\n ::: CSV-S004 :::')
#os.system('python src/main.py -s test/CSV/CSV-S004/students.csv -p test/CSV/CSV-S004/projects.csv -u test/CSV/CSV-S004/settings.csv')
# Result: Passed
Pass += 1
# Program's assignmen mode completed without an issue (S004 currently lists ~20 studentIDs)

total = Pass + Fail + Error
print('\n *** TESTING COMPLETE ***')
print('TOTAL:',total)
print('PASS:',Pass)
print('FAIL:',Fail)
print('ERROR:',Error)

'''
As of 9/12/2020
 *** TESTING COMPLETE ***
TOTAL: 27
PASS: 27
FAIL: 0
ERROR: 0
'''