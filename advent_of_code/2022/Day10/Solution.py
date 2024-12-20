
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%

#%%


#%%


#%%
def part1(inputlist):
    X = 1
    cycle = 1
    Xlist = []
    for row in inputlist:
        if row == 'noop':
            cycle += 1
            if cycle % 40 == 20:
                Xlist.append(X)
        if row.split(" ")[0] == 'addx':
            addvalue = int(row.split(" ")[1])
            cycle += 1
            if cycle % 40 == 20:
                Xlist.append(X)
            cycle += 1
            X += addvalue
            if cycle % 40 == 20:
                Xlist.append(X)
    newXlist = [Xlist[ii]*(20+40*ii) for ii in range(0,6)]
    print(Xlist)
    print(newXlist)
    return sum(newXlist)
            

#%%

def part2(inputlist):
    X = 1
    cycle = 0
    Xlist = []
    for row in inputlist:
        if row == 'noop':
            if abs(cycle%40-X) <= 1:
                Xlist.append('#')
            else:
                Xlist.append(' ')
            cycle += 1
        if row.split(" ")[0] == 'addx':
            addvalue = int(row.split(" ")[1])
            if abs(cycle%40-X) <= 1:
                Xlist.append('#')
            else:
                Xlist.append(' ')
            cycle += 1
            if abs(cycle%40-X) <= 1:
                Xlist.append('#')
            else:
                Xlist.append(' ')
            X += addvalue
            cycle += 1
    Outputlist = [''.join(Xlist[ii:ii+39]) for ii in range(0,240,40)]
    return Outputlist
#%%