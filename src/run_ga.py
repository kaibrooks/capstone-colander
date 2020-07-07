# genetic algorithm
# github.com/kaibrooks/capstone-colander
#
# runs the ga

import numpy as np
from geneticalgorithm import geneticalgorithm as ga # ga alg
import time # time the algorithm

# defs
def f(soln): # this is the objective function the algorithm tries to *minimize*, like an inverse 'fitness'
    # the ga's solution is an array, soln[]
    # don't print anything here or the console is going to be a mess
    objf = 0
    
    ### some example returns ###
    ## return for matching
    for i in range(len(y)):
        if soln[i] != y[i]: # want to match bits
            objf = objf + 1 # bad points
    return objf
    
    ## return the sum, but maximized
    #return -sum(soln)

    ## return a specific arrangement of the first 5 bits, minimize the rest
    # if soln[0] == y[0] and soln[1] == y[1] and soln[2] == y[2] and soln[3] == y[3] and soln[4] == y[4]: 
    #   return sum(soln)
    # else:
    #    return poison # extra bad score




print("*** RUNNING GA.PY ***\n")

## user settings
# settings that should come from reading the CSV (here for test)
num_students = 80 # number of students
num_projects = 20 # total projects available (NOT how many each student can select)
n = num_students # chromosome length 

# hyperparameters
num_iterations = 1000
poison = 9999 # spindle poison, value should disqualify that solution

# boundaries
var_bound=np.array([[1,num_projects]]*n) # boundaries the ga will stick to. should equal the project number spread

# array to match (for testing ga speed, not needed for 'live' use)
y = np.random.randint(1, num_projects, n) # make a random array

# hyperparameters
ga_params = {'max_num_iteration': num_iterations,\
                   'population_size':100,\
                   'mutation_probability':0.02,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':num_iterations*0.4
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
print('String to match:')
print('',y,'(',len(y),' items )')

# hit it
t0 = time.time() # go
model.run() # this is the model defined in geneticalgorithm.py
t1 = time.time()
total = t1-t0 # and stop
print("\nTime:", total)