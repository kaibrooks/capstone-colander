# message printing for localization
# use string interpolation to print with vars: prints.gen(f"there are {var} things")

import sys


def err(msg):
    """prints and error message and exits"""
    sys.exit("\nERROR: " + msg)

def warn(msg):
    """prints a warning"""
    print("\nWARNING: " + msg)

def gen(msg):
    """prints a general message"""
    print("\n" + msg)
    
def logerr(msg):
    """prints an error message"""
    print("\nERROR: " + msg)
