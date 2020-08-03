# points calculation for capstone-colander
# Kai Brooks
# github.com/kaibrooks/capstone-colander

# returns points_max, divided evenly down by num_projects, depending on which assignment_choice a student gets
# eg, 5 projects, 100 points max => 20 points loss per 'step'
# gets first pick = 100 points, second pick = 80 points, third pick = 60 points, etc

import math # ceil()
import load_csv
import numpy as np 


points_max = load_csv.weightStudentChoice1
num_students = load_csv.num_students
num_projects = load_csv.num_projects
num_choices = load_csv.num_choices

# scores for individual assignment
def points_ch(soln):
    total = 0
    for i in range(num_students): #C iterate through the solution to get assignment scores
        for j in range(num_choices): #not the same as num_projects
            if load_csv.df_choices.iat[i,j] == soln[i]: # (down, right) -- (0,2) is student 1 choice 3
                total += math.ceil( points_max - (points_max / num_projects)*(j+1 - 1) ) # points function when that's done, need + 1 because its indexed at 0 (choice 1 is j=0)
                break
            if j == num_choices: # didn't get any of their picks :(
                total = 0
    return total

# group size
def points_gs(soln):
    total = 0
    for i in range(1, num_projects): # iterate over the solution
        if np.count_nonzero(soln == i) == 0: # if a project doesn't run
            total += load_csv.weightTeamSize # ??? maybe
        if load_csv.minTeamSize[i] <= np.count_nonzero(soln == i) <= load_csv.maxTeamSize[i]: # group size restriction
            total += load_csv.weightTeamSize # reward for meeting the constraint
    return total