# convert id
# github.com/kaibrooks/capstone-colander
#
# converts projectIDs into sequential numbers

import load_csv as lc

def fix(soln):
    new_id = [0]* len(soln)
    for i in range(len(soln)):
        new_id[i] = lc.projectIDs[int(soln[i])-1]
    return new_id