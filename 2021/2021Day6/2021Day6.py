# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day6test.txt","r")
starttest = filetest.read()
test = [int(x) for x in starttest.split(",")]

file = open("2021day6input.txt","r")
start = file.read()
startlist = [int(x) for x in start.split(",")]


def newday(inputlist):
    newfisha = []
    newfishb = []
    for fish in inputlist:
        if fish == 0:
#            print(fish)
            newfisha.append(6)
            newfishb.append(8)
#            print(inputlist)
        else:
#            print(fish)
            newfisha.append(fish-1)
#            print(inputlist)
    newfish = newfisha+newfishb
    return newfish
            
def fishtime(inputlist,days):
#    print("Initial state: "+str(inputlist))
    for ii in range(0,days):
        inputlist = newday(inputlist)
#        print("After "+str(ii+1)+" days: "+str(inputlist))
    return len(inputlist)


def firstdict(inputlist):
    fishlist = {x:0 for x in range (0,9)}
    for fish in inputlist:
        fishlist[fish] += 1
    return fishlist

def newdayfast(inputdict):
    newdict = {x:0 for x in range (0,9)}
    for ii in range (0,8):
        newdict[ii] = inputdict[ii+1]
    newdict[6] += inputdict[0]
    newdict[8] = inputdict[0]
    return newdict

def fastday(inputlist,days):
    fishdict = firstdict(inputlist)
    for ii in range(0,days):
        fishdict = newdayfast(fishdict)
#        print("After "+str(ii+1)+" days: "+str(fishdict))
    return sum([fishdict[x] for x in range(0,9)])