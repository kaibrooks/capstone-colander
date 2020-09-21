# Functions for scoring the Genetic Algorithm (GA) are stored here

import math  # ceil()
import load_csv
import pandas as pd
import prints


def pointsStudentChoice(groupAssignments):
    global totalPSC
    totalPSC = 0
    #maxNumChoices = load_csv.numStudentChoices
    maxScore = load_csv.weightStudentChoice1

    prints.debug(f"\n\n========pointsStudentChoice========\n{groupAssignments}")
    # This outputs the score for each student's choice's based on their actual assignment
    # Students = rows (y), ProjectChoices = columns (x)
    for y in range(len(load_csv.studentID)):
        for x in range(len(load_csv.studentChoiceN.columns)):
            # If NaN is detected gives score based on position x then breaks
            prints.debug(f"ID {load_csv.studentID.iat[y]}, Assignment {groupAssignments[y]}, Choice {load_csv.studentChoiceN.iat[y, x]}")
            
            if pd.isna(load_csv.studentChoiceN.iat[y, x]):
                if load_csv.studentChoiceN.iat[y, 0] == groupAssignments[y]: # May be deletable pending Zoe's feedback
                        totalPSC += maxScore
                        prints.debug(f"Score {totalPSC}")
                        break

                totalPSC += math.ceil(maxScore / (2 ** x))
                prints.debug(f"Score {totalPSC}")
                break

            # If an assignment match is detected gives score based on position x then breaks
            else:
                if load_csv.studentChoiceN.iat[y, x] == groupAssignments[y]:
                    if load_csv.studentChoiceN.iat[y, 0] == groupAssignments[y]:
                        totalPSC += maxScore
                        prints.debug(f"Score {totalPSC}")
                        break

                    totalPSC += math.ceil(maxScore / (2 ** x))
                    prints.debug(f"Score {totalPSC}")
                    break

            # if pd.isna(load_csv.studentChoiceN.iat[y, x]):
            #     totalPSC += math.ceil(maxScore - (maxScore / maxNumChoices) * x)
            #     prints.debug(f"Score {totalPSC}")
            #     break

            # # If an assignment match is detected gives score based on position x then breaks
            # else:
            #     if load_csv.studentChoiceN.iat[y, x] == groupAssignments[y]:
            #         totalPSC += math.ceil(maxScore - (maxScore / maxNumChoices) * x)
            #         prints.debug(f"Score {totalPSC}")
            #         break

    return totalPSC


def pointsESLStudents(groupAssignments):
    global totalPES
    totalPES = 0

    pointWeight = load_csv.weightMaxESLStudents
    maxESL = load_csv.maxESLStudents
    groupESL = [0] * len(load_csv.projectIDs)  # Initializing an empty array to 0's
    groupSize = [0] * len(load_csv.projectIDs)

    prints.debug(f"\n\n========pointsESLStudents========\n{groupESL} gESL Before \n{groupSize} gSize Before")
    # groupESL[i] is the number of ESL students on team i
    for i in range(len(load_csv.studentID)):
        if load_csv.studentESL[i]:
            groupESL[groupAssignments[i]] += 1  # ESL students per team
        groupSize[groupAssignments[i]] += 1  # Students per team

    prints.debug(f"{groupESL} gESL After \n{groupSize} gSize After")
    # Awarding points
    for i in range(len(groupESL)):
        if groupESL[i] <= maxESL and groupSize[i] >= load_csv.minTeamSize[i]:
            totalPES += pointWeight

    return totalPES


def pointsStudentPriority(groupAssignments):
    global totalPSP
    totalPSP = 0

    # Checks if priority flag is set then checks if they got their first choice
    for i in range(len(load_csv.studentID)):
        if load_csv.studentPriority[i]:
            if groupAssignments[i] == load_csv.studentChoiceN.iat[i, 0]:
                totalPSP += load_csv.weightStudentPriority

    return totalPSP


