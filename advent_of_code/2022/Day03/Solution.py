
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
    overlap = []
    for row in inputlist:
        halfrow = int(len(row)/2)
        row1 = [x for x in row[0:halfrow]]
        row2 = [x for x in row[halfrow:]]
        overlap.append(list(set(row1).intersection(set(row2)))[0]) 
        lookup = alphabet+alphaup
        score = [lookup.index(x)+1 for x in overlap]
    return sum(score)
#%%

def part2(inputlist):
    elfgroups = int(len(inputlist)/3)
    lookup = alphabet+alphaup
    badges = []
    for ii in range(0,elfgroups):
        badge = list(set(inputlist[3*ii]).intersection(set(inputlist[3*ii+1])).intersection(set(inputlist[3*ii+2])))[0]
        badges.append(badge)
    score = [lookup.index(x)+1 for x in badges]
    return sum(score)
#%%