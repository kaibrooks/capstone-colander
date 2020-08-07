import sys
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype
import load_csv


def studentsHandler(studentsFile):

    global studentID
    global studentGPA
    global studentESL
    global studentPriority
    global studentChoiceN
    global studentAvoidN

    #flags to indicate that optional headers have been included default False
    #colPriority = False
    #colAvoid = False

    #load students csv file
    studentsFileData = pd.read_csv(studentsFile)

    # debug print to verify data has been loaded
    print(studentsFileData)


    ######Store Data#######

    #Move studentChoices into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentChoice' in col] # get columns named 'studentChoice'
    studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just choices

    #Move studentAvoid into a separate global dataframe
    fields = [col for col in studentsFileData.columns if 'studentAvoid' in col] # get columns named 'studentAvoid'
    studentAvoidN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just avoidances

    #print("student avoidances")
    #print(studentChoiceN)


    studentID = studentsFileData['studentID'].copy()
    studentGPA = studentsFileData['studentGPA'].copy()
    studentESL = studentsFileData['studentESL'].fillna(False)
    studentPriority = studentsFileData['studentPriority'].fillna(False)

    #debug print to verify studentID has been stored
    #print("Student Priority Test")
    #print(studentPriority)
  
    


    ########################Validate Data######################
    
    # verify all column headers are present in students csv file
    studentsColumns = ['studentID', 'studentChoice1', 'studentGPA','studentESL']
    for col in studentsColumns:
       if col not in studentsFileData.columns:
           sys.exit("ERROR: Required {0} column header not found in the students csv file. Terminating Program.".format(col))

    # look for optional column headers in students csv file
    #if 'studentPriority' not in studentsFileData.columns:
    #    print("Warning: studentPriority column header not found in the students csv file.")
    #else:
        #set colPriority flag to true
    #    colPriority = True
        #debug print
    #    print("Priority Flag column found")

    #if 'studentAvoid1' not in studentsFileData.columns:
    #    print("Warning: studentAvoid1 column header not found in the students csv file. No avoids will be considered for the solution.")
    #else:
        #set colAvoid flag to true
    #    colAvoid = True
        #debug print
    #    print("Avoid1 Flag column found")

    # #Move studentChoices into a separate global dataframe
    # fields = [col for col in studentsFileData.columns if 'studentChoice' in col] # get columns named 'studentChoice'
    # studentChoiceN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just choices

    # #Move studentAvoid into a separate global dataframe
    # fields = [col for col in studentsFileData.columns if 'studentAvoid' in col] # get columns named 'studentAvoid'
    # studentAvoidN = pd.read_csv(studentsFile, skipinitialspace=True, usecols=fields) # df with just avoidances

    #Validate only integers are present in studentID
    if is_numeric_dtype(studentID) == False:
         print('Error studentID type incorrect ')
         sys.exit("ERROR: Unexpected data type found in studentID. Terminating Program.")        
    else:
        print('studentID type correct')
    
    #Validate only integers are present in studentGPA
    if is_numeric_dtype(studentGPA) == False:
         print('Error studentGPA type incorrect ')
         sys.exit("ERROR: Unexpected data type found in studentGPA. Terminating Program.")        
    else:
        print('studentGPA type correct')

    

    
    #Validate only integers are present in studentPriority
    if is_bool_dtype(studentPriority) == False:
         print('Error studentPriority type incorrect ')
         sys.exit("ERROR: Unexpected data type found in studentPriority. Terminating Program.")        
    else:
        print('studentPriority type correct')
     
    #Validate only integers are present in studenChoiceN dataframe
    # creating a list of dataframe columns 
    clmn = list(studentChoiceN) 
    for i in clmn: 
        if is_numeric_dtype(studentChoiceN[i]) == False:
            print('Error studentChoice type incorrect ')
            sys.exit("ERROR: Unexpected data type found in studentChoice. Terminating Program.")        
        else:
            print('studentChoice type correct')

    #Validate only integers are present in studenAvoidN dataframe
    # creating a list of dataframe columns 
    clmn = list(studentAvoidN) 
    for i in clmn: 
        if is_numeric_dtype(studentAvoidN[i]) == False:
            print('Error studentAvoid type incorrect ')
            sys.exit("ERROR: Unexpected data type found in studentAvoid. Terminating Program.")        
        else:
            print('studentAvoid type correct')


    #Check if studentID has any duplicate values
    if studentID.duplicated().any():
        print('ERROR: studentID duplicate')
    
    #Check all values of studentGPA are within the 0.0-4.0 range
    for value in studentGPA:
        if (value < 0.0) or (value > 4.0):
            print('ERROR: GPA outside of acceptable range')

    #Iterate through studentAvoid?????????
    clmns = list(studentAvoidN) 
    sAvoidMatch = False

  
    for cind in clmns:                   #shuffle through the columns
        for rind in studentAvoidN.index: #shuffle through the rows
            if pd.isna(studentAvoidN[cind][rind]) == False:     #Ignore empty elements
                for i in studentID.index:          #shuffle through the studentIDs
                    if (studentAvoidN[cind][rind] == studentID[i]): # if a match is found flip flag
                        print ('Match Found')
                        print(studentAvoidN[cind][rind])
                        sAvoidMatch = True
                if sAvoidMatch == False:
                    print('ERROR: No match found for value' ) 
                    print(studentAvoidN[cind][rind])  

    print(load_csv.projectID)




