# runs the assignment algorithm

# standard libraries
import numpy as np
from geneticalgorithm import geneticalgorithm

# imports from the application
import load_csv
import score

# defs
def objf(soln): # objective function
    """objective function for genetic algorithm
    arguments:
    soln -- the solution to evaluate
    returns:
    y -- function value
    """

    # Messy conversion from numpy array to list of ints
    soln.tolist()
    soln = list(map(int, soln))

    y = score.scoringMode(soln)

    return -y # return negative for positive scoring

def run_ga(verbose=1):
    """run the genetic algorithm
    arguments:
    verbose (optional, default True) -- (1/0) outputs running text and progress bar
    returns:
    best_soln -- numpty array of the best solution
    """

    # vars
    effort_scaling = load_csv.effort # scale the effort value for this algorithm, '100' taking roughly 8 hours
    num_projects = len(load_csv.projectIDs) # total projects available
    num_generations = load_csv.numStudents*num_projects*effort_scaling # scale generations based on input size
    var_bound = np.array([[0, num_projects - 1]] * load_csv.numStudents) # solution shape
    ga_params = {'max_num_iteration': 2000,\
                    'population_size':100,\
                    'mutation_probability':0.2,\
                    'elit_ratio': 0.01,\
                    'crossover_probability': 0.5,\
                    'parents_portion': 0.3,\
                    'crossover_type':'uniform',\
                    'max_iteration_without_improv':None,\
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
    #if verbose:
        #prints.gen(f'Running {num_generations} generations with input: {load_csv.infile}')

    # hit it
    return model.run() # run the model defined in geneticalgorithm.py