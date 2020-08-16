# score.py unit test
# Kai Brooks
# github.com/kaibrooks/capstone-colander

import os,sys,inspect # this block finds points.py in the parent directory, not /test
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from score import points # get the points() function from score.py

## call the points() function like this:
# points(assignment_choice, num_projects, points_max)
#
# assignment_choice: which choice the student got assigned (1st choice, 2nd choice, etc)
# num_projects: total number of projects
# points_max: how many points a 'first pick' is worth
# ex: points(2, 5, 100) -- student got their second pick. there are 5 projects and a max score of 100

print('test_score.py output:')

# test example: looping through choices 1-5
num_projects = 5
points_max = 100
for i in range(1,6):
    assignment_choice = i
    award = points(assignment_choice, num_projects, points_max) # call the points function
    print('(Loop) Points for choice',assignment_choice,':', award) # print the result

# test example: erroneously using a negative number
assignment_choice = -1
num_projects = 5
points_max = 100
award = points(assignment_choice, num_projects, points_max) # call the points function
print('(Negative number) Points for choice',assignment_choice,':', award) # print the result