
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
    return [[99]*(len(inputlist[0])+2)]+[[99]+[int(x) for x in y]+[99] for y in inputlist]+[[99]*(len(inputlist[0])+2)]
#%%

def allsteps(map):
    upsteps = {}
    downsteps = {}
    for kk in range(0,len(map)):
        upsteps[(kk,0)] = []
        downsteps[(kk,0)] = []
        upsteps[(kk,len(map[0])-1)] = []
        downsteps[(kk,len(map[0])-1)] = []
    for kk in range(0,len(map[0])):
        upsteps[(0,kk)] = []
        downsteps[(0,kk)] = []
        upsteps[(len(map)-1,kk)] = []
        downsteps[(len(map[0])-1,kk)] = []

    for ii in range(1,len(map)-1):
        for jj in range(1,len(map)-1):
            u_valid = []
            d_valid = []
            for d in [[-1,0],[1,0],[0,-1],[0,1]]:
                if map[ii+d[0]][jj+d[1]] - map[ii][jj] == 1:
                    u_valid.append([ii+d[0],jj+d[1]])
                elif map[ii+d[0]][jj+d[1]] - map[ii][jj] == -1:
                    d_valid.append([ii+d[0],jj+d[1]])
            upsteps[(ii,jj)] = u_valid
            downsteps[(ii,jj)] = d_valid
    return upsteps,downsteps

def addruns(runs,uplist):
    newruns = []
    for run in runs:
        for ii in range(0,len(uplist[tuple(run[-1])])):
            newrun = run+[uplist[tuple(run[-1])][ii]]
            if newrun not in newruns:
                newruns.append(newrun)
    return newruns

def part1(inputlist):
    map = parselist(inputlist)
    upsteps,downsteps = allsteps(map)
    runs = [[[x,y]] for x in range(0,len(map)) for y in range (0,len(map[0]))]
    a = 0
    while a < 9:
        a = a+1
        newruns=addruns(runs,upsteps)
        runs = copy.deepcopy(newruns)
    th = set()
    for run in runs:
        new_th = tuple([tuple(run[0]),tuple(run[-1])])
        th.add(new_th)
    return len(th)
#%%

def part2(inputlist):
    map = parselist(inputlist)
    upsteps,downsteps = allsteps(map)
    # print(upsteps)
    runs = [[[x,y]] for x in range(0,len(map)) for y in range (0,len(map[0]))]
    # print(runs)
    a = 0
    while a < 9:
        a = a+1
        newruns=addruns(runs,upsteps)
        runs = copy.deepcopy(newruns)
    return print(sum([len(x) == 10 for x in newruns]))
#%%