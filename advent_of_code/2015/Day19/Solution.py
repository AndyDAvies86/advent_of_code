
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

file = open("inputtest2.txt","r")
startc = file.read()
testlistb = startb.split("\n")


#%%

def parselist(inputlist):
    start = inputlist[-1]
    reps = [x.split(" => ") for x in inputlist[:-2]]
    return start,reps
#%%

def part1(inputlist):
    mols = set([])
    start,reps = parselist(inputlist)
    for rep in reps:
        for ii in range(0,len(start)+1-len(rep[0])):
            newmol = start[:ii]+start[ii:].replace(rep[0],rep[1],1)
            if newmol != start:
                mols.add(newmol)
    # print(mols)
    return len(mols)
#%%

def part2(inputlist):
    pass
#%%