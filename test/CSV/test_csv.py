# script for running tests
# CSV Handler test cases report
# KNOWN ISSUES with current csv format:
# studentHandler will have problems with test csv files since 
# studentAvoid 1 and 2 exist -> only studentAvoid is accepted
# studentESL and studentPriority are cauase errors due to values being boolean

# Test case example
# CSV-Sample: Description
# Result: (Pass or fail)
# ERROR: error/warning message displayed to the terminal
# *additional comments*

print('*** RUNNING TEST_CSV.PY ***')

##############################################################################################

# Student CSV Handler test case:

# CSV-F001: write data into already existing 'assignment' column and save as an output
print('\n ::: CSV-F001 :::')
# Result: Unknown
# current testing build crashes in score.py

# CSV-F002: write data into non-existent 'assignment' column, create the column, then save data and as an output file.
print('\n ::: CSV-F002 :::')
# Result: Unknown
# current testing build crashes in score.py

# CSV-F003: save data as an output file with a non-reserved field names in the file
print('\n ::: CSV-F003 :::')
# Result: Unknown
# output assignment writer not ready for testing

# CSV-F004: columns rearranged
print('\n ::: CSV-F004 :::')
# Result: Passed
# no issue when columns are rearranged

# CSV-E001: missing studentID field name
print('\n ::: CSV-E001 :::')
# Result: Passed
# ERROR: Required studentID column header not found in the students csv file. Terminating Program.

# CSV-E002: missing GPA field name
print('\n ::: CSV-E002 :::')
# Result: Passed
# ERROR: Required studentGPA column header not found in the students csv file. Terminating Program.

# CSV-E003: missing studentChoice1 field name
print('\n ::: CSV-E003 :::')
# Result: Passed
# ERROR: Required studentChoice1 column header not found in the students csv file. Terminating Program.

# CSV-E004: missing studentESL field name
print('\n ::: CSV-E004 :::')
# Result: Passed
# ERROR: Required studentESL column header not found in the students csv file. Terminating Program.

# CSV-E005: missing studentPriority field name
print('\n ::: CSV-E005 :::')
# Result: Failed
# KeyError: 'studentPriority'
# Not sure why it wouldn't give out the error message: maybe it doesn't have oen?

# CSV-E006: missing studentAvoid field name
print('\n ::: CSV-E006 :::')
# Result: Passed
# ERROR: Required studentAvoid column header not found in the students csv file. Terminating Program.

# CSV-E024: studentID is not an integer value
print('\n ::: CSV-E024 :::')
# Result: Passed
# ERROR: Unexpected data type found in studentID.
# one of the studentID is '33340s702'

# CSV-E025: studentID is out of range of accepted values
print('\n ::: CSV-E025 :::')
# Result: Failed
# one of studentID is '-3', didn't seem to see that as a problem then accessed score.py for Assignment

# CSV-E026: studentID is not unique
print('\n ::: CSV-E026 :::')
# Result: Passed
# ERROR: Duplicate studentID found
# would be great to see which ones are the duplicates 

# CSV-E027: studentID value is missing
print('\n ::: CSV-E027 :::')
# Result: Passed
# ERROR: Empty element found in row 3 of the studentID column

# CSV-E028: studentGPA is not a float value
print('\n ::: CSV-E028 :::')
# Result: Passed
# ERROR: Unexpected data type found in studentGPA.
# one of studentGPA value is 'gpa', hence the error

# CSV-E029: studentGPA is out of range of accepted values
print('\n ::: CSV-E029 :::')
# Result: Passed
# ERROR: 4.43 outside of acceptable GPA range

# CSV-E030: studentGPA value is missing
print('\n ::: CSV-E030 :::')
# Result: Passed
# ERROR: Empty element found in row 1 of the studentGPA column

# CSV-E031: studentAvoid refers to an invalid studentID
print('\n ::: CSV-E031 :::')
# Result: Passed
# ERROR: No matching student id found for student = 7 in studentAvoid column

# CSV-E032: studentAvoid refers to themselves
print('\n ::: CSV-E032 :::')
# Result: Failed
# no error message displayed when a student has its own ID as studentAvoid

# CSV-E033: studentChoiceN refers to an invalid projectID
print('\n ::: CSV-E033 :::')
# Result: Passed
# ERROR: No matching project id found for studentChoice = 10
# example studentChoice (10) doesn't exist in project.csv hence the error 

