# Bliss Brass & Jaeyoon Lee
# Functions for scoring the Genetic Algorithm (GA) are stored here
# ##-##-2020

import math # ceil()
import load_csv
import pandas as pd
import prints


def pointsStudentChoice(groupAssignments):
    totalPSC = 0
    maxNumChoices = 5
    #maxNumChoices = load_csv.numStudentChoices
    maxScore = load_csv.weightStudentChoice1

    # This outputs the score for each student's choice's based on their actual assignment
    # Students = rows (y), ProjectChoices = columns (x)
    for y in range(len(load_csv.studentID)):
        for x in range(len(load_csv.studentChoiceN.columns)):
            prints.debug(f"ID {load_csv.studentID.iat[y]}, Choice {load_csv.studentChoiceN.iat[y, x]}")

            # If NaN is detected gives score based on x position then breaks
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
    totalPES = len(groupAssignments) * pointWeight; # Maximum possible score
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

# This calculates bonus points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(groupAssignments):
    totalPML = 0
    weightPML = load_csv.weightMaxLowGPAStudents
    minGPA = load_csv.lowGPAThreshold       # loads minimum GPA constraint
    maxLow = load_csv.maxLowGPAStudents     # loads maximum students with low GPA constraint
    # initialize maxLowGroup - counts how many per group do not meet minGPA constraint
    maxLowGroup = [0] * len(load_csv.projectIDs)
    # initialize groupSize - counts how many students there are in per group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting maxLowGPA students and group sizes
    for i in range(len(load_csv.studentID)):
        if load_csv.studentGPA[i] < minGPA:
            maxLowGroup[groupAssignments[i]] += 1
        groupSize[groupAssignments[i]] += 1

    prints.debug('groups with lowGPA students:',maxLowGroup)
    prints.debug('groups with # of studetns:',groupSize)

    # iterates through mawLowGroup for points - also ignores empty groups
    for i in range(len(maxLowGroup)):
        if maxLowGroup[i] <= maxLow and groupSize[i] > 0: 
            prints.debug('group:',load_csv.projectIDs[i],'satisfies the condition!')
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

    prints.debug('group size:',groupSize)
    prints.debug('min size:',load_csv.minTeamSize)
    prints.debug('max size:',load_csv.maxTeamSize)

    # iterates through groupSize to see if a group meets the size constraints
    for i in range(len(groupSize)):
        #print(load_csv.minTeamSize[i],load_csv.maxTeamSize[i],groupSize[i])
        if load_csv.minTeamSize[i] <= groupSize[i] <= load_csv.maxTeamSize[i]:
            prints.debug('project:',load_csv.projectIDs[i],'satisfies the condition!')
            prints.debug('project:',load_csv.projectIDs[i],'Min:',load_csv.minTeamSize[i],'Max:',load_csv.maxTeamSize[i],'group size:',groupSize[i])
            totalPTS += weightPTS

    return totalPTS

# This calculates penalty for violating studentAvoid constraint
def pointsAvoid(groupAssignments):
    totalPSA = 0
    weightPSA = load_csv.weightAvoid
    # initializes bad - counts how many avoid matches happen per group
    bad = 0

    for i in range(len(load_csv.studentID)):
        prints.debug('=========== Assignment:',load_csv.projectIDs[groupAssignments[i]],[i],'===========')
        for j in range(len(load_csv.studentAvoid1)):
            prints.debug([i],'student:',load_csv.studentID[i])
            prints.debug([j],'avoid1:',load_csv.studentAvoid1[j])
            # iterates through student ID and Avoid columns for possible violation
            if load_csv.studentID[i] == load_csv.studentAvoid1[j]:
                # only counts violation if in same group
                if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[j]]:
                    prints.debug('match detected in the same group!')
                    bad += 1

    for i in range(len(load_csv.studentID)):
        prints.debug('=========== Assignment:',load_csv.projectIDs[groupAssignments[i]],[i],'===========')
        for j in range(len(load_csv.studentAvoid2)):
            prints.debug([i],'student:',load_csv.studentID[i])
            prints.debug([j],'avoid2:',load_csv.studentAvoid2[j])
            if load_csv.studentID[i] == load_csv.studentAvoid2[j]:
                if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[j]]:
                    prints.debug('match detected in the same group!')
                    bad += 1
 
    for i in range(len(load_csv.studentID)):
        prints.debug('=========== Assignment:',load_csv.projectIDs[groupAssignments[i]],[i],'===========')
        for j in range(len(load_csv.studentAvoid3)):
            prints.debug([i],'student:',load_csv.studentID[i])
            prints.debug([j],'avoid3:',load_csv.studentAvoid3[j])
            if load_csv.studentID[i] == load_csv.studentAvoid3[j]:
                if load_csv.projectIDs[groupAssignments[i]] == load_csv.projectIDs[groupAssignments[j]]:
                    prints.debug('match detected in the same group!')
                    bad += 1


    #print('bad: ',bad)
    totalPSA -= (weightPSA * bad)

    return totalPSA

def scoringMode(groupAssignments):

    prints.debug(f"\nAssignment:\n', {groupAssignments}")
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