# script for running tests

import sys
import main

print('*** RUNNING TEST_CSV.PY ***')

# CSV-F005: column rearranged

# CSV-E007: missing project ID column

# CSV-E008: missing minTeamSize name and value

# CSV-E009: missing maxTeamSize name and value

# CSV-E037: projectID is not an integer

# CSV-E038: projectID is out of range

# CSV-E039: projectID is not unique

# CSV-E040: projectID numbers are not sequential from 1

# CSV-E041: minTeamSize is not an integer

# CSV-E042: maxTeamSize is not an integer

# CSV-E043: minTeamSize is larger than maxTeamSize

# CSV-E060: duplicate projectID column

# CSV-S005: excessive number of projectID rows

# CSV-S006: exccessive number of blank lines