# Bliss Brass
#for variable_name in range(start, stop, step)

from array import *
import struct

# var = struct.pack('hhl',1,2,3) 
#Projects = struct.pack('iii', )
#Students = struct.pack('if?ifi', )
rows, cols = (5, 5)


class Students:
    "Stores name and place pairs"
    def __init__(self, name, place):
        self.name = name
        self.place = place

class Projects(object):
    "Stores ProjectID's and team min/max sizes"
    def __init__(self):
        self.projectID = 0
        self.minTeamSize = 3
        self.maxTeamSize = 4

dataStructure = [[Projects() for i in range(cols)] for j in range(rows)] 
#segmentList = [Segment() for i in range(10)]

# Declaring a 2D array and initializing its elements to 0
#dataStructure = [[0 for i in range(cols)] for j in range(rows)] 

def scoringMode(dataStructure, a):
    print("Hello from a function")
    
    dataStructure[0][0] = 1
    for row in dataStructure:
        print(row) 

cat = 5
scoringMode(dataStructure, cat)
