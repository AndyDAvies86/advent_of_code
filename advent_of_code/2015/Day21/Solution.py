
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
testlist = startb.split("\n\n")


#%%

def parselist(inputlist):
    hp = int(inputlist[0].split(": ")[1])
    dm = int(inputlist[1].split(": ")[1])
    ar = int(inputlist[2].split(": ")[1])
    return [hp,dm,ar]

def kit(inputlist):
    
    weapons = [[int(x[12:15]),int(x[20]),int(x[28])] for x in inputlist[0].split("\n")[1:]]
    armor = [[int(x[12:15]),int(x[20]),int(x[28])] for x in inputlist[1].split("\n")[1:]]
    rings = [[int(x[12:15]),int(x[20]),int(x[28])] for x in inputlist[2].split("\n")[1:]]
    return weapons,armor,rings

#%%

def battle (boss,hero):
    print('b',boss,'h',hero)
    # print(hero)
    t = 0
    while boss[0] >= 0 and hero[0] >= 0:
        boss[0] = boss[0] - hero[1] + boss[2]
        if boss[0] < 0:
            print(t)
            return 'hero'
        hero[0] = hero[0] - boss[1] + hero[2]
        if hero[0] < 0:
            print(t)
            return 'boss'
        t = t+1
    return 'Error'

def part1(inputlist):
    boss = parselist(inputlist)
    kitlist = kit(testlist)
    for h in [[x,11-x] for x in range(3,12)]:
        print(h,battle(copy.deepcopy(boss),[100]+h))
#%%

def part2(inputlist):
    pass
#%%