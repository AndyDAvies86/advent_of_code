
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

file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")
#%%

def part1(inputlist):
    stringlength = 0
    reduction = 0
    for row in inputlist:
        stringlength += len(row)
        reduction +=2
        ii = 0
        while ii < len(row):
            print(str(ii)+" "+row[ii])
            if row[ii] == "\\" :
                if row[ii+1] == "x":
                    reduction = reduction + 3
                    ii = ii + 4
                else:
                    reduction = reduction + 1
                    ii = ii + 2
            else:
                ii = ii + 1
    print (stringlength)
    print(stringlength-reduction)
    return reduction
#%%


def part2(inputlist):
    stringlength = 0
    newstringlength = 0
    for row in inputlist:
        stringlength += len(row)
        newstring = "\""
        for char in row:
            if char == "\\":
                newstring += "\\\\"
            elif char == "\"" :
                newstring += "\\\""
            else:
                newstring += char
        newstring += "\""
        print(newstring)
        newstringlength += len(newstring)
    print(newstringlength)
    print(stringlength)
    return newstringlength-stringlength

#%%