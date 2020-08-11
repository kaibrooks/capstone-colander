# runs the assignment algorithm
# kai brooks
# github.com/kaibrooks/capstone-colander

# how to call the genetic algorithm:
# k = run_ga()
# k is a numpy.ndarray (array of integers)

# standard libraries
import numpy as np
from geneticalgorithm import geneticalgorithm
import time # time the algorithm

# imports from the application
import load_csv
import prints
from score import pointsAvoid, pointsESLStudents, pointsMaxLowGPAStudents, pointsStudentChoice, pointsStudentPriority, pointsTeamSize

# defs
def objf(soln): # objective function
    """objective function for genetic algorithm
    arguments:
    soln -- the solution to evaluate
    returns:
    y -- function value
    """
 
    soln = fix(soln) # indexing
    y = pointsTeamSize(soln)
    y += pointsStudentPriority(soln)
    y += pointsAvoid(soln)
    y += pointsESLStudents(soln)
    y += pointsMaxLowGPAStudents(soln)
    y += pointsStudentChoice(soln)
    
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
        new_id[i] = load_csv.projectIDs[int(soln[i])-1]
    return new_id

def run_ga():
    """run the genetic algorithm
    returns:
    best_soln -- the best solution
    """
    # passed vars
    num_students = load_csv.numStudents
    num_projects = len(load_csv.projectIDs) # total projects available
    
    # settings
    np.set_printoptions(precision=2) # output 2 past the decimal
    
    # hyperparameters
    global num_generations
    global ga_effort
    ga_effort = 2.5
    num_generations = num_students*num_projects*ga_effort # scale generations based on input size

    var_bound = np.array([[1,num_projects]]*num_students) # solution shape
    ga_params = {'max_num_iteration': num_generations,\
                    'population_size':100,\
                    'mutation_probability':0.02,\
                    'elit_ratio': 0.01,\
                    'crossover_probability': 0.5,\
                    'parents_portion': 0.3,\
                    'crossover_type':'uniform',\
                    'max_iteration_without_improv':num_generations*0.15,\
                    }

    # max_num_iteration <int> -- stop after this many generations
    # population_size <int> -- chromosomes (members) per generation
    # mutation_probability <float in [0,1]> -- mutation rate
    # elit_ration <float in [0,1]> -- elite ratio
    # crossover_probability <float in [0,1]>  -- probability of crossover for each gene
    # parents_portion <float in [0,1]> -- ratio of parents in each generation
    # crossover_type <string> -- 'uniform', 'one_point', or 'two_point' 
    # max_iteration_without_improv <int> -- stop early after this many successive generations without improvement

    # model information
    model=geneticalgorithm(function=objf,\
                dimension=num_students,\
                variable_type='int',\
                variable_boundaries=var_bound,\
                algorithm_parameters=ga_params
                )
    # function=objf -- function to minimize
    # dimension=num_students -- length
    # variable_type=int -- data type
    # variable_boundaries=var_bound -- data range per element 
    # algorithm_parameters=ga_params -- ga settings from above
    verbose = 1
    if verbose:        
        prints.printGeneral(f'Running {num_generations} with input: {load_csv.infile}')

    # hit it
    global total_time
    t0 = time.time()
    best_soln = model.run() # call the model defined in geneticalgorithm.py
    total_time = time.time() - t0
    
    return best_soln

def ga_debug(best_soln):
    """genetic algorithm debugging output
    arguments:
    best_soln (req) -- the best solution the ga outputs
    """
    num_projects = load_csv.num_projects
    
    prints.printGeneral(f'\n:: Debugging output ::')
    prints.printGeneral(f'Solution:\n {best_soln}')

    # group sizes
    global gs 
    gs = np.empty(num_projects, dtype=object)
    for i in range(num_projects):
        gs[i] = np.count_nonzero(best_soln == (i+1))

    trunc_limit = 22 # truncate the output to fit in the console
    if len(load_csv.df_choices['studentChoice1'].values.tolist()) > trunc_limit:
        prints.printGeneral(f'\nChoices (truncated):')
    else:
        prints.printGeneral(f'\nDesired choices:')
    prints.printGeneral(f"1: {load_csv.df_choices['studentChoice1'].values.tolist()[:trunc_limit]}")
    prints.printGeneral(f"2: {load_csv.df_choices['studentChoice2'].values.tolist()[:trunc_limit]}")
    prints.printGeneral(f"3: {load_csv.df_choices['studentChoice3'].values.tolist()[:trunc_limit]}")

    prints.printGeneral(f'\nGroup sizes:')
    prints.printGeneral(f'min: {load_csv.minTeamSize}')
    prints.printGeneral(f'ACT: {gs.tolist()}')
    prints.printGeneral(f'max: {load_csv.maxTeamSize}')

    prints.printGeneral(f'\nTiming:')
    prints.printGeneral(f'Run time: {round(total_time, 3)}')
    prints.printGeneral(f'Per generation: {round(total_time/num_generations, 6)}')
    
## call things for test
best_soln = run_ga()