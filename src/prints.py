# message printing for localization
# use string interpolation to print with vars: prints.printGeneral(f"there are {var} things")

import sys

global debugMode
debugMode = 0


def debug(msg):
    """prints a debugging message"""
    if debugMode:
        print("" + msg)


def check_debug():
    """check if debug mode is on"""
    return debugMode


def err(msg):
    """prints and error message and exits"""
    sys.exit("\nERROR: " + msg)


def warn(msg):
    """prints a warning"""
    print("\nWarning: " + msg)


def gen(msg):
    """prints a general message"""
    print(msg)


def logerr(msg):
    """prints an error message"""
    print("\nERROR: " + msg)


def score(msg):
    """prints a score"""
    #print("" + msg)