# CSV-E034: studentChoice1 is missing
print('\n ::: CSV-E034 :::')
# Result: Failed
# no error message displayed when one student has a missing studentChoice1 value

# CSV-E035: studentESL is not boolean
print('\n ::: CSV-E035 :::')
# Result: Passed
# ERROR: Unexpected data type found in studentESL.
# would be great to remind user that only TRUE/FALSE are accepted

# CSV-E036: studentPriority is not boolean
print('\n ::: CSV-E036 :::')
# Result: Passed
# ERROR: Unexpected data type found in studentPriority.
# would be great to remind user that only TRUE/FALSE are accepted

# CSV-E056: data partially filled in 'assignment' column in Assignment mode
print('\n ::: CSV-E056 :::')
# Result: Failed??
# no error message displayed 
# current testing environment crashes on assignment mode hence ?? marks

# CSV-E057: data partially filled in 'assignment' column in Scoring mode
print('\n ::: CSV-E057 :::')
# Result: Passed
# ERROR: Empty field found in row 0 Assignment column.
# this should display that there are more empty value in the column (only 3 filled in student.csv)

# CSV-E058: duplicated field names in student.csv
print('\n ::: CSV-E058 :::')
# Result: Passed
# ERROR: Found a duplicate required column in the students.csv: Index(['studentAvoid.1'], dtype='object'). Terminating Program.
# two studentAvoid columns field names exist

# CSV-S001: excessive studentChoiceN entries
print('\n ::: CSV-S001 :::')
# Result: Passed
# program executed without an issue with excessive studentChoiceN entires (12 in test case)

# CSV-S002: excessive studentAvoidN entries (Ignore this)
# test case ignored since studentAvoidN is discarded

# CSV-S003: excessive blank lines in student.csv
print('\n ::: CSV-S003 :::')
# Result: Passed?
# no error/warning message displayed 
# current testing environment crashes on assignment mode hence ?? marks

# CSV-S004: excessive studentID rows
print('\n ::: CSV-S004 :::')
# Result: Passed?
# no error/warning message displayed 
# current testing environment crashes on assignment mode hence ?? marks

##############################################################################################

# Project CSV Handler test case:

# CSV-F005: columns rearranged
print('\n ::: CSV-F005 :::')
# Result: Passed
# no error/warning message displayed

# CSV-E007: missing project ID column
print('\n ::: CSV-E007 :::')
# Result: Passed?
# ERROR: nan in the projectID column is not an integer.
# IndexError: list index out of range
# no 'Terminating program' message displayed - should be added?

# CSV-E008: missing minTeamSize name and value
print('\n ::: CSV-E008 :::')
# Result: Passed
# ERROR: Required minTeamSize column header not found in the projects csv file. Terminating Program.


# CSV-E009: missing maxTeamSize name and value
print('\n ::: CSV-E009 :::')
# Result: Passed
# ERROR: Required maxTeamSize column header not found in the projects csv file. Terminating Program.

# CSV-E037: projectID is not an integer
print('\n ::: CSV-E037 :::')
# Result: Passed
# ERROR: one in the projectID column is not an integer.
# ERROR: one in the projectID column is not an integer.
# ERROR: two in the projectID column is not an integer.
# ERROR: two in the projectID column is not an integer.
# ERROR: 3.5 in the projectID column is not an integer.
# ERROR: 4.21 in the projectID column is not an integer.
# ERROR: 10.05 in the projectID column is not an integer.
# program crashes in load_csv due to errors - missing 'terminating the program' message
# also 'one' and 'two' are repated twice - not sure why messages are repeated

# CSV-E038: projectID is out of range
print('\n ::: CSV-E038 :::')
# Result:

