# runs the assignment algorithm
# kai brooks
# github.com/kaibrooks/capstone-colander

# standard libraries
import numpy as np
from geneticalgorithm import geneticalgorithm
import time # time the algorithm
import pandas as pd # loads csv

# imports from the application
from score import points_ch, points_gs
import load_csv as lc
from prints import printError as err
from prints import printWarning as warn
from prints import printGeneral as msg

# defs
def objf(soln): # objective function
    """objective function for genetic algorithm
    arguments:
    soln -- the solution to evaluate
    returns:
    y -- function value
    """
    max_run_time = lc.max_run_time
    
    y = points_gs(soln) # group size
    soln = fix(soln) # indexing
    y += points_ch(soln) # choices
    
    # timing
    # if time.time()-t0 > max_run_time:
    #     print('stop me') # TODO break here

    return -y # return negative for positive scoring

def fix(soln):
    """convert sequential ga output array into project id array
    arguments:
    soln (req) -- ga output solution to convert
    returns:
    new_id -- array of project IDs
    """
    # eg, input: [1, 2, 3] // output: [1, 3, 6] -- assume no project number 2, 4, 5
    new_id = [0]* len(soln)
    for i in range(len(soln)):
        new_id[i] = lc.projectIDs[int(soln[i])-1]
    return new_id

def run_ga():
    """run the genetic algorithm
    returns:
    best_soln -- the best solution
    """
    # passed vars
    num_students = lc.num_students
    num_projects = lc.num_projects
    
    # hyperparameters
    global num_generations
    num_generations = 2000

    var_bound = np.array([[1,num_projects]]*num_students) # solution shape
    ga_params = {'max_num_iteration': num_generations,\
                    'population_size':100,\
                    'mutation_probability':0.02,\
                    'elit_ratio': 0.01,\
                    'crossover_probability': 0.5,\
                    'parents_portion': 0.3,\
                    'crossover_type':'uniform',\
                    'max_iteration_without_improv':num_generations*0.3
                    } 

    # model information
    model=geneticalgorithm(function=objf,\
                dimension=num_students,\
                variable_type='int',\
                variable_boundaries=var_bound,\
                algorithm_parameters=ga_params
                )
                
    # output things
    print('Running for',num_students,'students and',num_projects,'projects:',lc.infile)

    # hit it
    t0 = time.time() # go
    #best_soln # globalize for debug
    best_soln = model.run() # call the model defined in geneticalgorithm.py
    t1 = time.time()
    global total_time
    total_time = t1-t0 # and stop
    print('\nTime:', total_time)
    return best_soln

def ga_debug(best_soln):
    """genetic algorithm debugging output
    arguments:
    best_soln (req) -- the best solution the ga outputs
    """
    num_projects = lc.num_projects
    
    print(':: Debugging output ::')
    print('Solution:\n',best_soln)

    # group sizes
    global gs 
    gs = np.empty(num_projects, dtype=object)
    for i in range(num_projects):
        gs[i] = np.count_nonzero(best_soln == (i+1))

    trunc_limit = 22 # truncate the output to fit in the console
    if len(lc.df_choices['studentChoice1'].values.tolist()) > trunc_limit:
        print('\nChoices (truncated):')
    else:
        print('\nDesired choices:')
    print('1:',lc.df_choices['studentChoice1'].values.tolist()[:trunc_limit])
    print('2:',lc.df_choices['studentChoice2'].values.tolist()[:trunc_limit])
    print('3:',lc.df_choices['studentChoice3'].values.tolist()[:trunc_limit])

    print('\nGroup sizes:')
    print('min:',lc.minTeamSize)
    print('ACT:', gs.tolist())
    print('max:',lc.maxTeamSize)

    print('\nTiming:')
    print('Run time:',total_time)
    print('Per generation:', total_time/num_generations)
    

## call things for test
best_soln = run_ga()
ga_debug(best_soln)