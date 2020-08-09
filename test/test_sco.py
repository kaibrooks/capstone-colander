# run scoring tests
# kai brooks
# github.com/kaibrooks

import sys
sys.path.insert(1, 'src/') # look for imports in the project root
from score import pointsStudentChoice, pointsESLStudents, pointsStudentPriority, pointsMaxLowGPAStudents, pointsTeamSize, pointsAvoid

print('*** RUNNING TEST_SCO.PY ***')

# SCO-F001 - 'all-purpose' score
print('\n::: SCO-F001 :::')
cor_score = 1000 # correct score

# SCO-F002 - missing studentChoiceN
print('\n::: SCO-F001 :::')
cor_score = 400

# SCO-F003 - student assigned none of their choices
print('\n::: SCO-F003 :::')
cor_score = 200

# SCO-F004 - ESL constraint
print('\n::: SCO-F004 :::')
cor_score = 200

# SCO-F005 - group size constraint
print('\n::: SCO-F005 :::')
cor_score = 200

# SCO-F006 - group size constraint with default values 
print('\n::: SCO-F006 :::')
cor_score = 200

# SCO-F007 - student priority constraint
print('\n::: SCO-F007 :::')
cor_score = 300

# SCO-F008 - assumed null = 'false' in ESL constraint
print('\n::: SCO-F008 :::')
cor_score = 0

# SCO-F009 - studentAvoid constraint
print('\n::: SCO-F009 :::')
## cor_score should be the penalty applied 8 times

# SCO-F010 - maxLowGPAStudents constraint
print('\n::: SCO-F010 :::')
cor_score = 0