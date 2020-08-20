# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv
import pandas as pd

#load_csv.settingsHandler()
#load_csv.projectsHandler('projects.csv')
#load_csv.studentsHandler('students.csv')

def pointsStudentChoice(groupAssignments):
    totalPSC = 0
    number_choices = 5 # Replace with Zoe's studentHandler variable
    maxScore = load_csv.weightStudentChoice1
    
    # Students = rows (y), ProjectChoices = columns (x)
    for y in range(len(load_csv.studentID)):
        for x in range(len(load_csv.studentChoiceN.columns)):
            if pd.isna(load_csv.studentChoiceN.iat[y, x]) == True:
                pass
            elif load_csv.studentChoiceN.iat[y, x] == groupAssignments[y]:
                q = number_choices - len(load_csv.studentChoiceN.columns) # Test for student gaming
                totalPSC = totalPSC + math.ceil(maxScore - q * (maxScore / number_choices) - (maxScore / number_choices) * x)
                #totalPSC = totalPSC + math.ceil(maxScore - (maxScore / number_choices) * (q + x))
    return totalPSC

def pointsESLStudents(groupAssignments):
    pointWeight = load_csv.weightMaxESLStudents
    maxESL = load_csv.maxESLStudents
    totalPES = len(groupAssignments) * pointWeight; # Maximum possible score
    groupESL = [0] * len(load_csv.projectIDs) # Initializing an empty array to 0's

    for i in range(len(load_csv.studentID)):
        # Checking if a students ESL flag is set
        if load_csv.studentESL[i] == True:
            # The students actual assignment (groupAssignments[i]) is used to index into groupESL to
            # track how many ESL students are on that team.
            groupESL[groupAssignments[i]] += 1

            if groupESL[groupAssignments[i]] > maxESL:
                totalPES -= pointWeight

    return totalPES

def pointsStudentPriority(groupAssignments):
    totalPSP = 0

    # Checks if priority flag is set then checks if they got their first choice
    for i in range(len(load_csv.studentID)):
        if load_csv.studentPriority[i] == True:
            if groupAssignments[i] == load_csv.studentChoiceN.iat[i, 0]:
                totalPSP += load_csv.weightStudentPriority

    return totalPSP

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(groupAssignments):
    totalPML = 0
    weight_pml = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold
    maxLow = load_csv.maxLowGPAStudents
    maxLow_group = [0] * len(load_csv.projectIDs)
    group_size = [0] * len(load_csv.projectIDs)

    def maxgroup(maxLow_group):
        for i in range(len(load_csv.studentID)):
            if load_csv.studentGPA[i] < minGPA:
                maxLow_group[groupAssignments[i]] = maxLow_group[groupAssignments[i]] + 1
        return maxLow_group

    def sizegroup(group_size):
        for i in range(len(load_csv.studentID)):
            group_size[groupAssignments[i]] = group_size[groupAssignments[i]] + 1
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
def pointsTeamSize(groupAssignments):
    totalPTS = 0
    weight_pts = load_csv.weightTeamSize
    group_size = [0] * len(load_csv.projectIDs)

    def group(group_size):
        for i in range(len(load_csv.studentID)):
            group_size[groupAssignments[i]] = group_size[groupAssignments[i]] + 1
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
def pointsAvoid(groupAssignments):
    totalPSA = 0
    bad = 0
    weight_psa = load_csv.weightAvoid

    for j in range(len(load_csv.projectIDs)):
        #print('Group ID:',load_csv.projectIDs[j])
        for i in range(len(groupAssignments)):
            if groupAssignments[i] == j:                    
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

def scoringMode(groupAssignments): 
    groupAssignments = [0, 0, 2, 0, 1, 1, 1, 1, 9, 9, 2, 3, 4, 5, 6, 4, 4]

    print('Assignment: ', groupAssignments)
    score = 0
    
    score = pointsStudentChoice(groupAssignments)
    print('score after PSC = ', score)
    score += pointsESLStudents(groupAssignments)
    print('score after PES = ', score)
    score += pointsStudentPriority(groupAssignments)
    print('score after PSP = ', score)
    
    score += pointsMaxLowGPAStudents(groupAssignments)
    print('score after PML = ', score)
    score += pointsTeamSize(groupAssignments)
    print('score after PTS = ', score)
    score += pointsAvoid(groupAssignments)
    print('score after PSA = ', score)

    print('score grand total =', score)

    return score