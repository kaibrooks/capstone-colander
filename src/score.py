# points calculation for capstone-colander
# kai brooks
# github.com/kaibrooks/capstone-colander

import math # use ceil()
#import load_csv as lc
import numpy as np 

# points_max = lc.weightStudentChoice1
# num_students = lc.num_students
# num_projects = lc.num_projects
# num_choices = lc.num_choices

# # scores for individual assignment
# def points_ch(soln):
#     total = 0
#     for i in range(num_students): #C iterate through the solution to get assignment scores
#         for j in range(num_choices): #not the same as num_projects
#             if lc.df_choices.iat[i,j] == soln[i]: # (down, right) -- (0,3) is student 1 choice 4
#                 total += math.ceil( points_max - (points_max / num_projects)*(j+1 - 1) ) # points function when that's done, need + 1 because its indexed at 0 (choice 1 is j=0)
#                 break
#             if j == num_choices: # didn't get any of their picks :(
#                 total = 0
#     return total

# # group size
# def points_gs(soln):
#     total = 0
#     for i in range(num_projects): # iterate over the solution
#         if np.count_nonzero(soln == (i+1)) == 0:
#             total += lc.weightTeamSize*0.2 # give small points to prevent spreading students around
#         #print('Checking: i=',i,' - min=',lc.minTeamSize[i],'- max=',lc.maxTeamSize[i], ' - ACT=',np.count_nonzero(soln == i))
#         #print('Soln: ',soln)
#         #if np.count_nonzero(soln == i) == 0: # if a project doesn't run
#         #    total += lc.weightTeamSize # ??? maybe
#         if lc.minTeamSize[i] <= np.count_nonzero(soln == (i+1)) <= lc.maxTeamSize[i]: # group size restriction
#             #print('*** TP',i,':',lc.minTeamSize[i],'<',np.count_nonzero(soln == (i+1)),'<', lc.maxTeamSize[i])
#             total += lc.weightTeamSize # reward for meeting the constraint
#     return total

# def groupsizes(soln):
#     gs = np.empty(num_projects, dtype=object)
#     for i in range(num_projects):
#         gs[i] = np.count_nonzero(best_soln == (i+1))


# stubs
def pointsStudentChoice(inputArray):
    return sum(inputArray)

def pointsESLStudents(inputArray):
    return 0

def pointsStudentPriority(inputArray):
    return 0

def pointsMaxLowGPAStudents(inputArray):
    return 0

def pointsTeamSize(inputArray):
    return 0

def pointsAvoid(inputArray):
    return 0