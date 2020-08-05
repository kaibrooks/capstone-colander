# message printing for localization
# github.com/kaibrooks/capstone-colander

import sys

def printError(msg):
    """prints and error message and exits"""
    sys.exit("\nERROR: " + msg)

def printWarning(msg):
    """prints a warning"""
    print("\nWARNING: " + msg)

def printGeneral(msg):
    """prints a general message"""
    print("\n" + msg)