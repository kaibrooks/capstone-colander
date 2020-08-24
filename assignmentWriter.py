# load_csv
import pandas as pd # loads csv

def assignmentColumnCreator(studentsFile, groupAssignments):
    df = pd.read_csv(studentsFile) # load a file as a variable
    print(df) # output it
    #print("Total Students : ", df['studentID'].count())
    #print("Average GPA    : ", df['studentGPA'].mean())

    # copy the first file so we don't overwrite it
    # Setting index to False prevents storing of the row numbers in the csv
    df.to_csv(studentsFile, index = False)

    project_assignment = []
    for i in range(len(df)):
        project_assignment.append(groupAssignments[i]) # add that column to the dataframe

    df['Assignment'] = '' # if no 'Assignment' column, create it
    new_data = pd.DataFrame({'Assignment': project_assignment}) # project assignments
    df.update(new_data) # add them to the csv

    ## write a new csv
    df.to_csv('new_students.csv', index=False)
    print(df) # output it

groupAssignments = [1, 7, 7, 4]
cat = 'students.csv'
assignmentColumnCreator(cat, groupAssignments)