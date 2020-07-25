# load students csv file
studentsFileData = pd.read_csv(studentsFile)

# verify all column headers are present in projects csv file
## NEEDS to be updated to send warnings for missing studentPriority and studentAvoid
studentsColumns = ['studentID', 'studentChoice1', 'studentGPA']
for col in studentsColumns:
    if col not in studentsFileData.columns:
        sys.exit("ERROR: Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

# debug print to verify data has been loaded
print(studentsFileData)

#Create a series to indicate datatypes of each column
studentDTypes = studentsFileData.dtype

#debug print to verify datatype series is correct
print(studentDTypes)

#Validate integers are present in studentID
if studentDTypes['studentID'] != 'int64'
    sys.exit("ERROR: Unexpected data type found in studentID. Terminating Program.")


# if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
## REVIEW (maybe use for esl/priority flags?)
#projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(42)  # 42 needs to be changed to settings.csv value
#minTeamSize = int_checker('minTeamSize')
#projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(42)
#maxTeamSize = int_checker('maxTeamSize')



# call another script
if not programMode == 'verbose':
    print('Calling the next function...')
    #os.system('python src/test/test_main.py') # put what file we actually want run here
#os.system('python src/run_ga.py') # put what file we actually want run here