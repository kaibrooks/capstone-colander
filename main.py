import names
import argparse
import pandas as pd
import random

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--students", help="Number of students", required=False, default=100)
parser.add_argument("-p", "--projects", help="Number of projects", required=False, default=25)

argument = parser.parse_args()
if argument.students:
    students = int(argument.students)
if argument.projects:
    projects = int(argument.projects)

df = pd.DataFrame(columns=['studentName', 'studentID', 'studentGPA', 'studentESL', 'studentPriority'])
fd = pd.DataFrame(columns=['projectName', 'projectID', 'minTeamSize', 'maxTeamSize', 'customField'])

ESLs, firstPriority, GPAs, studentAvoid, customField, studentChoice = [], [], [], [], [], []
minTeamSize, maxTeamSize = [], []

i = 0
while i < students:
    name = names.get_full_name()
    df = df.append({'studentName': name}, ignore_index=True)
    tempESL = random.choices([0, 1], weights=[75, 25])
    tempESL = tempESL[0]
    ESLs.append(tempESL)
    tempPriority = random.choices([0, 1], weights=[90, 10])
    tempPriority = tempPriority[0]
    firstPriority.append(tempPriority)
    tempGPA = round(random.uniform(2,4), 2)
    GPAs.append(tempGPA)
    i += 1

newData = pd.DataFrame({'studentGPA': GPAs})
df.update(newData)
newData = pd.DataFrame({'studentESL': ESLs})
df.update(newData)
newData = pd.DataFrame({'studentPriority': firstPriority})
df.update(newData)

studentsIDs = random.sample(range(99999999), students)
newData = pd.DataFrame({'studentID': studentsIDs})
df.update(newData)

i = 0
while i < projects:
    name = names.get_last_name()
    fd = fd.append({'projectName': name}, ignore_index=True)
    tempMinSize = random.choices(['',3,4])
    tempMinSize = tempMinSize[0]
    minTeamSize.append(tempMinSize)
    tempMaxSize = random.choices(['',4,5,6])
    tempMaxSize = tempMaxSize[0]
    maxTeamSize.append(tempMaxSize)
    i += 1

newData = pd.DataFrame({'minTeamSize': minTeamSize})
fd.update(newData)
newData = pd.DataFrame({'maxTeamSize': maxTeamSize})
fd.update(newData)

projectIDs = random.sample(range(77777777), projects)
newData = pd.DataFrame({'projectID': projectIDs})
fd.update(newData)

avoidChoices = random.choices([1,2,3,4], weights=[30,50,15,5])
avoidChoices = avoidChoices[0]

i = 1
while i <= avoidChoices:
    df['studentAvoid{0}'.format(i)] = ''
    i += 1

def studentAvoider(numStudents, percentage, colName):
    studentAvoid.clear()
    numStudents = int(round(numStudents * percentage))
    i = 1
    while i <= numStudents:
        tempAvoid = random.choice(studentsIDs)
        studentAvoid.append(int(tempAvoid))
        i += 1
    newData = pd.DataFrame({str(colName): studentAvoid})
    df.update(newData)

studentAvoider(float(len(studentsIDs)), .10, 'studentAvoid1')
if 'studentAvoid2' in df.columns:
    studentAvoider(float(len(studentsIDs)), .06, 'studentAvoid2')
if 'studentAvoid3' in df.columns:
    studentAvoider(float(len(studentsIDs)), .03, 'studentAvoid3')

numStudentChoices = random.choices([3,4,5,6,7], weights=[25,40,20,8,7])
numStudentChoices = numStudentChoices[0]

i = 1
while i <= numStudentChoices:
    df['studentChoice{0}'.format(i)] = ''
    i += 1

def projectChooser(numStudents, percentage, colName):
    studentChoice.clear()
    numStudents = int(round(numStudents * percentage))
    i = 1
    while i <= numStudents:
        tempChoice = random.choice(projectIDs)
        studentChoice.append(int(tempChoice))
        i += 1
    newData = pd.DataFrame({str(colName): studentChoice})
    df.update(newData)

projectChooser(float(len(studentsIDs)), .95, 'studentChoice1')
projectChooser(float(len(studentsIDs)), .85, 'studentChoice2')
projectChooser(float(len(studentsIDs)), .75, 'studentChoice3')
if 'studentChoice4' in df.columns:
    projectChooser(float(len(studentsIDs)), .5, 'studentChoice4')
if 'studentChoice5' in df.columns:
    studentAvoider(float(len(studentsIDs)), .3, 'studentChoice5')
if 'studentChoice6' in df.columns:
    studentAvoider(float(len(studentsIDs)), .1, 'studentChoice6')
if 'studentChoice7' in df.columns:
    studentAvoider(float(len(studentsIDs)), .05, 'studentChoice7')

df['customField'] = ''

first = ['David', 'Jae', 'Zoe', 'Kai', 'Bliss', 'The Killer Rabbit of Caerbannog']
second = ['loves', 'hates', 'once ate a group of', 'once bamboozled a group of', 'enjoys fighting']
third = ['clowns.', 'geese.', 'cold-hearted eskimos.', 'cooks who only make cottage pies.', 'knights in rusty armour.']

i = 0
while i < students:
    tempCustom1 = random.choice(first)+" "+random.choice(second)+" "+random.choice(third)
    tempCustom2 = ''
    tempCustom = random.choice([tempCustom1, tempCustom2])
    customField.append(tempCustom)
    i += 1
newData = pd.DataFrame({'customField': customField})
df.update(newData)

fourth = ['Easy Project!', 'Hard Project!', 'Confusing Project!', 'Fun Project!', '', 'Sponsor: The Killer Rabbit of Caerbannog.']
i = 0
customField.clear()
while i < projects:
    tempProjectCustom = random.choice(fourth)
    customField.append(tempProjectCustom)
    i += 1
newProjectData = pd.DataFrame({'customField': customField})
fd.update(newProjectData)

df.to_csv('students.csv', index=False)
fd.to_csv('projects.csv', index=False)