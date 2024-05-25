
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
def setforest(inputlist):
    forest = np.array([[int(x) for x in row] for row in inputlist])
    return forest

#%%


#%%
def part1(inputlist):
    forest = setforest(inputlist)
    visible = 0
    for x in range(0,len(forest[0])):
        for y in range(0,len(forest)):
            ycheck = [forest[y,x] - z for z in forest[y,:]]
            xcheck = [forest[y,x] - z for z in forest[:,x]]
            if x == 0 or x == len(forest[0])-1 or y == 0 or y == len(forest)-1:
                visible += 1
            elif min(ycheck[:x]) > 0 or min(ycheck[x+1:]) > 0 or min(xcheck[:y]) > 0 or min(xcheck[y+1:]) > 0:
                visible += 1
            #print(x,y,visible)
    return visible
#%%

def part2(inputlist):
    forest = setforest(inputlist)
    scenemax = 0
    for x in range(0,len(forest[0])):
        for y in range(0,len(forest)):
            scene = [0,0,0,0]
            ycheck = [forest[y,x] - z for z in forest[y,:]]
            xcheck = [forest[y,x] - z for z in forest[:,x]]
            scenelist = [ycheck[:x][::-1],ycheck[x+1:],xcheck[:y][::-1],xcheck[y+1:]]
            for jj in range(0,4):
                for ii in range(0,len(scenelist[jj])):
                    if scenelist[jj][ii] > 0:
                        scene[jj] += 1
                    else:
                        scenelist[jj][ii] == 0
                        scene[jj] += 1
                        break
            #print(x,y,forest[y,x],scenelist,scene)
            if np.prod(scene) > scenemax:
                scenemax = np.prod(scene)
    return scenemax
#%%