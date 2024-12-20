
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
    walls = []
    for jj in range(0,len(inputlist)):
        for ii in range(0,len(inputlist[0])):
            if inputlist[jj][ii] == '#':
                walls.append([ii,jj])
            if inputlist[jj][ii] == '^':
                start = [ii,jj]
    return walls, start
#%%

def p1_ex_count(inputlist):
    directions = [[0,-1],[1,0],[0,1],[-1,0]]
    d = 0
    walls, pos = parselist(inputlist)
    allpos = set()

    while 0 <= pos[0] < len(inputlist[0]) and 0 <= pos[1] < len(inputlist):
        allpos.add(tuple(pos))
        # print(d,pos,directions[d])
        new_pos = [pos[0]+directions[d][0],pos[1]+directions[d][1]]
        if new_pos in walls:
            d = (d+1) % 4
        else:
            pos = new_pos
    return allpos

def part1(inputlist):
    return len(p1_ex_count(inputlist))
            
#%%

def checkobs(inputlist,walls,pos):
    # print(walls)
    allpos=set()
    directions = [[0,-1],[1,0],[0,1],[-1,0]]
    d = 0
    while 0 <= pos[0] < len(inputlist[0]) and 0 <= pos[1] < len(inputlist):
        # print(d,pos,directions[d])
        allpos.add(tuple(pos+[d]))
        new_pos = [pos[0]+directions[d][0],pos[1]+directions[d][1]]
        # print(new_pos)
        if tuple(new_pos+[d]) in allpos:
            return 1
        elif new_pos in walls:
            d = (d+1) % 4
        else:
            pos = new_pos
            # print(pos,directions[d])
    return allpos

def part2(inputlist):
    old_walls,pos = parselist(inputlist)
    # print(old_walls)
    to_check = p1_ex_count(inputlist)
    # print(to_check)
    new_walls = []
    m = 0
    print (len(to_check))
    for check in to_check:
        # print(check)
        ii = check[0]
        jj = check[1] 
        if [ii,jj] not in new_walls:
            # print(ii,jj,m)
            m = m+1
            if m%100 == 0:
                print(m)
            walls  = old_walls+[[ii,jj]]
            # print(walls)
            if checkobs(inputlist,walls,pos) == 1:
                new_walls.append([ii,jj])
    return len(new_walls)
#%%