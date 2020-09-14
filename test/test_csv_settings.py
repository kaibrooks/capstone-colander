# script for running CSV test cases
# Jaeyoon Lee

import os
import sys

Pass = 0
Fail = 0
Error = 0

print('*** RUNNING TEST_CSV_SETTINGS.PY ***')

##############################################################################################

# Settings CSV Handler test case:

# CSV-F006: columns rearranged
print('\n ::: CSV-F006 :::')
#os.system('python src/main.py -s test/CSV/CSV-F006/students.csv -p test/CSV/CSV-F006/projects.csv -u test/CSV/CSV-F006/settings.csv')
# Result: Passed
Pass += 1
# Score: 1990.0
# ** Program has completed running **

# CSV-E010: missing field name 'name'
print('\n ::: CSV-E010 :::')
os.system('python src/main.py -s test/CSV/CSV-E010/students.csv -p test/CSV/CSV-E010/projects.csv -u test/CSV/CSV-E010/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required name column header not found in the settings csv file. Terminating Program.
# name is 'nam' in this test case settings.csv file, hence the error

# CSV-E011: missing field name 'min'
print('\n ::: CSV-E011 :::')
os.system('python src/main.py -s test/CSV/CSV-E011/students.csv -p test/CSV/CSV-E011/projects.csv -u test/CSV/CSV-E011/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required min column header not found in the settings csv file. Terminating Program.
# min is 'minz' in this test case, hence the error

# CSV-E012: missing field name 'max'
print('\n ::: CSV-E012 :::')
os.system('python src/main.py -s test/CSV/CSV-E012/students.csv -p test/CSV/CSV-E012/projects.csv -u test/CSV/CSV-E012/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required max column header not found in the settings csv file. Terminating Program.
# max is 'max_amooy' in this test case, hence the error

# CSV-E013: missing field name 'points'
print('\n ::: CSV-E013 :::')
os.system('python src/main.py -s test/CSV/CSV-E013/students.csv -p test/CSV/CSV-E013/projects.csv -u test/CSV/CSV-E013/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required points column header not found in the settings csv file. Terminating Program. 
# points is SCORE in this test case, hence the error

# CSV-E014: missing name field for lowGPAThreshold
print('\n ::: CSV-E014 :::')
os.system('python src/main.py -s test/CSV/CSV-E014/students.csv -p test/CSV/CSV-E014/projects.csv -u test/CSV/CSV-E014/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required lowGPAThreshold row not found in the settings csv file. Terminating Program.

# CSV-E015: missing name field for MaxLowGPAStudents
print('\n ::: CSV-E015 :::')
os.system('python src/main.py -s test/CSV/CSV-E015/students.csv -p test/CSV/CSV-E015/projects.csv -u test/CSV/CSV-E015/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required maxLowGPAStudents row not found in the settings csv file. Terminating Program. 

# CSV-E016: missing name field for MaxESLStudents
print('\n ::: CSV-E016 :::')
os.system('python src/main.py -s test/CSV/CSV-E016/students.csv -p test/CSV/CSV-E016/projects.csv -u test/CSV/CSV-E016/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required maxESLStudents row not found in the settings csv file. Terminating Program.

# CSV-E017: missing name field for weightMaxLowGPAStudents
print('\n ::: CSV-E017 :::')
os.system('python src/main.py -s test/CSV/CSV-E017/students.csv -p test/CSV/CSV-E017/projects.csv -u test/CSV/CSV-E017/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightMaxLowGPAStudents row not found in the settings csv file. Terminating Program. 

# CSV-E018: missing name field for weightMaxESLStudents
print('\n ::: CSV-E018 :::')
os.system('python src/main.py -s test/CSV/CSV-E018/students.csv -p test/CSV/CSV-E018/projects.csv -u test/CSV/CSV-E018/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightMaxESLStudents row not found in the settings csv file. Terminating Program. 

# CSV-E019: missing name field for weightMinTeamSize (previoulsy weightTeamSize)
print('\n ::: CSV-E019 :::')
os.system('python src/main.py -s test/CSV/CSV-E019/students.csv -p test/CSV/CSV-E019/projects.csv -u test/CSV/CSV-E019/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightMinTeamSize row not found in the settings csv file. Terminating Program.

'''
# same for weightMaxTeamSize as above
# CSV-E019-2: missing name field for weightTeamSize
print('\n ::: CSV-E019 :::')
os.system('python src/main.py -s test/CSV/CSV-E019/students.csv -p test/CSV/CSV-E019/projects.csv -u test/CSV/CSV-E019/settings.csv')
# Result: Passed
# ERROR: Required weightTeamSize row not found in the settings csv file. Terminating Program.
'''
# CSV-E020: missing name field for weightStudentPriority
print('\n ::: CSV-E020 :::')
os.system('python src/main.py -s test/CSV/CSV-E020/students.csv -p test/CSV/CSV-E020/projects.csv -u test/CSV/CSV-E020/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightStudentPriority row not found in the settings csv file. Terminating Program.

# CSV-E021: missing name field for weightStudentChoice1
print('\n ::: CSV-E021 :::')
os.system('python src/main.py -s test/CSV/CSV-E021/students.csv -p test/CSV/CSV-E021/projects.csv -u test/CSV/CSV-E021/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightStudentChoice1 row not found in the settings csv file. Terminating Program.

# CSV-E022: missing name field for weightAvoid
print('\n ::: CSV-E022 :::')
os.system('python src/main.py -s test/CSV/CSV-E022/students.csv -p test/CSV/CSV-E022/projects.csv -u test/CSV/CSV-E022/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required weightAvoid row not found in the settings csv file. Terminating Program.

# CSV-E023: missing name field for Efforts
print('\n ::: CSV-E023 :::')
os.system('python src/main.py -s test/CSV/CSV-E023/students.csv -p test/CSV/CSV-E023/projects.csv -u test/CSV/CSV-E023/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Required effort row not found in the settings csv file. Terminating Program.

# CSV-E044: lowGPAThreshold is not a float
print('\n ::: CSV-E044 :::')
os.system('python src/main.py -s test/CSV/CSV-E044/students.csv -p test/CSV/CSV-E044/projects.csv -u test/CSV/CSV-E044/settings.csv')
# Result: Passed
Pass += 1
# ERROR: The lowGPAThreshold 'min' value is not a float.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E044/settings.csv']. See ERROR messages above for more info.

# CSV-E045: lowGPAThreshold is out of range
print('\n ::: CSV-E045 :::')
os.system('python src/main.py -s test/CSV/CSV-E045/students.csv -p test/CSV/CSV-E045/projects.csv -u test/CSV/CSV-E045/settings.csv')
# Result: Passed
Pass += 1
# ERROR: lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E045/settings.csv']. See ERROR messages above for more info.

# CSV-E046: MaxLowGPAThreshold is not an integer
print('\n ::: CSV-E046 :::')
os.system('python src/main.py -s test/CSV/CSV-E046/students.csv -p test/CSV/CSV-E046/projects.csv -u test/CSV/CSV-E046/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Value 2.33 in maxLowGPAStudents is not a required int.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E046/settings.csv']. See ERROR messages above for more info.

# CSV-E047: MaxLowGPAStudents is out of range
print('\n ::: CSV-E047 :::')
os.system('python src/main.py -s test/CSV/CSV-E047/students.csv -p test/CSV/CSV-E047/projects.csv -u test/CSV/CSV-E047/settings.csv')
# Result: Passed
Pass += 1
# ERROR: ERROR: Value 0.0 in maxLowGPAStudents is an integer out of the required range.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E047/settings.csv']. See ERROR messages above for more info.

# CSV-E048: MaxESLStudents is not an integer
print('\n ::: CSV-E048 :::')
os.system('python src/main.py -s test/CSV/CSV-E048/students.csv -p test/CSV/CSV-E048/projects.csv -u test/CSV/CSV-E048/settings.csv')
# Result: Passed
Pass += 1
# ERROR: '$E' in the maxESLStudents row is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E048/settings.csv']. See ERROR messages above for more info.

# CSV-E049: MaxESLStudents is out of range
print('\n ::: CSV-E049 :::')
os.system('python src/main.py -s test/CSV/CSV-E049/students.csv -p test/CSV/CSV-E049/projects.csv -u test/CSV/CSV-E049/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Value 1.8446744073709552e+19 in maxESLStudents is an integer out of the required range.
# the program gives the correct error message, 
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E049/settings.csv']. See ERROR messages above for more info.

# CSV-E050: Effort is not an integer
print('\n ::: CSV-E050 :::')
#os.system('python src/main.py -s test/CSV/CSV-E050/students.csv -p test/CSV/CSV-E050/projects.csv -u test/CSV/CSV-E050/settings.csv')
# Result: Passed
Pass += 1
# Warning: valid 'effort' value not found in the settings csv. Running with default value.
# Score: 1980.0
# ** Program has completed running **

# CSV-E051: Effort is out of range
print('\n ::: CSV-E051 :::')
#os.system('python src/main.py -s test/CSV/CSV-E051/students.csv -p test/CSV/CSV-E051/projects.csv -u test/CSV/CSV-E051/settings.csv')
# Result: Passed
Pass += 1
# Warning: 'effort' in the settings csv is not an int between 1 and 100. Running with default value of 20. 
# Score: 1980.0
# ** Program has completed running **

# CSV-E052: weightMaxLowGPAStudents is not an integer
print('\n ::: CSV-E052 :::')
os.system('python src/main.py -s test/CSV/CSV-E052/students.csv -p test/CSV/CSV-E052/projects.csv -u test/CSV/CSV-E052/settings.csv')
# Result: Passed
Pass += 1
# ERROR: zero in the weightMaxLowGPAStudents row is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E052/settings.csv']. See ERROR messages above for more info.

# CSV-E053: weightMaxLowGPAStudents is out of range
print('\n ::: CSV-E053 :::')
os.system('python src/main.py -s test/CSV/CSV-E053/students.csv -p test/CSV/CSV-E053/projects.csv -u test/CSV/CSV-E053/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Value -1.0 in the weightMaxLowGPAStudents column must be an integer greater than zero and less than 2^64.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E053/settings.csv']. See ERROR messages above for more info.

# CSV-E054: weightMaxESLStudents is not an integer
print('\n ::: CSV-E054 :::')
os.system('python src/main.py -s test/CSV/CSV-E054/students.csv -p test/CSV/CSV-E054/projects.csv -u test/CSV/CSV-E054/settings.csv')
# Result: Passed
Pass += 1
# ERROR: $!`[] in the weightMaxESLStudents row is not an integer.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E054/settings.csv']. See ERROR messages a messages above for more info.

# CSV-E055: weightMaxESLStudents is out of range
print('\n ::: CSV-E055 :::')
os.system('python src/main.py -s test/CSV/CSV-E055/students.csv -p test/CSV/CSV-E055/projects.csv -u test/CSV/CSV-E055/settings.csv')
# Result: Passed
Pass += 1
# ERROR: Value -1337.0 in weightMaxESLStudents is an integer out of the required range.
# ERROR: Program terminating due to errors in the following files: ['test/CSV/CSV-E055/settings.csv']. See ERROR messages above for more info.

# CSV-E060: duplicated field names in settings.csv
print('\n ::: CSV-E060 :::')
os.system('python src/main.py -s test/CSV/CSV-E060/students.csv -p test/CSV/CSV-E060/projects.csv -u test/CSV/CSV-E060/settings.csv')
# Result: Passed
Pass += 1
# ERROR: projectID column is duplicated in the Projects CSV file. Terminating Program

'''
# CSV-S007: excessive blank lines in settings.csv
print('\n ::: CSV-S007 :::')
os.system('python src/main.py -a -s test/CSV/CSV-S007/students.csv -p test/CSV/CSV-S007/projects.csv -u test/CSV/CSV-S007/settings.csv')
# Result: Failed
Fail += 1
# ERROR: test/CSV/CSV-S007/settings.csv is not a valid csv file.
# ERROR: Program Terminated in command line handler. See messages(s) above for additional information.
# perhaps the test case is written wrong
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
TOTAL: 28
PASS: 28
FAIL: 0
ERROR: 0
'''