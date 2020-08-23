# run scoring tests
# kai brooks
# github.com/kaibrooks
​
import sys
sys.path.insert(1, 'src/') # look for imports in the project root
from score import pointsStudentChoice, pointsESLStudents, pointsStudentPriority, pointsMaxLowGPAStudents, pointsTeamSize, pointsAvoid
​
print('*** RUNNING TEST_SCO.PY ***')
​
# SCO-F001 - 'all-purpose' score
print('\n::: SCO-F001 :::')
cor_score = 700 # correct score
##### still needs to be tested #######
​
# SCO-F002 - missing studentChoiceN
print('\n::: SCO-F002 :::')
cor_score = 400
# Result: Passed
​
# SCO-F003 - student assigned none of their choices
print('\n::: SCO-F003 :::')
cor_score = 0
# Result: Passed
​
# SCO-F004 - ESL constraint
print('\n::: SCO-F004 :::')
cor_score = 200
# Result: Failed
# Note: Score of 400 was calculated.
# seems like ESL points was counted 4 times rather than twice for each group.
​
# SCO-F005 - group size constraint
print('\n::: SCO-F005 :::')
cor_score = 200
# Result: Passed
​
# SCO-F006 - group size constraint with default values
print('\n::: SCO-F006 :::')
cor_score = 200
# Result: Passed
​
# SCO-F007 - student priority constraint
print('\n::: SCO-F007 :::')
cor_score = 300
# Result: Passed
​
# SCO-F008 - assumed null = 'false' in ESL constraint
print('\n::: SCO-F008 :::')
cor_score = 0
# Result: Passed
​
# SCO-F009 - studentAvoid constraint
print('\n::: SCO-F009 :::')
cor_score = -800
##### still needs to be tested #######
​
# SCO-F010 - maxLowGPAStudents constraint
print('\n::: SCO-F010 :::')
cor_score = 0
# Result: Passed

# SCO-F011 - different studentChoiceN's filled
print('\n::: SCO-F011 :::')
cor_score = 550
# Result: Failed
# Note: Score of 820 was calculated
