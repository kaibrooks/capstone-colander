import sys


def printError(msg):
    sys.exit("\nERROR: " + msg)

def printWarning(msg):
    print("\nWARNING: " + msg)

def printGeneral(msg):
    print("\n** " + msg + " **")