# CSV-E039: projectID is not unique
print('\n ::: CSV-E039 :::')
# Result: Passed
# ERROR: Value -10 in the projectID column must be an integer greater than zero and less than 2^64.    
# ERROR: Value -1 in the projectID column must be an integer greater than zero and less than 2^64.     
# ERROR: Value 0 in the projectID column must be an integer greater than zero and less than 2^64.
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E040: projectID numbers are not sequential from 1
print('\n ::: CSV-E040 :::')
# Result: Passed?
# Warning: gap found in projectID sequence in the projects csv file. (not neccesarily mentioning from 1)
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E041: minTeamSize is not an integer
print('\n ::: CSV-E041 :::')
# Result: Passed
# ERROR: 2.1 in the minTeamSize column is not an integer.
# ERROR: 2.5 in the minTeamSize column is not an integer.
# ERROR: 3.3 in the minTeamSize column is not an integer.
# ERROR: 3.9 in the minTeamSize column is not an integer.
# ERROR: 2.15 in the minTeamSize column is not an integer.
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E042: maxTeamSize is not an integer
print('\n ::: CSV-E042 :::')
# Result: Passed
# ERROR: 5.5 in the maxTeamSize column is not an integer.
# ERROR: 7.7 in the maxTeamSize column is not an integer.
# ERROR: 8.8 in the maxTeamSize column is not an integer.
# ERROR: 9.9 in the maxTeamSize column is not an integer.
# ERROR: 10.12 in the maxTeamSize column is not an integer.
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E043: minTeamSize is larger than maxTeamSize
print('\n ::: CSV-E043 :::')
# Result: Passed
# ERROR: minTeamSize is greater than maxTeamSize for projectID 1.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 2.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 11.
# ERROR: minTeamSize is greater than maxTeamSize for projectID 100.
# ERROR: Invalid data found in input CSV files. Terminating program.

# CSV-E059: duplicated field names in project.csv
print('\n ::: CSV-E059 :::')
# Result: Failed
# failed to catch the duplicate projectName and crashes in score.py (current build issue with Assignment mode)

# CSV-S005: excessive projectID rows
print('\n ::: CSV-S005 :::')
# Result: Passed?
# Warning: gap found in projectID sequence in the projects csv file.
# does not report any issue with excessive projectIDs
# program terminated because no matching project ID were found for students

# CSV-S006: excessive blank lines in project.csv
print('\n ::: CSV-S006 :::')
# Result: Passed
# ERROR: nan in the projectID column is not an integer.
# the above error is repeated for every blank rows

##############################################################################################

# Settings CSV Handler test case:

# CSV-F006: columns rearranged
print('\n ::: CSV-F006 :::')
# Result: Pased
# ERROR: Required teamSize row not found in the settings csv file. Terminating Program.
# program terminated due to field names rearrangement hence not seeing required rows

# CSV-E010: missing field name 'name'
print('\n ::: CSV-E010 :::')
# Result: Passed
# ERROR: Required name column header not found in the settings csv file. Terminating Program.
# name is 'nam' in this test case settings.csv file, hence the error

# CSV-E011: missing field name 'min'
print('\n ::: CSV-E011 :::')
# Result: Passed
# ERROR: Required min column header not found in the settings csv file. Terminating Program.
# min is 'minz' in this test case, hence the error

# CSV-E012: missing field name 'max'
print('\n ::: CSV-E012 :::')
# Result: Passed
# ERROR: Required max column header not found in the settings csv file. Terminating Program.
# max is 'max_amooy' in this test case, hence the error

# CSV-E013: missing field name 'points'
print('\n ::: CSV-E013 :::')
# Result: Passed
# ERROR: Required points column header not found in the settings csv file. Terminating Program. 
# points is SCORE in this test case, hence the error

# CSV-E014: missing name field for lowGPAThreshold
print('\n ::: CSV-E014 :::')
# Result: Passed
# ERROR: Required lowGPAThreshold row not found in the settings csv file. Terminating Program.

# CSV-E015: missing name field for MaxLowGPAStudents
print('\n ::: CSV-E015 :::')
# Result: Passed
# ERROR: Required maxLowGPAStudents row not found in the settings csv file. Terminating Program. 

# CSV-E016: missing name field for MaxESLStudents
print('\n ::: CSV-E016 :::')
# Result: Passed
# ERROR: Required maxESLStudents row not found in the settings csv file. Terminating Program.

# CSV-E017: missing name field for weightMaxLowGPAStudents
print('\n ::: CSV-E017 :::')
# Result: Passed
# ERROR: Required weightMaxLowGPAStudents row not found in the settings csv file. Terminating Program. 

# CSV-E018: missing name field for weightMaxESLStudents
print('\n ::: CSV-E018 :::')
# Result: Passed
# ERROR: Required weightMaxESLStudents row not found in the settings csv file. Terminating Program. 

# CSV-E019: missing name field for weightTeamSize
print('\n ::: CSV-E019 :::')
# Result: Passed
# ERROR: Required weightTeamSize row not found in the settings csv file. Terminating Program.

