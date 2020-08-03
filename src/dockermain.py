# this is a "staging" file, it just calls another file
# it's here because docker always runs "dockermain.py"
# change the actual file to run on the last line
# don't develop in this

import os
from datetime import date, datetime

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S') # get the date/time
print("Container built", now) # print it

# call another script
os.system('python src/run_ga.py') # put what file we actually want run here