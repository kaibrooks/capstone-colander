# runs the assignment algorithm
# kai brooks
# github.com/kaibrooks/capstone-colander

# standard libraries
import numpy as np
from geneticalgorithm import geneticalgorithm

# imports from the application
import load_csv
import prints
import score

# defs
def objf(soln): # objective function
    """objective function for genetic algorithm
    arguments:
    soln -- the solution to evaluate
    returns:
    y -- function value
    """

    soln = fix(soln) # indexing
    y = score.pointsTeamSize(soln)
    y += score.pointsStudentPriority(soln)
    y += score.pointsAvoid(soln)
    y += score.pointsESLStudents(soln)
    y += score.pointsMaxLowGPAStudents(soln)
    y += score.pointsStudentChoice(soln)

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

def run_ga(verbose=1):
    """run the genetic algorithm
    arguments:
    verbose (optional, default True) -- (1/0) outputs running text and progress bar
    returns:
    best_soln -- numpty array of the best solution
    """

    # vars
    num_projects = len(load_csv.projectIDs) # total projects available
    num_generations = load_csv.numStudents*num_projects*load_csv.effort # scale generations based on input size

    var_bound = np.array([[1,num_projects]]*load_csv.numStudents) # solution shape
    ga_params = {'max_num_iteration': num_generations,\
                    'population_size':100,\
                    'mutation_probability':0.02,\
                    'elit_ratio': 0.01,\
                    'crossover_probability': 0.5,\
                    'parents_portion': 0.3,\
                    'crossover_type':'uniform',\
                    'max_iteration_without_improv':num_generations*0.35,\
                    'verbose':verbose,\
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
                dimension=load_csv.numStudents,\
                variable_type='int',\
                variable_boundaries=var_bound,\
                algorithm_parameters=ga_params
                )
    # function=objf -- function to minimize
    # dimension=load_csv.numStudents -- chromosome length
    # variable_type=int -- data type
    # variable_boundaries=var_bound -- data range per gene
    # algorithm_parameters=ga_params -- ga settings from above
    if verbose:
        prints.gen(f'Running {num_generations} generations with input: {load_csv.infile}')

    # hit it
    return model.run() # run the model defined in geneticalgorithm.py