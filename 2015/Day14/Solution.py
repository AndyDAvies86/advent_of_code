
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
    speed = {}
    go = {}
    rest = {}
    cycle ={}
    for row in inputlist:
        x = row.split(" ")
        speed[x[0]] = int(x[3])
        go[x[0]] = int(x[6])
        rest[x[0]] = int(x[-2])
        cycle[x[0]] = go[x[0]] + rest[x[0]]
    return speed,go,rest,cycle


#%%
def part1(inputlist,time):
    speed,go,rest,cycle = parseinput(inputlist)
    dist = {}
    for rd in speed:
        cycles = time//cycle[rd]
        rem = time % cycle[rd]
        dist[rd] = (cycles*go[rd]+min(rem,go[rd]))*speed[rd]
        # print(rd,time,cycles,rem,dist[rd])
    score = max([dist[rd] for rd in dist])
    return score


#%%

def part2(inputlist,time):
    speed,go,rest,cycle = parseinput(inputlist)
    pts = {}
    for rd in speed:
        pts[rd] = 0
    for t in range (1,time):
            dist = {}
            winner = part1(inputlist,t)
            for rd in speed:
                cycles = t//cycle[rd]
                rem = t % cycle[rd]
                dist[rd] = (cycles*go[rd]+min(rem,go[rd]))*speed[rd]
                # print(rd,time,cycles,rem,dist[rd])
                if dist[rd] == winner:
                    pts[rd] = pts[rd] + 1
    score = max([pts[rd] for rd in pts])
    return score

#%%