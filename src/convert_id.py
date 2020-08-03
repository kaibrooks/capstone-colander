# converts projectIDs into sequential numbers


 # input    = [4 2 3 3 1 4 2]
 # want out = [6 2 4 4 1 6 2]
#projectIDs  = [1, 2, 4, 6]

import load_csv as lc

'''  Genetic Algorithm Converter for Python
    
    Converts genetic algorithm output to actual project numbers
    
    Implementation and output:
        
        methods:
                fix(): convert genetic algoritm output to project numbers from projectIDs
                
        outputs:
                new_id: the solution with the fixed ID's
    '''

def fix(soln):
    new_id = [0]* len(soln)
    for i in range(len(soln)):
        new_id[i] = lc.projectIDs[int(soln[i])-1]
    return new_id

#nyan = fix()

#print(nyan)