# CSV-E020: missing name field for weightStudentPriority
print('\n ::: CSV-E020 :::')
# Result: Passed
# ERROR: Required weightStudentPriority row not found in the settings csv file. Terminating Program.

# CSV-E021: missing name field for weightStudentChoice1
print('\n ::: CSV-E021 :::')
# Result: Passed
# ERROR: Required weightStudentChoice1 row not found in the settings csv file. Terminating Program.

# CSV-E022: missing name field for weightAvoid
print('\n ::: CSV-E022 :::')
# Result: Passed
# ERROR: Required weightAvoid row not found in the settings csv file. Terminating Program.

# CSV-E023: missing name field for Efforts
print('\n ::: CSV-E023 :::')
# Result: Passed?
# Warning: valid 'effort' value not found in the settings csv. Running with default value of 20. 
# program does not halt itself - though test plan implies that it would
# effort could be an exception to program terminating itself if missing

# CSV-E044: lowGPAThreshold is not a float
print('\n ::: CSV-E044 :::')
# Result: Passed
# ERROR: The lowGPAThreshold 'min' value is not a float.
# NameError: name 'lowGPAThreshold' is not defined
# program terminates when min GPA is not a fload ('tolerance' in test case)

# CSV-E045: lowGPAThreshold is out of range
print('\n ::: CSV-E045 :::')
# Result: Passed
# ERROR: lowGPAThreshold 'min' setting requires a 0.00 - 4.00 value.
# ERROR: Invalid data found in input CSV files. Terminating program.
# lowGPAThreshold is 5.0 in the test case, hence the error

# CSV-E046: MaxLowGPAThreshold is not an integer
print('\n ::: CSV-E046 :::')
# Result: Passed?
# ERROR: 2.33 in the maxLowGPAStudents row is not an integer.
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)

# CSV-E047: MaxLowGPAStudents is out of range
print('\n ::: CSV-E047 :::')
# Result: Passed?
# ERROR: Value 0.0 in the maxLowGPAStudents column must be an integer greater than zero and less than 2^64.
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)

# CSV-E048: MaxESLStudents is not an integer
print('\n ::: CSV-E048 :::')
# Result: Passed
# ERROR: '$E' in the maxESLStudents row is not an integer.
# UnboundLocalError: local variable 'tempInt' referenced before assignment

# CSV-E049: MaxESLStudents is out of range
print('\n ::: CSV-E049 :::')
# Result: Passed?
# ERROR: Value 2.0000000000000003e+75 in the maxESLStudents column must be an integer greater than zero and less than 2^64
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)

# CSV-E050: Effort is not an integer
print('\n ::: CSV-E050 :::')
# Result: Passed?
# Warning: valid 'effort' value not found in the settings csv. Running with default value of 20.
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)
# program may not need to terminate for effort since default is given

# CSV-E051: Effort is out of range
print('\n ::: CSV-E051 :::')
# Result: Passed
# Warning: 'effort' in the settings csv is not an int between 1 and 100. Running with default value of 20.

# CSV-E052: weightMaxLowGPAStudents is not an integer
print('\n ::: CSV-E052 :::')
# Result: Passed
# ERROR: zero in the weightMaxLowGPAStudents row is not an integer.
# UnboundLocalError: local variable 'tempInt' referenced before assignment

# CSV-E053: weightMaxLowGPAStudents is out of range
print('\n ::: CSV-E053 :::')
# Result: Passed?
# ERROR: Value -1.0 in the weightMaxLowGPAStudents column must be an integer greater than zero and less than 2^64.
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)

# CSV-E054: weightMaxESLStudents is not an integer
print('\n ::: CSV-E054 :::')
# Result: Passed
# ERROR: $!`[] in the weightMaxESLStudents row is not an integer.

# CSV-E055: weightMaxESLStudents is out of range
print('\n ::: CSV-E055 :::')
# Result: Passed?
# ERROR: Value -1337.0 in the weightMaxESLStudents column must be an integer greater than zero and less than 2^64.
# the program gives the correct error message, 
# but proceeded to score.py (which crashed due to current build issue)

# CSV-E060: duplicated field names in settings.csv
print('\n ::: CSV-E060 :::')
# Result: Passed
# ERROR: Found a duplicate required column in the Settings CSV file: Index(['min.1'], dtype='object'). Terminating Program.

# CSV-S007: excessive blank lines in settings.csv
print('\n ::: CSV-S007 :::')
# Result: Passed
# program seems to ignore exessive blank lines
