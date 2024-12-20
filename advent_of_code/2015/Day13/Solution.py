
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json
import itertools

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

def parseinput(inputlist):
    rels = {}
    for row in inputlist:
        inst = row.split(" ")
        if inst[0][0] not in rels:
            rels[inst[0][0]] = {}
        if inst[2] == "gain":
            rels[inst[0][0]][inst[-1][0]] = int(inst[3])
        else:
            rels[inst[0][0]][inst[-1][0]] = -int(inst[3])
    return rels


#%%
def part1(inputlist):
    max_score = 0
    rels = parseinput(inputlist)
    perm_list = list(itertools.permutations([x for x in rels]))

    for perm in perm_list:
        score = 0
        new_perm = [perm[-1]]+list(perm)+[perm[0]]
        for ii in range(1,len(perm)+1):
            score = score + rels[new_perm[ii]][new_perm[ii-1]]+rels[new_perm[ii]][new_perm[ii+1]]
        if score > max_score:
            max_score = score    
    return max_score


#%%

def part2(inputlist):
    max_score = 0
    rels = parseinput(inputlist)
    rels['Me'] = {}
    for person in rels:
        rels['Me'][person] = 0
        rels[person]['Me'] = 0

    perm_list = list(itertools.permutations([x for x in rels]))

    for perm in perm_list:
        score = 0
        new_perm = [perm[-1]]+list(perm)+[perm[0]]
        for ii in range(1,len(perm)+1):
            score = score + rels[new_perm[ii]][new_perm[ii-1]]+rels[new_perm[ii]][new_perm[ii+1]]
        if score > max_score:
            max_score = score    
    return max_score


#%%