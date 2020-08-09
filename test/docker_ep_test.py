# docker entrypoint for test

import os
from datetime import date, datetime

# startup information
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S') # get the date/time
print("Container built", now) # print it

# call another script
os.system('python test/test_sco.py') # put what file we actually want run here