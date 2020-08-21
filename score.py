# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv
import pandas as pd
import prints

#load_csv.settingsHandler()
#load_csv.projectsHandler('projects.csv')
#load_csv.studentsHandler('students.csv')

def pointsStudentChoice(groupAssignments):
    totalPSC = 0
    number_choices = 5 # Replace with Zoe's studentHandler variable
    maxScore = load_csv.weightStudentChoice1
    print(load_csv.studentID)
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
    weightPML = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold
    maxLow = load_csv.maxLowGPAStudents    
    # initialize maxLowGroup - counts how many per group do not meet minGPA constraint
    maxLowGroup = [0] * len(load_csv.projectIDs)
    # initialize groupSize - counts how many students there are in per group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting maxLowGPA students and group sizes
    for i in range(len(load_csv.studentID)):
        if load_csv.studentGPA[i] < minGPA:
            maxLowGroup[groupAssignments[i]] += 1
        groupSize[groupAssignments[i]] += 1

    prints.debug(f"========pointsMaxLowGPAStudents========")
    prints.debug(f"groups with lowGPA students: {maxLowGroup}")
    prints.debug(f"groups with # of studetns: {groupSize}")

    # iterates through mawLowGroup for points - also ignores empty groups
    for i in range(len(maxLowGroup)):
        if maxLowGroup[i] <= maxLow and groupSize[i] > 0: 
            prints.debug(f"group: {load_csv.projectIDs[i]} satisfies the condition!")
            totalPML += weightPML

    return totalPML

# This calculates bonus points for having met group size constraints
def pointsTeamSize(groupAssignments):
    totalPTS = 0
    weightPTS = load_csv.weightTeamSize 
    # initialize groupSize - counts how many students there are in per group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting group size
    for i in range(len(load_csv.studentID)):
        groupSize[groupAssignments[i]] += 1

    prints.debug(f"========pointsTeamSize========")
    prints.debug(f"group size: {groupSize}")
    prints.debug(f"min size: {load_csv.minTeamSize}")
    prints.debug(f"max size: {load_csv.maxTeamSize}")

    # iterates through groupSize to see if a group meets the size constraints
    for i in range(len(groupSize)):
        if load_csv.minTeamSize[i] <= groupSize[i] <= load_csv.maxTeamSize[i]:
            prints.debug(f"project: {load_csv.projectIDs[i]} satisfies the condition!")
            prints.debug(f"project: {load_csv.projectIDs[i]} Min:{load_csv.minTeamSize[i]} Max: {load_csv.maxTeamSize[i]} group size: {groupSize[i]}")
            totalPTS += weightPTS

    return totalPTS

# This calculates penalty for violating studentAvoid constraint
def pointsAvoid(groupAssignments):
    totalPSA = 0
    weightPSA = load_csv.weightAvoid
    # initializes bad - counts how many avoid matches happen per group
    bad = 0

    prints.debug(f"========pointsAvoid========")
    prints.debug(f"{load_csv.studentAvoidN['studentAvoid']}")

    for i in range(len(load_csv.studentID)):
        # looks through Avoid column for matches - if column doens't exist, passes
        try:
            print('=========== Assignment:',load_csv.projectIDs[groupAssignments[i]],[i],'===========')
            for j in range(len(load_csv.studentAvoidN['studentAvoid'])):
                prints.debug(f"{[i]}student:{load_csv.studentID[i]}")
                prints.debug(f"{[j]}avoid1:{load_csv.studentAvoidN['studentAvoid'][j]}")
                # iterates through student ID and Avoid columns for possible violation
                if load_csv.studentID[i] == load_csv.studentAvoidN['studentAvoid'][j]:
                    # only counts violation if in same group
                    if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[j]]:
                        prints.debug(f"match detected in the same group!")
                        bad += 1
                        break
        except:
            pass
        try:            
            print('=========== Assignment:',load_csv.projectIDs[groupAssignments[i]],[i],'===========')
            for k in range(len(load_csv.studentAvoidN['studentAvoid2'])):
                prints.debug(f"{[i]}student:{load_csv.studentID[i]}")
                prints.debug(f"{[k]}avoid2:{load_csv.studentAvoidN['studentAvoid2'][k]}")
                # iterates through student ID and Avoid columns for possible violation
                if load_csv.studentID[i] == load_csv.studentAvoidN['studentAvoid2'][k]:
                    # only counts violation if in same group
                    if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[k]]:
                        prints.debug(f"match detected in the same group!")
                        bad += 1
                        break
        except:
            pass
        try:                    
            prints.debug(f"=========== Assignment:{load_csv.projectIDs[groupAssignments[i]]}{[i]}===========")
            for l in range(len(load_csv.studentAvoid3)):
                prints.debug(f"{[i]}student:{load_csv.studentID[i]}")
                prints.debug(f"{[l]}avoid3:{load_csv.studentAvoidN['studentAvoid3'][l]}")
                # iterates through student ID and Avoid columns for possible violation
                if load_csv.studentID[i] == load_csv.studentAvoidN['studentAvoid3'][l]:
                    # only counts violation if in same group
                    if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[l]]:
                        prints.debug(f"match detected in the same group!")
                        bad += 1
                        break
        except:
            pass
        
    prints.debug(f"bad: {bad}")
    totalPSA -= (weightPSA * bad)

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