# This calculates points for having fewer students than maxLowGPAStudents in a group
def pointsMaxLowGPAStudents(groupAssignments):
    global totalPML
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

    prints.debug("========pointsMaxLowGPAStudents========")
    prints.debug(f"groups with lowGPA students: {maxLowGroup}")
    prints.debug(f"groups with # of studetns: {groupSize}")

    # iterates through maxLowGroup for points - also ignores empty groups
    for i in range(len(maxLowGroup)):
        if maxLowGroup[i] <= maxLow and groupSize[i] >= load_csv.minTeamSize[i]:
            prints.debug(f"group: {load_csv.projectIDs[i]} satisfies the condition!")
            totalPML += weightPML

    return totalPML


# This calculates points for having met group size constraints
def pointsTeamSize(groupAssignments):
    global totalPTS
    totalPTS= 0
    weightMinPTS = load_csv.weightMinTeamSize
    weightMaxPTS = load_csv.weightMaxTeamSize

    # initialize groupSize - counts how many students there are in each group
    groupSize = [0] * len(load_csv.projectIDs)

    # loop for counting group size
    for i in range(len(load_csv.studentID)):
        # print(groupSize[groupAssignments[i]], groupAssignments[i], i)
        groupSize[groupAssignments[i]] += 1

    prints.debug("========pointsTeamSize========")
    prints.debug(f"group size: {groupSize}")
    prints.debug(f"min size: {load_csv.minTeamSize}")
    prints.debug(f"max size: {load_csv.maxTeamSize}")

    # iterates through groupSize to identify group meeting the size constraints
    for i in range(len(groupSize)):
        if load_csv.minTeamSize[i] - 1 > groupSize[i] and groupSize[i] > 0:
            totalPTS -= weightMinPTS
            prints.debug(f"group{[i]} teamSize:{groupSize[i]} points:{totalPTS}")
            continue
        if load_csv.minTeamSize[i] <= groupSize[i]:
            totalPTS += weightMinPTS
            if groupSize[i] > load_csv.maxTeamSize[i] + 1:
                totalPTS -= weightMaxPTS
                continue
            if groupSize[i] <= load_csv.maxTeamSize[i]:
                totalPTS += weightMaxPTS
        prints.debug(f"group{[i]} teamSize:{groupSize[i]} points:{totalPTS}")

    return totalPTS


# This calculates points for violating studentAvoid constraint
def pointsAvoid(groupAssignments):
    global totalPSA
    totalPSA = 0
    weightPSA = load_csv.weightAvoid
    # initializes bad - counts how many studentAvoid matches are found
    bad = 0

    prints.debug("========pointsAvoid========")
    # prints.debug(f"{load_csv.studentAvoid}")

    for i in range(load_csv.numStudents):
        # skips student with empty avoid value
        if pd.isna(load_csv.studentAvoid[i]) is False:
            # stores studentAvoid data to 'avoid'
            avoid = int(load_csv.studentAvoid[i])
            prints.debug("======student loop======")
            prints.debug(f"student: {[i]} avoid: {avoid}")
            prints.debug(f"student group: {groupAssignments[i]}")
            prints.debug(f"avoid group: {groupAssignments[avoid]}")
            # identifies studentAvoid match within in same group
            if groupAssignments[i] == groupAssignments[avoid]:
                prints.debug("studentAvoid match found")
                bad += 1

    prints.debug(f"bad: {bad}")
    totalPSA -= (weightPSA * bad)

    return totalPSA


def scoringMode(groupAssignments):
    score = 0

    score = pointsStudentChoice(groupAssignments)
    #score += pointsESLStudents(groupAssignments)
    #score += pointsStudentPriority(groupAssignments)

    #score += pointsMaxLowGPAStudents(groupAssignments)
    score += pointsTeamSize(groupAssignments)
    #score += pointsAvoid(groupAssignments)

    prints.score(f"\nstudentChoice score: {totalPSC}")
    # prints.score(f"ESLStudents score: {totalPES}")
    # prints.score(f"studentPriority score: {totalPSP}")
    # prints.score(f"maxLowGPA score: {totalPML}")
    prints.score(f"teamSize score: {totalPTS}")
    # prints.score(f"studentAvoid score: {totalPSA}")

    #prints.score(f"\nscore grand total = {score}")

    return score
