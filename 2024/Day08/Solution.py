
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
    ants = {}
    for jj in range(0,len(inputlist)):
        for ii in range(0,len(inputlist[0])):
            if inputlist[jj][ii] != '.':
                if inputlist[jj][ii] not in ants:
                    ants[inputlist[jj][ii]] = []
                ants[inputlist[jj][ii]] = ants[inputlist[jj][ii]]+[[ii,jj]]
    return ants
#%%

def part1(inputlist):
    ants = parselist(inputlist)
    antinodes = set()
    ht = len(inputlist)
    wd = len(inputlist[0])
    for ant in ants:
        for perm in list(it.permutations(ants[ant],2)):
            anode = (2*perm[0][0]-perm[1][0],2*perm[0][1]-perm[1][1])
            # print(ant,perm,anode)
            if 0<=anode[0]<wd and 0<=anode[1]<ht:
                antinodes.add(anode)
                # print("Yes")
    return len(antinodes)
#%%

def part2(inputlist):
    ants = parselist(inputlist)
    antinodes = set()
    ht = len(inputlist)
    wd = len(inputlist[0])
    for ant in ants:
        for perm in list(it.permutations(ants[ant],2)):
            for m in range(0,max(ht,wd)):
                anode = ((m+1)*perm[0][0]-m*perm[1][0],(m+1)*perm[0][1]-m*perm[1][1])
                # print(ant,perm,anode)
                if 0<=anode[0]<wd and 0<=anode[1]<ht:
                    antinodes.add(anode)
                    # print("Yes")
    return len(antinodes)
#%%