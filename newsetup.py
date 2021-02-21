import sys
import pathlib
from decimal import Decimal

if len(sys.argv) != 2:
    print("""
    Usage: python3 newsetup.py datatype
    Here, datatyle is either "region" or "disease"
    """)
    sys.exit(1)

datatype = True #true = region, false = disease
datastring = sys.argv[1]

if datastring == "region": datatype = True
elif datastring == "disease": datatype = False
else:
    print("""
    Usage: python3 newsetup.py datatype
    Here, datatype is either "region" or "disease"
    """)
    sys.exit(1)

dataname = input("enter data name (e.g. covid or usa): ")
datafound = pathlib.Path('constants/' + datastring + '/' + dataname).is_file()

if datafound:
    datfile = open('constants/' + datastring + '/' + dataname, 'rt')
outfile = open('temp/' + datastring + '/' + dataname, 'w')

dictinf = {}

if datatype: 
    dictinf["deathrate"] = None
    dictinf["birthrate"] = None
    dictinf["initpop"] = None
else:
    dictinf["virulence"] = None
    dictinf["sicklength"] = None
    dictinf["infectivity"] = None
    dictinf["appearance"] = 0
    dictinf["howmany"] = 1

#parse lines
if datafound:
    for line in datfile.readlines():
        arr = line.split()
        dictinf[arr[0]] = float(arr[1])

for key, val in dictinf.items():
    if val is None:
        dictinf[key] = float(input("enter value of " + key + " (current/default value is " + str(val) + "): "))
    else:
        dictinf[key] = float(input("enter value of " + key + " (current/default value is " + str(Decimal(val)) + "): "))

for key, val in dictinf.items():
    outfile.write(str(key) + " " + str(Decimal(val)) + "\n")

datfile.close()
outfile.close()
