# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day5test.txt","r")
starttest = filetest.read()
test = starttest.split("\n")

file = open("2021day5input.txt","r")
start = file.read()
startlist = start.split("\n")

def linesperp(inputlist):
    linesperp = []
    linesdiag = []
    for row in inputlist:
        preprow = row.split(" ")
        newrow = []
        newrow.append([int(x) for x in preprow[0].split(",")])
        newrow.append([int(x) for x in preprow[2].split(",")])
        if newrow[0][0] == newrow [1][0] or newrow[0][1] == newrow [1][1]:
            linesperp.append(newrow)
        else:
            linesdiag.append(newrow)
    return linesperp,linesdiag

    
def vents(inputlist):
    lines = linesperp(inputlist)[0]
    vents = []
    for line in lines:
        for ii in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
            for jj in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
                vents.append((ii,jj))
    return vents
            
def ventsdiag(inputlist):
    lines = linesperp(inputlist)[1]
    vents = []
    for line in lines:
        length = max(line[0][0],line[1][0])-min(line[0][0],line[1][0])
        direction = (int((line[1][0]-line[0][0])/length),int((line[1][1]-line[0][1])/length))
#        print(line,length,direction)
        for ii in range(0,length+1):
            newvent = (line[0][0]+ii*direction[0],line[0][1]+ii*direction[1])
            vents.append(newvent)
#        print(vents)
    return vents

def part1(inputlist):
    ventlist = vents(inputlist)
    dedupe = list(set(ventlist))
    ventdict = {x:0 for x in dedupe}
#    print(len(ventlist),len(dedupe))
    dupecount = 0
    for vent in ventlist:
        ventdict[vent] += 1
    for vent in dedupe:
        if ventdict[vent] > 1:
            dupecount += 1
    return dupecount
        
def part2(inputlist):
    ventlist = vents(inputlist) + ventsdiag(inputlist)
    dedupe = list(set(ventlist))
    ventdict = {x:0 for x in dedupe}
#    print(len(ventlist),len(dedupe))
    dupecount = 0
    for vent in ventlist:
        ventdict[vent] += 1
    for vent in dedupe:
        if ventdict[vent] > 1:
            dupecount += 1
#            print(vent)
    return dupecount
        
