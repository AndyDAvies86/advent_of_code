
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
def parsepuzzle(inputlist):
    numlist1 = sorted([int(x.split("  ")[0]) for x in inputlist])
    numlist2 = sorted([int(x.split("  ")[1]) for x in inputlist])
    return numlist1,numlist2
#%%

def part1(inputlist):
    nl1,nl2 = parsepuzzle(inputlist)
    diff = 0
    for ii in range(0,len(nl1)):
        newdiff = abs(nl1[ii]-nl2[ii])
        diff = diff+newdiff
    return diff

#%%

def part2(inputlist):
    nl1,nl2 = parsepuzzle(inputlist)
    score = 0
    for ii in range(0,len(nl1)):
        newscore = nl1[ii]*sum([x == nl1[ii] for x in nl2])
        score = score+newscore
    return score

#%%