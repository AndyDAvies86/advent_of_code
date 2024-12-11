
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
    pos = []
    total = []
    for row in inputlist:
        sprow = row.split(' ')
        x = int(sprow[1][1:])
        p = int(sprow[-1][:-1])
        t = int(sprow[3])
        pos.append(p)
        total.append(t)
    return pos,total
#%%

def part1(inputlist):
    pos,total = parselist(inputlist)
    t = 0
    # d=0
    go = True
    # print(t,pos,total)
    while go:
        newpos = [(pos[ii] + t+ii+1) % total[ii] for ii in range (0,len(pos))]
        # print(t,newpos)
        if sum(newpos) == 0:
            return t
        t = t+1


#%%

def part2(inputlist):
    pos,total = parselist(inputlist)
    pos = pos+[0]
    total = total+[11]
    t = 0
    # d=0
    go = True
    # print(t,pos,total)
    while go:
        newpos = [(pos[ii] + t+ii+1) % total[ii] for ii in range (0,len(pos))]
        # print(t,newpos)
        if sum(newpos) == 0:
            return t
        t = t+1
#%%