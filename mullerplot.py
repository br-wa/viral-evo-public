import sys
import numpy
import pandas
import os
import pathlib

if len(sys.argv) < 2:
    print("""
    Usage: python3 mullerplot.py name dis1 dis2 etc
    outputs to plotted/name
    """)
    sys.exit(1)

data = pandas.read_csv('output.csv')

disList = sys.argv[2:]
popData = []
disData = []
label = {}

for dis in disList:
    if not pathlib.Path('temp/disease/' + dis).is_file():
        print("disease " + dis + " not found")
    f = open('temp/disease/' + dis,'r')
    curl = dis + " ("
    for line in f.readlines():
        strs = line.split()
        if strs[0] == "virulence":
            curl = curl + "v = " + '{:.2E}'.format(float(strs[1])) + ", "
        if strs[0] == "infectivity":
            curl = curl + "b = " + '{:.2E}'.format(float(strs[1])) + ")"
    label[dis] = curl

for dis in disList:
    disData.append(["none",label[dis]])
    curdat = data["total " + dis + " infected"]
    for i in range(curdat.size):
        popData.append([i,label[dis],curdat[i]])

for i in range(len(data)):
    popData.append([i,"none",0])

popFrame = pandas.DataFrame(data=popData,columns=["Generation","Identity","Population"])
disFrame = pandas.DataFrame(data=disData,columns=["Parent","Identity"])

popFrame.to_csv('popFrame.csv',index=False)
disFrame.to_csv('disFrame.csv',index=False)

os.system('Rscript mullerplot.r \'' + sys.argv[1] + '\'')
