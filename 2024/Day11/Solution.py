
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
    stonelist = [int(x) for x in inputlist[0].split(' ')]
    stonedict = {stone: stonelist.count(stone) for stone in stonelist}
    return stonedict

#%%

def op1(inputlist):
    stones = [int(x) for x in inputlist[0].split(' ')]
    for ii in range(0,25):
        newstones = []
        for stone in stones:
            if stone == 0:
                newstones.append(1)
            elif len(str(stone))%2 == 0:
                x = len(str(stone))//2
                newstones = newstones+[int(str(stone)[:x]),int(str(stone)[x:])]
            else:
                newstones.append(2024*stone)
        stones = copy.deepcopy(newstones)
        print(len(stones))
    return len(stones)

def oblinks(inputlist,n):
    stones = [int(x) for x in inputlist[0].split(' ')]
    for ii in range(0,n):
        newstones = []
        for stone in stones:
            if stone == 0:
                newstones.append(1)
            elif len(str(stone))%2 == 0:
                x = len(str(stone))//2
                newstones = newstones+[int(str(stone)[:x]),int(str(stone)[x:])]
            else:
                newstones.append(2024*stone)
        stones = copy.deepcopy(newstones)
        print(len(stones))
    return {stone:stones.count(stone) for stone in stones}

def stblink(stone):
    if stone == 0:
        return {1:1}
    elif len(str(stone))%2 == 0:
        x = len(str(stone))//2
        if int(str(stone)[:x]) == int(str(stone)[x:]):
            return {int(str(stone)[:x]):2}#
        else:
            return {int(str(stone)[:x]):1,int(str(stone)[x:]):1}
    else:
        return {2024*stone:1}

def blink(stones):
    newstones = {}
    for stone in stones:
        newstone = stblink(stone)
        for ns in newstone:
            if ns not in newstones:
                newstones[ns] = 0
            newstones[ns] = newstones[ns]+stones[stone]*newstone[ns]
    return newstones

def blinks(inputlist,n):
    stones = parselist(inputlist)
    for ii in range(0,n):
        stones = blink(stones)
        print(sum([stones[x] for x in stones]))
    return stones


def part1(inputlist):
    stones = parselist(inputlist)
    for ii in range(0,25):
        stones = blink(stones)
    return sum([stones[x] for x in stones])
#%%

def part2(inputlist):
    stones = parselist(inputlist)
    for ii in range(0,75):
        stones = blink(stones)
    return sum([stones[x] for x in stones])
#%%