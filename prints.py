# message printing for localization
# use string interpolation to print with vars: prints.printGeneral(f"there are {var} things")

import sys


def printError(msg):
    """prints and error message and exits"""
    sys.exit("\nERROR: " + msg)

def printWarning(msg):
    """prints a warning"""
    print("\nWARNING: " + msg)

def printGeneral(msg):
    """prints a general message"""
    print("" + msg)
    
def logerr(msg):
    """prints an error message"""
    print("\nERROR: " + msg)
