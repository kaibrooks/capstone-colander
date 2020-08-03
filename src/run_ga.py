# genetic algorithm
# github.com/kaibrooks/capstone-colander
#
# runs the ga

import numpy as np
from geneticalgorithm import geneticalgorithm as ga # ga alg
import time # time the algorithm
import pandas as pd # loads csv
from score import points_ch, points_gs
import load_csv as lc

# defs
def objf(soln): # objective function
    y = 0
    y = points_ch(soln) # choices
    y += points_gs(soln) # group size

    # timing
    # if time.time()-t0 > max_run_time:
    #     print('stop me') # TODO break here

    return -y # return negative for positive scoring

print("*** RUNNING RUN_GA.PY ***\n")

#global soln

# passed vars
num_students = lc.num_students
num_projects = lc.num_projects
num_choices = lc.num_choices
max_run_time = lc.max_run_time

# hyperparameters
num_iterations = 2000
var_bound=np.array([[1,num_projects]]*num_students) # solution shape
ga_params = {'max_num_iteration': num_iterations,\
                   'population_size':100,\
                   'mutation_probability':0.02,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':num_iterations*0.9
                   } 

# model information
model=ga(function=objf,\
            dimension=num_students,\
            variable_type='int',\
            variable_boundaries=var_bound,\
            algorithm_parameters=ga_params
            )
            
# output things
print('Running for',num_students,'students and',num_projects,'projects:',lc.infile)

# hit it
t0 = time.time() # go
best_soln = model.run() # call the model defined in geneticalgorithm.py
t1 = time.time()
total = t1-t0 # and stop
print('\nTime:', total)

## everything below this line is debugging output
trunc_limit = 22 # truncate the output to fit in the console
if len(lc.df_choices['studentChoice1'].values.tolist()) > trunc_limit:
    print('\nChoices (truncated):')
else:
    print('\nChoices:')
print('1:',lc.df_choices['studentChoice1'].values.tolist()[:trunc_limit])
print('2:',lc.df_choices['studentChoice2'].values.tolist()[:trunc_limit])
print('3:',lc.df_choices['studentChoice3'].values.tolist()[:trunc_limit])

# group sizes
gs = np.empty(num_projects, dtype=object)
for i in range(num_projects):
    gs[i] = np.count_nonzero(best_soln == (i+1))

print('\nGroups:')
print('min:',lc.minTeamSize)
print('ACT:', gs.tolist())
print('max:',lc.maxTeamSize)