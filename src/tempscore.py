# points calculation for capstone-colander
# Kai Brooks
# github.com/kaibrooks/capstone-colander

# returns points_max, divided evenly down by num_projects, depending on which assignment_choice a student gets
# eg, 5 projects, 100 points max => 20 points loss per 'step'
# gets first pick = 100 points, second pick = 80 points, third pick = 60 points, etc

import math # ceil()

def points( assignment_choice, num_projects, points_max ):
   
    if assignment_choice > num_projects:
        exit('Error: assignment choice doesn\'t exist')
        # in reality this zeroes the entire solutions score and moves on to the next one
        # but that code isn't implemented yet
        print('You shouldn\'t see this if the program exited correctly')
    elif assignment_choice == 0: # if a studen't didn't get any of their choices
        total = 0
    else: 
        total = math.ceil( points_max - (points_max / num_projects)*(assignment_choice - 1) )
    return total