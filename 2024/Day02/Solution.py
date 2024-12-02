
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
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%

def parselist(inputlist):
    return [[int(x) for x in row.split(" ")] for row in inputlist]


def testsafe(rep):
    changes = [rep[ii]-rep[ii-1] for ii in range(1,len(rep))]
    if min(changes) >= -3 and max(changes) <= -1:
        return 1
    elif min(changes) >= 1 and max(changes) <= 3:
        return 1
    return 0
#%%

def part1(inputlist):
    reports = parselist(inputlist)
    safe = 0
    for rep in reports:
        safe = safe+testsafe(rep)
        # print(rep,changes,safe)
    return safe
#%%

def removes(rep):
    if testsafe(rep[1:]) == 1:
        return 1
    elif testsafe(rep[:-1]) == 1:
        return 1
    for ii in range(1,len(rep)-1):
        if testsafe(rep[:ii]+rep[ii+1:]) == 1:
            return 1
    return 0



def part2(inputlist):
    reports = parselist(inputlist)
    safe = 0
    for rep in reports:
        if testsafe(rep) == 1:
            safe = safe+1
        else:
            safe = safe+removes(rep)

    return safe
#%%