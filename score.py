# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv
import pandas as pd
import prints

def pointsStudentChoice(groupAssignments):
    totalPSC = 0
    maxNumChoices = load_csv.numStudentChoices
    maxScore = load_csv.weightStudentChoice1

    # This outputs the score for each student's choice's based on their actual assignment
    # Students = rows (y), ProjectChoices = columns (x)
    for y in range(len(load_csv.studentID)):
        for x in range(len(load_csv.studentChoiceN.columns)):
            # If NaN is detected gives score based on x position then breaks
            prints.debug(f"ID {load_csv.studentID.iat[y]}, Choice {load_csv.studentChoiceN.iat[y, x]}")

            if pd.isna(load_csv.studentChoiceN.iat[y, x]) == True:
                totalPSC = totalPSC + math.ceil(maxScore - (maxScore / maxNumChoices) * x)
                prints.debug(f"Score {totalPSC}")

                break
            
            # If an assignment match is detected gives score based on position x then breaks
            elif pd.isna(load_csv.studentChoiceN.iat[y, x]) == False:
                if load_csv.studentChoiceN.iat[y, x] == groupAssignments[y]:
                    totalPSC = totalPSC + math.ceil(maxScore - (maxScore / maxNumChoices) * x)
                    prints.debug(f"Score {totalPSC}")

                    break

    return totalPSC

def pointsESLStudents(groupAssignments):
    pointWeight = load_csv.weightMaxESLStudents
    maxESL = load_csv.maxESLStudents
    totalPES = len(groupAssignments) * pointWeight # Maximum possible score
    groupESL = [0] * len(load_csv.projectIDs) # Initializing an empty array to 0's

    # groupESL[i] is the number of ESL students on team i
    for i in range(len(load_csv.studentID)):
        # Checking if a students ESL flag is set
        if load_csv.studentESL[i] == True:
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

# This calculates points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(groupAssignments):
    totalPML = 0
    weightPML = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold
    maxLow = load_csv.maxLowGPAStudents    
    # initialize maxLowGroup - counts how many per group do not meet minGPA constraint
    maxLowGroup = [0] * len(load_csv.projectIDs)
    # initialize groupSize - counts how many students there are in each group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting maxLowGPA students and group sizes
    for i in range(len(load_csv.studentID)):
        if load_csv.studentGPA[i] < minGPA:
            maxLowGroup[groupAssignments[i]] += 1
        groupSize[groupAssignments[i]] += 1

    prints.debug(f"========pointsMaxLowGPAStudents========")
    prints.debug(f"groups with lowGPA students: {maxLowGroup}")
    prints.debug(f"groups with # of studetns: {groupSize}")

    # iterates through maxLowGroup for points - also ignores empty groups
    for i in range(len(maxLowGroup)):
        if maxLowGroup[i] <= maxLow and groupSize[i] > 0: 
            prints.debug(f"group: {load_csv.projectIDs[i]} satisfies the condition!")
            totalPML += weightPML

    return totalPML

# This calculates points for having met group size constraints
def pointsTeamSize(groupAssignments):
    totalPTS = 0
    weightPTS = load_csv.weightTeamSize 
    # initialize groupSize - counts how many students there are in each group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting group size
    for i in range(len(load_csv.studentID)):
        groupSize[groupAssignments[i]] += 1

    prints.debug(f"========pointsTeamSize========")
    prints.debug(f"group size: {groupSize}")
    prints.debug(f"min size: {load_csv.minTeamSize}")
    prints.debug(f"max size: {load_csv.maxTeamSize}")

    # iterates through groupSize to identify group meeting the size constraints
    for i in range(len(groupSize)):
        if load_csv.minTeamSize[i] <= groupSize[i] <= load_csv.maxTeamSize[i]:
            prints.debug(f"project: {load_csv.projectIDs[i]} satisfies the condition!")
            prints.debug(f"project: {load_csv.projectIDs[i]} Min:{load_csv.minTeamSize[i]} Max: {load_csv.maxTeamSize[i]} group size: {groupSize[i]}")
            totalPTS += weightPTS

    return totalPTS

# This calculates points for violating studentAvoid constraint
def pointsAvoid(groupAssignments):
    totalPSA = 0
    weightPSA = load_csv.weightAvoid
    # initializes bad - counts how many studentAvoid matches are found
    bad = 0

    prints.debug(f"========pointsAvoid========")
    #prints.debug(f"{load_csv.studentAvoid}")
    
    for i in range(load_csv.numStudents):
        # skips student with empty avoid value
        if pd.isna(load_csv.studentAvoid[i]) == False:
            # stores studentAvoid data to 'avoid'
            avoid = load_csv.studentAvoid[i]
            prints.debug(f"======student loop======")
            prints.debug(f"student: {[i]} avoid: {avoid}")
            prints.debug(f"student group: {load_csv.studentAssignment[i]}")
            prints.debug(f"avoid group: {load_csv.studentAssignment[avoid]}")
            # identifies studentAvoid match within in same group
            if load_csv.studentAssignment[i] == load_csv.studentAssignment[avoid]:
                prints.debug(f"studentAvoid match found")
                bad += 1
    
    prints.debug(f"bad: {bad}")
    totalPSA -= (weightPSA * bad)

    return totalPSA

def scoringMode(groupAssignments): 
    groupAssignments = [0, 5, 2, 3, 1, 1, 1, 1, 9, 9, 2, 3, 4, 5, 6, 4, 4]

    prints.debug(f"Assignment: {groupAssignments}")
    score = 0
    
    #score = pointsStudentChoice(groupAssignments)
    #print('score after PSC = ', score)
    #score += pointsESLStudents(groupAssignments)
    #print('score after PES = ', score)
    #score += pointsStudentPriority(groupAssignments)
    #print('score after PSP = ', score)
    
    #score += pointsMaxLowGPAStudents(groupAssignments)
    #print('score after PML = ', score)
    #score += pointsTeamSize(groupAssignments)
    #print('score after PTS = ', score)
    score += pointsAvoid(load_csv.studentAssignment)
    print('score after PSA = ', score)

    print('score grand total =', score)

    return score