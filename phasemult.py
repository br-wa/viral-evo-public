#!/usr/bin/python3

import matplotlib.pyplot
import numpy
import sys
import os
import pandas
import decimal
from math import log

def readfile(disfile):
    f = open('temp/disease/' + disfile,'r')
    dictinf = {}
    for line in f.readlines():
        arr = line.split()
        dictinf[arr[0]] = float(arr[1])
    f.close()
    return dictinf

numdays = 1500
modify = readfile('variable')
ctrl = readfile('control')
ctrl2 = readfile('control2')
ti = "total infected"
tvi = "total variable infected"

def writemod(disfile):
    f = open('temp/disease/' + disfile,'w')
    for key, val in modify.items():
        f.write(str(key) + " " + str(decimal.Decimal(val)) + "\n")
    f.close()

def operate(ratio):
    return log(ratio)/log(2)

def iter(virul,inf):
    modify['virulence'] = virul
    modify['infectivity'] = inf
    writemod('variable')
    os.system("./sir " + str(numdays) + " usa control control2 variable > output.csv")
    data = pandas.read_csv('output.csv')
    lastnonempty = numdays
    while data[ti][lastnonempty] == 0 and data[tvi][lastnonempty] == 0:
        lastnonempty = lastnonempty-1
    return (float(data[tvi][lastnonempty])+0.000001)/(float(data[ti][lastnonempty] - data[tvi][lastnonempty])+0.000001)

def main():
    if len(sys.argv) != 5:
        print("""
        Usage: python3 phase.py virul_increment #virul infec_increment #infec
        """)
        exit(1)
    title = input("enter title: \n")
    virul = []
    infec = []
    x = []
    y = []
    s = []
    rarray = []
    maxr = 0.0
    for i in range(1,int(sys.argv[2])+1):
        virul.append(i * float(sys.argv[1]))
    for i in range(1,int(sys.argv[4])+1):
        infec.append(i * float(sys.argv[3]))
    for v in virul:
        print("running " + str(v))
        for b in infec:
            y.append(v)
            x.append(b)
            r = operate(iter(v,b))
            if r < -20:
                rarray.append(-20)
            elif r > 20:
                rarray.append(20)
            else:
                rarray.append(r)
    for r in rarray:
        maxr = max(maxr,abs(r))
    matplotlib.pyplot.title(title + '\n colored based on log2(variable prevalence/control prevalence) capped at +-20 \n control 1: infectivity ' + str(ctrl['infectivity']) + ' and virulence ' + str(ctrl['virulence']) + '\n control 2: infectivity ' + str(ctrl2['infectivity']) + ' and virulence ' + str(ctrl2['virulence']))
    fig = matplotlib.pyplot.scatter(x,y,c=rarray,cmap='coolwarm',vmin=-maxr,vmax=maxr)
    matplotlib.pyplot.scatter([ctrl['infectivity'],ctrl2['infectivity']],[ctrl['virulence'],ctrl2['virulence']],s=[50],marker="x",c='black')
    matplotlib.pyplot.xlim(0.0,float(sys.argv[4]) * float(sys.argv[3]))
    matplotlib.pyplot.ylim(0.0,float(sys.argv[2]) * float(sys.argv[1]))
    matplotlib.pyplot.xlabel('new virus infectivity')
    matplotlib.pyplot.ylabel('new virus virulence')
    matplotlib.pyplot.colorbar(fig)
    matplotlib.pyplot.savefig('phaseplot/myplot.png',bbox_inches='tight') 

if __name__ == "__main__":  
    main()
