# load_csv.py reads and parses all three csv files,
# then verifies all data in the csv files is valid.

import sys
import pandas as pd


# def projectsHandler(projectsFile):

#     # load projects csv file
#     projectsFileData = pd.read_csv(projectsFile)

#     # verify required project csv headers are preset
#     projectsColumns = ['projectID', 'minTeamSize', 'maxTeamSize']
#     for col in projectsColumns:
#         if col not in projectsFileData.columns:
#             sys.exit("ERROR: Required {0} column header not found in the projects csv file. Terminating Program.".format(col))

#     # debug print to verify data has been loaded
#     print("\n*** Debug print to verify csv contents ***")
#     print(projectsFileData)

#     # function to verify that values listed in csv files are integers
#     def int_checker(columnName):
#         intArray = []
#         for value in projectsFileData[columnName]:
#             try:
#                 intArray.append(int(value))
#             except ValueError:
#                 sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
#         return intArray

#     # verify that all values in program csv file are integers
#     projectIDs = int_checker('projectID')

#     # verify that there are no duplicate project IDs in the projectID column
#     if projectsFileData.projectID.duplicated().any():
#         sys.exit("ERROR: projectid {0} is a duplicate projectID in the csv file. Terminating Program.".format({projectsFileData[projectsFileData.projectID.duplicated()].projectID.iloc[0]}))

#     # if values for team sizes are blank, enter size from settings.csv and then verify all values are integers
#     projectsFileData['minTeamSize'] = projectsFileData['minTeamSize'].fillna(42)  # 42 needs to be changed to settings.csv value once that code is written
#     minTeamSize = int_checker('minTeamSize')
#     projectsFileData['maxTeamSize'] = projectsFileData['maxTeamSize'].fillna(42)
#     maxTeamSize = int_checker('maxTeamSize')  # TeamSizes not currently returned but may need to be for the scoring function



def studentsHandler(studentsFile):

    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentChoiceN
    global studentAvoidN
    global assignment

    #flags to indicate that optional headers have been included default False
    #colPriority = False
    #colAvoid = False

    #load students csv file
    studentsFileData = pd.read_csv(studentsFile)

    # debug print to verify data has been loaded
    #print(studentsFileData)


    #Move studentChoices into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentChoice' in col] # get columns named 'studentChoice'
    studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just choices

    #Move studentAvoid into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentAvoid' in col] # get columns named 'studentAvoid'
    studentAvoidN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just avoidances

    print("student avoidances")
    print(studentAvoidN)

    

    ######Store Data#######
    # Store single column data
    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].copy()
    studentPriority = studentsFileData['studentPriority'].copy()
    assignment = studentsFileData['Assignment'].copy()



    #debug print to verify studentID has been stored
    #print("Student ID Series Test")
    #print(studentID)

    #debug print to verify studentGPA has been stored
    #print("GPA Series Test")
    #print(studentGPA)

    #debug print to verify studentESL has been stored
    #print("Student ESL Series Test")
    #print(studentESL)

    #debug print to verify studentPriority has been stored
    #print("Student Priority Series Test")
    #print(studentPriority)

    #debug print to verify Assign has been stored
    #print("Assignment Series Test")
    #print(assign)
    