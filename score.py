# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv

def pointsStudentChoice(inputArray):
    totalPSC = 0
    number_choices = 5
    points_max = load_csv.weightStudentChoice1
    
    # Students = rows (y), ProjectChoices = columns (x)
    for y in range(len(load_csv.studentID)):
        for x in range(len(load_csv.studentChoiceN.columns)):
            if load_csv.studentChoiceN.iat[y, x] == inputArray[y]:
                totalPSC = totalPSC + math.ceil(points_max - (points_max / number_choices) * x)

    return totalPSC

def pointsESLStudents(inputArray):
    totalPES = 0
    point_weight = load_csv.weightMaxESLStudents
    maxESL = load_csv.maxESLStudents

    # Initializing an empty array to 0's
    ESL_Group = [0] * len(load_csv.studentID)

    for i in range(len(load_csv.studentID)):
        # Checking if a students ESL flag is set to 1
        if load_csv.studentESL[i] == 1:
            # The students actual assignment (inputArray[i]) is used to index into ESL_Group to
            # track how many ESL students are on that team.
            ESL_Group[inputArray[i]] = ESL_Group[inputArray[i]] + 1

            if ESL_Group[inputArray[i]] > maxESL:
                totalPES -= point_weight
                #print(totalPES, 'Current total')
    #print(ESL_Group, 'ESL_Group After')

    return totalPES

def pointsStudentPriority(inputArray):
    totalPSP = 0

    # Checks if priority flag is set then checks if they got their first choice
    for i in range(len(load_csv.studentID)):
        if load_csv.studentPriority[i] == 1:
            if inputArray[i] == load_csv.studentChoiceN.iat[i, 0]:
                totalPSP += load_csv.weightStudentPriority

    return totalPSP

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(inputArray):
    totalPML = 0
    weight_pml = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold
    maxLow = load_csv.maxLowGPAStudents
    maxLow_group = [0] * len(load_csv.projectIDs)
    group_size = [0] * len(load_csv.projectIDs)

    def maxgroup(maxLow_group):
        for i in range(len(load_csv.studentID)):
            if load_csv.studentGPA[i] < minGPA:
                maxLow_group[inputArray[i]] = maxLow_group[inputArray[i]] + 1
        return maxLow_group

    def sizegroup(group_size):
        for i in range(len(load_csv.studentID)):
            group_size[inputArray[i]] = group_size[inputArray[i]] + 1
        return group_size

    maxgroup(maxLow_group)
    sizegroup(group_size)

    for i in range(len(maxLow_group)):
        if maxLow_group[i] >= 0 and maxLow_group[i] <= maxLow and group_size[i] > 0: 
            totalPML += weight_pml
        else:
            pass

    return totalPML

# This calculates bonus points for having met group size constraints
def pointsTeamSize(inputArray):
    totalPTS = 0
    weight_pts = load_csv.weightTeamSize
    group_size = [0] * len(load_csv.projectIDs)

    def group(group_size):
        for i in range(len(load_csv.studentID)):
            group_size[inputArray[i]] = group_size[inputArray[i]] + 1
        return group_size

    group(group_size)

    for i in range(len(group_size)):
        if group_size[i] > 0:
            if load_csv.minTeamSize[i] <= group_size[i] and group_size[i] <= load_csv.maxTeamSize[i]:
                totalPTS += weight_pts
            else:
                pass

    return totalPTS

# This calculates penalty for violating studentAvoid constraint
def pointsAvoid(inputArray):
    totalPSA = 0
    bad = 0
    weight_psa = load_csv.weightAvoid

    for j in range(len(load_csv.projectIDs)):
        #print('Group ID:',load_csv.projectIDs[j])
        for i in range(len(inputArray)):
            if inputArray[i] == j:                    
                #print('ID:',load_csv.studentID[i],'Avoid:',load_csv.studentAvoid1[i])
                if load_csv.studentAvoid1[i] == load_csv.studentID[j]:
                    #print('match detected!','student:',load_csv.studentID[j],',matches with Avoid:',load_csv.studentAvoid1[i])
                    bad += 1                
                if load_csv.studentAvoid1[j] == load_csv.studentID[i]:
                    #print('match detected!','student:',load_csv.studentID[i],',matches with Avoid:',load_csv.studentAvoid1[j])
                    bad += 1  
                if any(load_csv.studentAvoid1) == load_csv.studentID[i]:
                    #print('match detected!','student:',load_csv.studentID[i],',matches with Avoid:',load_csv.studentAvoid1[i])
                    bad += 1                       

    #print('bad: ',bad)
    totalPSA -= (weight_psa * bad)

    return totalPSA

def scoringMode(inputArray): 
    inputArray = [0, 0, 2, 0, 1, 1, 1, 1, 9, 9, 2, 3, 4, 5, 6, 4, 4]

    print('Assignment: ', inputArray)
    score = 0
    
    score = pointsStudentChoice(inputArray)
    print('score after PSC = ', score)
    score += pointsESLStudents(inputArray)
    print('score after PES = ', score)
    score += pointsStudentPriority(inputArray)
    print('score after PSP = ', score)
    
    score += pointsMaxLowGPAStudents(inputArray)
    print('score after PML = ', score)
    score += pointsTeamSize(inputArray)
    print('score after PTS = ', score)
    score += pointsAvoid(inputArray)
    print('score after PSA = ', score)

    print('score grand total =', score)

    return score