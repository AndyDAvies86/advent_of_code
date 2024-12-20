# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:00:46 2020

@author: Andy
"""

import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

#file = open("2020day15.txt","r")
#start = file.read()
#startlist = start.split("\n")
#
#file = open("2020day15test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

start = "12,20,0,6,1,17,7"
test = "1,3,2"

def part1(inputlist,time):
    splitlist = inputlist.split(",")
    turns = [int(x) for x in splitlist]
    revturns = turns[::-1]
    while len(revturns)<time:
        if revturns[0] in revturns[1:]:
            revturns = [revturns.index(revturns[0],1)]+revturns
        else:
            revturns = [0]+revturns
    return revturns[0]

def inspect(inputlist,time):
    splitlist = inputlist.split(",")
    turns = [int(x) for x in splitlist]
    revturns = turns[::-1]
    while len(revturns)<time:
        if revturns[0] in revturns[1:]:
            revturns = [revturns.index(revturns[0],1)]+revturns
        else:
            revturns = [0]+revturns
    return revturns[::-1]

def findloop(inputlist):
    pass

def part2(inputlist,time):
    turnslist = {}
    splitlist = inputlist.split(",")
    turns = [int(x) for x in splitlist]
    for i in range(0,len(turns)-1):
        turnslist[turns[i]] = i
    i = len(turns)-1
    temp = turns[-1]
    while i < time-1:
        if temp not in turnslist:
            newtemp = 0
        else:
            newtemp = i-turnslist[temp]
        turnslist[temp] = i
        temp = copy.deepcopy(newtemp)
        if i % 1000000 == 0:
            print(str(int(i/1000000))+"M")
        i+=1
    return newtemp
        