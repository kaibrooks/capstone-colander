# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv

load_csv.settingsHandler()
load_csv.projectsHandler()
load_csv.studentsHandler()

# Student 0, 1, 2, ..., 8, 9
fauxGA = [0, 0, 0, 0, 1, 1, 1, 1, 9, 9]

def pointsStudentChoice(inputGA):
    totalPSC = 0
    num_projects = 5
    points_max = load_csv.weightStudentChoice1

    #print(load_csv.minTeamSize[3], 'zzz')

    for i in load_csv.studentID:
        if load_csv.studentChoice[i] == fauxGA[i]:
            #print(fauxGA[i], 'faux')
            # Replace fauxGA[i] with student choice array of choices 1 - 5
            totalPSC = totalPSC + math.ceil(points_max - (points_max / num_projects) * (fauxGA[i] - 1))
            #print(totalPSC, "totalPSC IN LOOP")
            
        else:
            totalPSC = totalPSC
            #print(totalPSC, "totalPSC")
    #print('totalPSC =', totalPSC)

    return totalPSC

def pointsESLStudents(inputGA):
    totalPES = 0
    point_weight = load_csv.weightMaxESLStudents
    maxESL = load_csv.maxESLStudents

    # Initializing an empty array of 50 to 0's
    ESL_Group = [0] * 50

    #print(maxESL, max_points, 'max stuff')
    print(ESL_Group, 'ESL_Group Before')

    for i in load_csv.studentID:
        # Checking if a students ESL flag is set to 1
        if load_csv.studentESL[i] == 1:
            #print(ESL_Group[fauxGA[i]], 'faux')
            # The students actual assignment (fauxGA[i]) is used to index into ESL_Group to
            # track how many ESL students are on that team.
            ESL_Group[fauxGA[i]] = ESL_Group[fauxGA[i]] + 1

            #x += 1
            #if x > load_csv.maxTeamSize
            
            if ESL_Group[fauxGA[i]] > maxESL:
                totalPES -= point_weight
                print(totalPES, 'Current total')
    print(ESL_Group, 'ESL_Group After')

    return totalPES

def pointsStudentPriority(inputGA):
    totalPSP = 0

    for i in load_csv.studentID:
        if load_csv.studentPriority[i] == 1:
            if fauxGA[i] == load_csv.studentChoice:
                totalPSP += load_csv.weightStudentPriority
            else:
                totalPSP -= load_csv.weightStudentPriority

    return totalPSP

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(inputGA):
    totalPML = 0
    weight_pml = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold
    maxLow = load_csv.maxLowGPAStudents
    maxLow_group = [0] * 10

    print(minGPA, ': min GPA cutoff')
    print(maxLow, ': max students with min GPA in a group')

    def group(maxLow_group):
        for i in load_csv.studentID:
            if load_csv.studentGPA[i] < minGPA:
                maxLow_group[fauxGA[i]] = maxLow_group[fauxGA[i]] + 1
        return maxLow_group

    print(group(maxLow_group))

    for i in range(len(maxLow_group)):
        if maxLow_group[i] > 0 and maxLow_group[i] <= maxLow:
            totalPML += weight_pml
            print('total PML score =', totalPML)      
        else:
            print('No bonus!')

    return totalPML

# This calculates bonus points for having met group size constraints
def pointsTeamSize(inputGA):
    totalPTS = 0
    weight_pts = load_csv.weightTeamSize
    group_size = [0] * 10

    def group(group_size):
        for i in load_csv.studentID:
            group_size[fauxGA[i]] = group_size[fauxGA[i]] + 1
        return group_size

    print(group(group_size))

    for i in range(len(group_size)):
        if group_size[i] > 0:
            print('mininum team size:', load_csv.minTeamSize[i])
            print('maximum team size:', load_csv.maxTeamSize[i])
            print('this group has', group_size[i], 'people')

            if load_csv.minTeamSize[i] <= group_size[i] and group_size[i] <= load_csv.maxTeamSize[i]:
                totalPTS += weight_pts
                print('total PTS score =', totalPTS)
            else:
                print('No bonus!')

    return totalPTS

# This calculates bonus for not violating student disallowance constraint
def pointsAvoid(inputGA):
    totalPSA = 0
    weight_psa = load_csv.weightAvoid

    for i in range(len(fauxGA)):
        if load_csv.studentID[i] != load_csv.studentAvoid1[i]:
            totalPSA += weight_psa
            print('total PSA score =', totalPSA)
        else:
            ('No bonus!')

    return totalPSA

def scoringMode(inputGA):
    print("Hello from a function")
    print(inputGA)
    score = 0
    
    #score = pointsStudentChoice(inputGA)
    #print('score after PSC = ', score)
    #score += pointsESLStudents(inputGA)
    #print('score after PES = ', score)
    #score += pointsStudentPriority(inputGA)
    #print('score after PSP = ', score)
    
    #score += pointsMaxLowGPAStudents(inputGA)
    #print('score after PML = ', score)
    #score += pointsTeamSize(inputGA)
    #print('score after PTS = ', score)
    score += pointsAvoid(inputGA)
    print('score after PSA = ', score)

    print('score grand total =', score)

cat = 'Vera'
scoringMode(cat)