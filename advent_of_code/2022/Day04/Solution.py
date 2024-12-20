
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

def part1(inputlist):
    contained = 0
    for row in inputlist:
        ranges = [[int(x) for x in y.split("-")] for y in row.split(",")]
        if (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]) or (ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]):
            contained += 1
            #print(ranges)
    return contained
#%%

def part2(inputlist):
    contained = 0
    for row in inputlist:
        ranges = [[int(x) for x in y.split("-")] for y in row.split(",")]
        test = 0
        if (ranges[0][0] in range(ranges[1][0],ranges[1][1]+1) or ranges[0][1] in range(ranges[1][0],ranges[1][1]+1)) or (ranges[1][0] in range(ranges[0][0],ranges[0][1]+1) or ranges[1][1] in range(ranges[0][0],ranges[0][1]+1)):
            contained += 1
            test = 1
        #print(ranges,test)
    return contained
#%%