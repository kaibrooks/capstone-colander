# # load CSV dummy file

import pandas as pd

# #def projectsHandler():

# global minTeamSize
# global maxTeamSize
# global projectIDs

# #def settingsHandler():
# global weightMaxLowGPAStudents
# global weightMaxESLStudents
# global weightTeamSize
# global weightStudentPriority
# global weightStudentChoice1
# global weightAvoid
# global maxLowGPAStudents
# global maxESLStudents
# global lowGPAThreshold
# global maxRunTime

# # things the ga needs
# global df
# global df_choices
# global num_projects
# global num_students
# global num_choices
# global max_run_time
# global infile # temp

# ## test case: all-purpose : /io/students_n50_c5_p15.csv
#infile = '/io/students_n50_c5_p15.csv'
#projectIDs  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# minTeamSize = [4, 4, 4, 3, 4, 3, 3, 3, 4, 3, 4, 2, 4, 4, 3]
# maxTeamSize = [5, 4, 7, 4, 4, 5, 6, 4, 5, 5, 4, 5, 6, 6, 5]

# ## test case: samechoice : /io/students_n10_c5_p5_samechoice.csv
infile = '/io/students_n10_c5_p5_samechoice.csv'
projectIDs = [1, 2, 3, 4, 5]
# minTeamSize = [4, 4, 2, 3, 3]
# maxTeamSize = [4, 4, 2, 3, 3]


# maxESLStudents          = 0 # 2
# lowGPAThreshold         = 0 # 2.75
# maxLowGPAStudents       = 0 # 2
# weightMaxLowGPAStudents = 0 # 100
# weightMaxESLStudents    = 0 # 75
# weightStudentPriority   = 0 # 100
# weightAvoid             = 0 # 60
# maxRunTime              = 120 # 120 minutes
# weightTeamSize          = 100 # 100
# weightStudentChoice1    = 100 # 100

df = pd.read_csv(infile) # load a file as a variable
# fields = [col for col in df.columns if 'studentChoice' in col] # get columns named 'studentChoice'
# df_choices = pd.read_csv(infile, skipinitialspace=True, usecols=fields) # df with just choices

global numStudents
numStudents = df['studentID'].count() # number of students (count each ID)
# num_projects = len(projectIDs) # total projects available
# num_choices = len(df_choices.columns)