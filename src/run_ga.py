# genetic algorithm
# github.com/kaibrooks/capstone-colander
#
# runs the ga

import numpy as np
from geneticalgorithm import geneticalgorithm as ga # ga alg
import time # time the algorithm
import pandas as pd # loads csv
from tempscore import points

# defs
def f(soln): # this is the objective function the algorithm tries to *minimize*, like an inverse 'fitness'
    # the ga's solution is an array, soln[]
    # don't print anything here or the console is going to be a mess
    objf = 0

    # scores for individual assignment
    for i in range(n): # iterate through the solution to get assignment scores
        for j in range(num_choices): #not the same as num_projects
            if df_choices.iat[i,j] == soln[i]: # (down, right) -- (0,2) is student 1 choice 3
                objf += points(j+1, num_projects, 100) # points function when that's done, need + 1 because its indexed at 0 (choice 1 is j=0)
                break
            if j == num_choices: # didn't get any of their picks :(
                objf += points(0, num_projects, 100)
    
    # scores for group-related constraints
    for i in range(1, num_projects+1): # iterate over the solution
        if 5 <= np.count_nonzero(soln == i) <= 6: # group size restriction
            objf *= 1.1 # reward for meeting the constraint
            # does this need to break? think about it

    return -objf # return negative since our scores are positive

# load CSV (temp)
infile = '/io/students_n100_c5_p30.csv'
df = pd.read_csv(infile) # load a file as a variable
fields = [col for col in df.columns if 'studentChoice' in col] # get columns named 'studentChoice'
df_choices = pd.read_csv(infile, skipinitialspace=True, usecols=fields) # df with just choices
print(df_choices)
# print(df_choices)
# print(df_choices.iat[0,0])
# print(df_choices.iat[4,0]) # down then right -- (0,0) is student 1 choice 1

print("*** RUNNING RUN_GA.PY ***\n")

## user settings
# settings that should come from reading the CSV (here for test)
num_students = df['studentID'].count() # number of students (count each ID)
num_projects = 30 # total projects available
num_choices = 5 # total choices
n = num_students # chromosome length 

# hyperparameters
num_iterations = 1000
poison = 1 # spindle poison, value should disqualify that solution

# boundaries
var_bound=np.array([[1,num_projects]]*n) # boundaries the ga will stick to. should equal the project number spread

# array to match (for testing ga speed, not needed for 'live' use)
#y = np.random.randint(1, num_projects, n) # make a random array

# hyperparameters
ga_params = {'max_num_iteration': num_iterations,\
                   'population_size':100,\
                   'mutation_probability':0.02,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':num_iterations*0.3
                   } 
                   # crossover_type: one_point; two_point, uniform

# model information
model=ga(function=f,\
            dimension=n,\
            variable_type='int',\
            variable_boundaries=var_bound,\
            algorithm_parameters=ga_params
            )
            # variable_type: real, int, bool
            # with bool, no boundaries needed

# output things
print('Running for',num_students,'students and',num_projects,'project choices')

# hit it
t0 = time.time() # go
best_soln = model.run() # call the model defined in geneticalgorithm.py
t1 = time.time()
total = t1-t0 # and stop
print('\nTime:', total)



print('Group sizes:')
for i in range(1, num_projects+1): # number of projects in total
    print('Project',i,':',np.count_nonzero(best_soln == i))